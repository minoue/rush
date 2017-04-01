from maya import cmds
import json
import imp
import os


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

    moduleList = []
    for root, dirs, files in os.walk(moduleRoot):
        for f in files:
            fullPath = os.path.join(root, f)
            if (fullPath.endswith(".py") and not
                    fullPath.endswith("__init__.py")):
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
        except ImportError:
            pass

    commandClassList = [i.Commands for i in moduleObjectList]

    cmdsDict = {}
    for c in commandClassList:
        cmdsDict.update(c.commandDict)

    saveCommands(cmdsDict)

    return commandClassList


def saveCommands(cmdsDict):
    """ Save all commands as a json file in the maya user directory
    
    Args:
        cmdsDict (dict): All commands
    
    Return:
        None
    
    """
    outPath = os.path.normpath(os.path.join(mayaScriptDir, "rushCmds.json"))

    with open(outPath, 'w') as outFile:
        json.dump(
            cmdsDict,
            outFile,
            indent=4,
            separators=(',', ':'),
            sort_keys=True)


class RushCommands():
    pass


# Re-difine RushCommands class to inherit all comamnd classes for the list
cl = tuple(getClassList())
RushCommands = type('RushCommands', cl, dict(RushCommands.__dict__))
