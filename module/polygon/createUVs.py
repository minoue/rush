import maya.cmds as cmds


# class name must be 'Commands'
class Commands(object):

    # Name of dictionary must be this module name + 'Dict'
    commandDict = {}

    def __init__(self):
        pass

    def _UVSetEditor(self):
        cmds.UVSetEditor()
    commandDict['UVSetEditor'] = "sphere.png"

    def _SetCurrentUVSet(self):
        cmds.SetCurrentUVSet()
    commandDict['SetCurrentUVSet'] = "sphere.png"
