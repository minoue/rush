import maya.cmds as cmds
import maya.mel as mel


# class name must be 'Commands'
class Commands(object):

    commandDict = {}

    # Components -------------------------------

    def _polyBevel(self):
        cmds.polyBevel()
    commandDict['polyBevel'] = 'polyBevel.png'

    def _polyBridge(self):
        mel.eval("performPolyBridgeEdge 0")
    commandDict['polyBridge'] = 'polyBridge.png'

    def _polyCircularize(self):
        cmds.PolyCircularize()
    commandDict['polyCircularize'] = 'polyCircularize.png'

    def _polyCollapse(self):
        cmds.PolygonCollapse()
    commandDict['polyCollapse'] = 'polyCollapseEdge.png'

    def _polyConnectComponents(self):
        cmds.polyConnectComponents()
    commandDict['polyConnectComponents'] = 'polyConnectComponents.png'

    def _detachComponent(self):
        cmds.DetachComponent()
    commandDict['detachComponent'] = 'polySplitVertex.png'

    def _polyExtrude(self):
        cmds.PolyExtrude()
    commandDict['polyExtrude'] = 'polyExtrudeFacet.png'

    def _mergeComponents(self):
        cmds.PolyMerge()
    commandDict['mergeComponents'] = 'polyMerge.png'

    def _mergeComponentsOptions(self):
        cmds.PolyMergeOptions()
    commandDict['mergeComponentsOptions'] = 'polyMerge.png'

    def _mergeToCenter(self):
        cmds.MergeToCenter()
    commandDict['mergeToCenter'] = 'polyMergeToCenter.png'

    def _transformComponents(self):
        cmds.MovePolygonComponent()
    commandDict['transformComponents'] = 'polyMoveVertex.png'

    def _transformComponentsOptions(self):
        cmds.MovePolygonComponentOptions()
    commandDict['transformComponentsOptions'] = 'polyMoveVertex.png'

    def _polyFlip(self):
        mel.eval("dR_performSymmetryFlip")
    commandDict['polyFlip'] = 'polyFlip.png'

    def _polySymmetrize(self):
        mel.eval("dR_performSymmetrize")
    commandDict['polySymmetrize'] = 'symmetrize.png'

    # Vertex -------------------------------

    def _averageVertex(self):
        cmds.AverageVertex()
    commandDict['averageVertex'] = 'polyAverageVertex.png'

    def _averageVertexOptions(self):
        mel.eval("performPolyAverageVertex 1")
    commandDict['averageVertexOptions'] = 'polyAverageVertex.png'

    def _chamferVertex(self):
        cmds.ChamferVertex()
    commandDict['chamferVertex'] = 'polyChamfer.png'

    def _chamferVertexOptions(self):
        cmds.ChamferVertexOptions()
    commandDict['chamferVertexOptions'] = 'polyChamfer.png'

    # Edge -------------------------------

    def _detachEdgeComponent(self):
        cmds.DetachEdgeComponent()
    commandDict['detachEdgeComponent'] = 'polyEditEdgeFlow.png'

    # Face -------------------------------

    def _extractFace(self):
        cmds.ExtractFace()
    commandDict['extractFace'] = 'polyChipOff.png'

    def _extractFaceOptions(self):
        cmds.ExtractFaceOptions()
    commandDict['extractFaceOptions'] = 'polyChipOff.png'
