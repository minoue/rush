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


def loadRushCohfig():
    """

    Return:
        config(list): List of path module paths

    """
    userDir = os.path.expanduser("~")
    configPath = os.path.join(userDir, ".rushConfig")

    defaultModulePath = os.path.join(
        cmds.internalVar(userScriptDir=True), 'rush')

    if os.path.exists(configPath):
        try:
            with open(configPath, 'r') as inFile:
                config = inFile.read().split()
        except IOError:
            config = [defaultModulePath]
            logger.debug("Failed to load config file")
    else:
        logger.debug("Config file doesn't exist. Creating a new config file")

        # Init config file
        try:
            with open(configPath, 'w') as outFile:
                outFile.writelines([defaultModulePath])
            logger.debug("Created new config file")
        except IOError:
            logger.debug("Failed to save config file")
        finally:
            config = [defaultModulePath]

    return config


def getModulePath(path):
    """

    Args:
        path (str): directory path to search modules

    Return:
        moduleList (list): List of module paths
        None: if the path doesn't exist

    """
    if not os.path.exists(path):
        return None

    moduleList = []
    for root, dirs, files in os.walk(path):
        for f in files:
            fullPath = os.path.join(root, f)
            if (fullPath.endswith(".py") and not
                    fullPath.endswith("__init__.py") and not
                    fullPath.endswith("rush.py")):
                moduleList.append(fullPath)

    return moduleList


def getClassList(config):
    """

    Args:
        config (list): List of paths

    Return:
        list: list of classes

    """

    mayaScriptDir = cmds.internalVar(userScriptDir=True)

    # logger.debug("Module path: %s " % moduleRoot)

    moduleList = []
    moduleObjectList = []

    for path in config:
        pathList = getModulePath(path)
        if pathList is not None:
            moduleList.extend(pathList)

    for path in moduleList:
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
            moduleObjectList.append(mod)
        except:
            logger.debug("Failed to load module : %s" % path)

    commandClassList = [i.Commands for i in moduleObjectList]
    logger.debug("All command classes: %s" % str(commandClassList))

    cmdsDict = {}
    for c in commandClassList:
        cmdsDict.update(c.commandDict)

    outPath = os.path.normpath(os.path.join(mayaScriptDir, "rushCmds.json"))
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
config = loadRushCohfig()
cl = tuple(getClassList(config))
RushCommands = type('RushCommands', cl, dict(RushCommands.__dict__))
