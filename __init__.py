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


def getClassList():
    """

    Args:
        param (logger): logger

    Return:
        list: list of classes

    """

    moduleDirName = "rush"
    mayaScriptDir = cmds.internalVar(userScriptDir=True)

    moduleRoot = os.path.join(mayaScriptDir, moduleDirName)
    logger.debug("Module path: %s " % moduleRoot)

    moduleList = []
    for root, dirs, files in os.walk(moduleRoot):
        for f in files:
            fullPath = os.path.join(root, f)
            if (fullPath.endswith(".py") and not
                    fullPath.endswith("__init__.py") and not
                    fullPath.endswith("rush.py")):
                moduleList.append(fullPath)

    moduleObjectList = []

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
cl = tuple(getClassList())
RushCommands = type('RushCommands', cl, dict(RushCommands.__dict__))
