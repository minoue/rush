import maya.cmds as cmds
import maya.mel as mel


# class name must be 'Commands'
class Commands(object):

    # Name of dictionary must be this module name + 'Dict'
    normalsDict = {}

    def __init__(self):
        pass

    # ############
    # Normal Menu
    # ############
    def _setNormalAngle(self):
        cmds.SetNormalAngle()
    normalsDict['setNormalAngle'] = "polyNormalSetAngle.png"
