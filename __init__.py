import os
import json
import glob
import inspect

from pathlib import Path
from operator import getitem
from collections import OrderedDict
from importlib.util import module_from_spec
from importlib.util import spec_from_file_location

from maya import cmds


class Commands(object):
    commandDict = {}


def __loadModules(*args) -> list:
    """Return a list of module objects

    Returns:
        list: module objects

    """
    scriptDir = cmds.internalVar(userScriptDir=True)
    pluginPath = os.path.join(scriptDir, "rush", "module")

    modules = []

    for root, dirs, files in os.walk(pluginPath):
        for name in files:
            if name.endswith(".py"):
                modulePath = os.path.join(root, name)
                baseName = Path(modulePath).stem
                spec = spec_from_file_location(baseName, modulePath)
                module = module_from_spec(spec)
                spec.loader.exec_module(module)
                modules.append(module)
    return modules


def __initCommands(*args) -> None:
    """
    """

    modules = __loadModules()
    for m in modules:
        # Update cmd dict for all commands from all modules
        for cmd in m.commandDict:
            label = cmd[:1].capitalize() + cmd[1:]
            id = label + "_exmod"
            runTimeCommandName = "rush_{}".format(id)

            command_data = {}
            command_data[id] = {
                'label': label,
                'icon': m.commandDict[cmd],
                'path': "",
                'command': runTimeCommandName,
                'module': m.__name__,
                'sourceType': "mel",
                'sourceCommand': cmd}
            Commands.commandDict.update(command_data)

        # set all functions from each module to the tmp class
        functions = inspect.getmembers(m, inspect.isfunction)
        for func_name, func_obj in functions:
            setattr(Commands, func_name, staticmethod(func_obj))


def __initMenuCommandds(*args):
    """

    Returns:
        dict: Menu commands from files

    """

    cmdDict = {}

    current_file_path = os.path.dirname(__file__)
    default_command_path = os.path.join(
        current_file_path, "menuCommands")

    if not os.path.exists(default_command_path):
        print("not found")
        return

    # Load all menu files as dict and append to cmdDict
    commandFiles = glob.glob("{}/*.json".format(default_command_path))
    for f in commandFiles:
        with open(f, "r") as cmdFile:
            tmpDict = json.load(cmdFile)
            cmdDict = {**cmdDict, **tmpDict}
            # cmdDict |= json.load(cmdFile)

    # Sort by label string length
    cmdOrderedDict = OrderedDict(
        sorted(cmdDict.items(), key=lambda x: len(getitem(x[1], 'label'))))

    # Convert back to normal dict
    cmdDict = dict(cmdOrderedDict)

    return cmdDict


def init():
    """ Initialize commands class
    """

    print('init commands')

    # Cleanup commands
    allCommands = cmds.runTimeCommand(q=True, userCommandArray=True)
    if allCommands is not None:
        for c in allCommands:
            if c.startswith("rush_"):
                cmds.runTimeCommand(c, e=True, delete=True)

    __initCommands()

    # Register runtTimeCommands
    for cmdID in Commands.commandDict:

        cmd = Commands.commandDict[cmdID]['sourceCommand']
        cmd_str = "from rush import Commands; Commands.{}()".format(cmd)
        label = Commands.commandDict[cmdID]['label']
        runtimeCommandName = Commands.commandDict[cmdID]['command']

        cmds.runTimeCommand(
            runtimeCommandName,
            label=label,
            annotation="Rush custom command",
            commandLanguage="python",
            command=cmd_str,
            keywords="rush")

    menuCommands = __initMenuCommandds()
    Commands.commandDict = {**Commands.commandDict, **menuCommands}


if __name__ == "__main__":
    init()
