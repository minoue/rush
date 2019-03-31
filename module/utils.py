from __future__ import print_function
from maya import cmds


commandDict = {}


def reloadRush():
    try:
        cmds.unloadPlugin("Rush.py")
        cmds.loadPlugin("Rush.py")
    except Exception:
        print("Failed to reload plugin")


commandDict['reloadRush'] = "sphere.png"
