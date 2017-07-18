import maya.cmds as cmds


# class name must be 'Commands'
class Commands(object):

    commandDict = {}

    def _selectShortestEdgePath(self):
        cmds.SelectShortestEdgePathTool()
    commandDict['selectShortestEdgePath'] = 'selectEdgePath.png'
