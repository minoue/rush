import os
import json


SCRIPT_PATH = os.path.dirname(__file__)


def getPreference():
    """ Load pref json data nad return as dict"""

    prefFile = open(os.path.join(SCRIPT_PATH, "pref.json"), 'r')
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
