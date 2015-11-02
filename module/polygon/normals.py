import maya.cmds as cmds


# class name must be 'Commands'
class Commands(object):

    # Name of dictionary must be this module name + 'Dict'
    commandDict = {}

    def __init__(self):
        pass

    # ############
    # Normal Menu
    # ############
    def _setNormalAngle(self):
        cmds.SetNormalAngle()
    commandDict['setNormalAngle'] = "polyNormalSetAngle.png"
