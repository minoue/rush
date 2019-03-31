import maya.cmds as cmds


commandDict = {}


def setNormalAngle():
    cmds.SetNormalAngle()


commandDict['setNormalAngle'] = "polyNormalSetAngle.png"
