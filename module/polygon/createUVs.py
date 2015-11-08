import maya.cmds as cmds


# class name must be 'Commands'
class Commands(object):

    commandDict = {}

    def _UVSetEditor(self):
        cmds.UVSetEditor()
    commandDict['UVSetEditor'] = "sphere.png"

    def _SetCurrentUVSet(self):
        cmds.SetCurrentUVSet()
    commandDict['SetCurrentUVSet'] = "sphere.png"
