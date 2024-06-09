# -*- coding: utf-8 -*-

""" Initialize rush plugin commands

"""

import inspect
import json
import sys
import imp
import os
import glob
from collections import OrderedDict
from operator import getitem
from maya import cmds


def __loadConfig() -> list:
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


def __getModulePath(moduleDirPath: str) -> list:
    """ Create and return a list of module paths

    Args:
        moduleDirPath (str): directory path to search modules

    Return:
        mods (list): List of module paths
    """

    if not os.path.exists(moduleDirPath):
        return []

    # Get all module files in the directories

    module_paths = []

    for root, _, files in os.walk(moduleDirPath):
        for f in files:
            if f.endswith(".py"):
                path = os.path.join(root, f)
                module_paths.append(path)

    return module_paths


def __loadModule(modulePath: str):
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

    try:
        mod = imp.load_source(name, modulePath)
        return mod
    except Exception:
        print("Failed to load module : %s" % modulePath)
        return None


class TmpCls(object):

    commandDict = {}


MODULES = []


for module_dir in __loadConfig():
    normpath = os.path.normpath(module_dir)
    if os.path.exists(normpath):
        module_paths = __getModulePath(module_dir)
        for i in module_paths:
            MODULES.append(i)


for module_name in MODULES:
    m = __loadModule(module_name)

    try:
        tempDict = {}
        for cmd in m.commandDict:
            displayName = cmd[:1].capitalize() + cmd[1:]

            # id = str(uuid.uuid4())
            id = displayName + "_exmod"
            command_data = {}
            command_data[id] = {
                    'label': displayName,
                    'icon': m.commandDict[cmd],
                    'path': module_name,
                    'command': cmd,
                    'module': m.__name__,
                    'sourceType': "python",
                }
            tempDict.update(command_data)
        TmpCls.commandDict.update(tempDict)
    except AttributeError:
        pass

    functions = inspect.getmembers(m, inspect.isfunction)

    for funcTuple in functions:
        funcName = funcTuple[0]
        funcObj = funcTuple[1]
        setattr(TmpCls, funcName, staticmethod(funcObj))


# Set up a dict to be used in the main plugin file
cmdDict = {}

current_file_path = os.path.dirname(__file__)
default_command_path = os.path.join(current_file_path, "menuCommands")

# Load all menu files as dict and append to cmdDict
commandFiles = glob.glob("{}/*.json".format(default_command_path))
for f in commandFiles:
    with open(f, "r") as cmdFile:
        # dict_tmp = json.load(cmdFile)
        # cmdDict = {**cmdDict, **dict_tmp}
        cmdDict |= json.load(cmdFile)

# Sort by label string length
cmdOrderedDict = OrderedDict(
    sorted(cmdDict.items(), key=lambda x: len(getitem(x[1], 'label'))))

# Convert back to normal dict
cmdDict = dict(cmdOrderedDict)
