import os
import json
import maya.cmds as cmds

SCRIPT_PATH = os.path.dirname(__file__)
MAYA_SCRIPT_DIR = cmds.internalVar(userScriptDir=True)


def getPreference():
    """ Load pref json data nad return as dict"""

    for root, dirs, files in os.walk(MAYA_SCRIPT_DIR):
        if 'miExecPref.json' in files:
            # Load pref json file from user script dir if exists.
            abspath = os.path.join(root, 'miExecPref.json')
            prefFile = open(abspath, 'r')
        else:
            # Load pref json file from miExec package directory.
            prefFile = open(os.path.join(SCRIPT_PATH, "miExecPref.json"), 'r')

    prefDict = json.load(prefFile)
    prefFile.close()

    return prefDict


def getWindowSetting():
    """ Load window setting json data and return as dict"""

    prefDict = getPreference()
    pardir = os.path.join(SCRIPT_PATH, os.pardir)

    windowFilePath = os.path.join(
        pardir,
        "style",
        prefDict['style'],
        "window.json")

    windowFile = open(windowFilePath, 'r')
    windowDict = json.load(windowFile)
    windowFile.close()

    return windowDict
