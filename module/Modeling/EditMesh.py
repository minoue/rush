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

    # Vertex -------------------------------

    def _averageVertex(self):
        cmds.AverageVertex()
    commandDict['averageVertex'] = 'polyAverageVertex.png'

    def _averageVertexOptions(self):
        mel.eval("performPolyAverageVertex 1")
    commandDict['averageVertexOptions'] = 'polyAverageVertex.png'

    # Face -------------------------------

    def _extractFace(self):
        cmds.ExtractFace()
    commandDict['extractFace'] = 'polyChipOff.png'

    def _extractFaceOptions(self):
        cmds.ExtractFaceOptions()
    commandDict['extractFaceOptions'] = 'polyChipOff.png'
