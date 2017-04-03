from maya import cmds
import logging
import json
import imp
import os

# level = logging.DEBUG
level = logging.ERROR

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
logger.addHandler(handler)
logger.setLevel(level)
handler.setLevel(level)


def loadConfig():
    """ Load config file

    Return:
        config(list): List of path module paths

    """
    userDir = os.path.expanduser("~")
    configPath = os.path.join(userDir, ".rushConfig")

    defaultModulePath = os.path.join(
        cmds.internalVar(userScriptDir=True), 'rush')

    # Create new config file
    if not os.path.exists(configPath):
        initConfig(configPath, defaultModulePath)
        config = [defaultModulePath]
        return config

    try:
        f = open(configPath, 'r')
        config = f.read().split()
        f.close()
    except IOError:
        config = [defaultModulePath]
        logger.debug("Failed to load config file")

    return config


def initConfig(configPath, defaultModulePath):
    """ Init and save new config file

    Args:
        configPath (str): path to config file
        defaultModulePath (str): default module path

    Return:
        None

    """
    logger.debug("Config file doesn't exist. Creating a new config file")
    # Init config file
    try:
        with open(configPath, 'w') as outFile:
            outFile.writelines([defaultModulePath])
        logger.debug("Created new config file")
    except IOError:
        logger.debug("Failed to save config file")


def getModulePath(path):
    """ Create and return a list of module paths

    Args:
        path (str): directory path to search modules

    Return:
        mods (list): List of module paths
        None: if the path doesn't exist

    """
    if not os.path.exists(path):
        return None

    # Get all files in the directory
    allFiles = [os.path.join(root, f) for root, firs, files in os.walk(path)
                for f in files]

    # Get only python files
    pythonFiles = [i for i in allFiles if i.endswith(".py")]

    # Remove __init__ and main plugin file
    mods = [f for f in pythonFiles
            if not f.endswith("__init__.py") and not f.endswith("rush.py")]

    return mods


def loadModule(path):
    """ Load module

    Args:
        path (str): module path

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

    name = os.path.splitext(path)[0].split("/")
    name = "/".join(name[-2:])

    try:
        mod = imp.load_source(name, path)
        return mod
    except:
        logger.debug("Failed to load module : %s" % path)
        return None


def getClassList(config):
    """ Create and return a list of command classes

    Args:
        config (list): List of paths

    Return:
        commandClassList: list of classes

    """

    # Create a single list of module paths
    moduleList = []
    for path in config:
        logger.debug("Module path: %s " % path)
        pathList = getModulePath(path)
        if pathList is not None:
            moduleList.extend(pathList)

    # Create a list of module objects
    moduleObjectList = []
    for path in moduleList:
        m = loadModule(path)
        if m is not None:
            moduleObjectList.append(m)

    # Class only for the reload command
    class Reload(object):
        commandDict = {}

        def _reloadRush(self):
            try:
                cmds.unloadPlugin("rush.py")
                cmds.loadPlugin("rush.py")
            except:
                print "Failed to reload plugin"
        commandDict['reloadRush'] = "sphere.png"

    # Crate a list of classes
    commandClassList = [i.Commands for i in moduleObjectList]
    commandClassList.append(Reload)
    logger.debug("All command classes: %s" % str(commandClassList))

    # Create and write a list of all commands for the completer in main plugin
    cmdsDict = {}
    for c in commandClassList:
        cmdsDict.update(c.commandDict)
    outPath = os.path.normpath(
        os.path.join(
            cmds.internalVar(userScriptDir=True),
            "rushCmds.json"))
    saveCommands(outPath, cmdsDict)

    return commandClassList


def saveCommands(path, cmdsDict):
    """ Save all commands as a json file in the maya user directory

    Args:
        path (str): output path
        cmdsDict (dict): All commands

    Return:
        None

    """

    logger.debug("Saving command file to %s" % path)

    try:
        with open(path, 'w') as outFile:
            json.dump(
                cmdsDict,
                outFile,
                indent=4,
                separators=(',', ':'),
                sort_keys=True)
    except IOError:
        logger.debug("Failed to save command file")


class RushCommands(object):
    pass


# Re-difine RushCommands class to inherit all comamnd classes for the list
config = loadConfig()
cl = tuple(getClassList(config))
RushCommands = type('RushCommands', cl, dict(RushCommands.__dict__))
