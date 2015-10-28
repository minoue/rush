import maya.cmds as cmds


# class name must be 'Commands'
class Commands(object):

    # Name of dictionary must be this module name + 'Dict'
    createUVsDict = {}

    def __init__(self):
        pass

    def _UVSetEditor(self):
        cmds.UVSetEditor()
    createUVsDict['UVSetEditor'] = "sphere.png"

    def _SetCurrentUVSet(self):
        cmds.SetCurrentUVSet()
    createUVsDict['SetCurrentUVSet'] = "sphere.png"
