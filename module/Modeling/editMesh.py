import maya.cmds as cmds
import maya.mel as mel


# class name must be 'Commands'
class Commands(object):

    commandDict = {}

    def _mergeComponents(self):
        mel.eval("performPolyMerge 0")
    commandDict['mergeComponents'] = 'polyMerge.png'

    def _mergeComponentsOptions(self):
        cmds.PolyMergeOptions()
    commandDict['mergeComponentsOptions'] = 'polyMerge.png'

    def _detachEdgeComponent(self):
        cmds.DetachEdgeComponent()
    commandDict['detachEdgeComponent'] = 'polyEditEdgeFlow.png'

    def _polyBevel(self):
        cmds.polyBevel()
    commandDict['polyBevel'] = 'polyBevel.png'
