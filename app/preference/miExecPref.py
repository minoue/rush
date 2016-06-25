import os
import json
import maya.cmds as cmds

SCRIPT_PATH = os.path.dirname(__file__)
MAYA_SCRIPT_DIR = cmds.internalVar(userScriptDir=True)


def getPreference():
    """ Load pref json data nad return as dict"""

    scripts = os.listdir(MAYA_SCRIPT_DIR)
    if 'miExecPref.json' in scripts:
        path = os.path.join(MAYA_SCRIPT_DIR, 'miExecPref.json')
        prefFile = open(path, 'r')
    else:
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
