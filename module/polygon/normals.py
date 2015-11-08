import maya.cmds as cmds


# class name must be 'Commands'
class Commands(object):

    commandDict = {}

    def _setNormalAngle(self):
        cmds.SetNormalAngle()
    commandDict['setNormalAngle'] = "polyNormalSetAngle.png"
