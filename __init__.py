"""
Initialize rush plugin commands

"""

from __future__ import print_function
import inspect
import json
import sys
import imp
import os
from maya import cmds


def loadConfig():
    """ Load config file

    Return:
        config(list): List of path module paths

    """
    configFilePath = os.path.normpath(os.path.join(
        cmds.internalVar(userScriptDir=True), 'rush.json'))

    defaultModulePath = os.path.normpath(os.path.join(
        cmds.internalVar(userScriptDir=True), 'rush', 'module'))

    config = [defaultModulePath]

    # Use only default module path if config file does not exist
    if not os.path.exists(configFilePath):
        print("Additional config file not found: %s" % configFilePath)
        return config

    # Open and load config file in use home dir and append it to the
    # config list
    try:
        fileData = open(configFilePath, 'r')
        extraConfig = json.load(fileData)
        additionalPaths = extraConfig["path"]
        fileData.close()
    except IOError:
        print("Failed to load config file")

    config.extend(additionalPaths)

    return config


def getModulePath(moduleDirPath):
    """ Create and return a list of module paths

    Args:
        moduleDirPath (str): directory path to search modules

    Return:
        mods (list): List of module paths
        None: if the path doesn't exist

    """
    if not os.path.exists(moduleDirPath):
        return None

    # Get all files in the directory
    allFiles = [os.path.join(root, filePath) for root, _, files
                in os.walk(moduleDirPath) for filePath in files]

    # Get only python files
    pythonFiles = [i for i in allFiles if i.endswith(".py")]

    # Remove __init__ and main plugin file
    mods = [filePath for filePath in pythonFiles
            if not filePath.endswith("__init__.py") and not filePath.endswith("Rush.py")]

    return mods


def loadModule(modulePath):
    """ Load module

    Args:
        modulePath (str): Full path to the python module

    Return:
        mod (module object): command module
        None: if path doesn't exist

    """
    # Create module names for import, for exapmle ...
    #
    # "rush/template"
    # "animation/animate"
    # "common/create"
    # "common/display"

    normPath = os.path.normpath(modulePath)

    if sys.platform == "win32":
        name = os.path.splitext(normPath)[0].split("\\")
    else:
        name = os.path.splitext(normPath)[0].split("/")

    name = "/".join(name[-2:])

    # If arnold is not loaded or installed, ignore modules for arnold
    if name.startswith("Arnold"):
        hasArnold = cmds.pluginInfo("mtoa", q=True, loaded=True)
        if not hasArnold:
            return None

    try:
        mod = imp.load_source(name, modulePath)
        return mod
    except Exception:
        print("Failed to load module : %s" % modulePath)
        return None


class TmpCls(object):

    commandDict = {}


for path in loadConfig():
    normpath = os.path.normpath(path)
    if os.path.exists(normpath):
        module_paths = getModulePath(path)
        for module_path in module_paths:
            m = loadModule(module_path)
            try:
                tempDict = {}
                for cmd in m.commandDict:
                    displayName = cmd[:1].capitalize() + cmd[1:]
                    command_data = {}
                    command_data[displayName] = {}
                    command_data[displayName]['icon'] = m.commandDict[cmd]
                    command_data[displayName]['path'] = module_path
                    command_data[displayName]['command'] = cmd
                    command_data[displayName]['module'] = m.__name__
                    tempDict.update(command_data)
                TmpCls.commandDict.update(tempDict)
            except AttributeError:
                pass
            fs = inspect.getmembers(m, inspect.isfunction)
            for f in fs:
                setattr(TmpCls, f[0], staticmethod(f[1]))
