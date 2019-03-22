import maya.cmds as cmds
import maya.mel as mel


# class name must be 'Commands'
class Commands(object):

    commandDict = {}

    # Components -------------------------------

    def _PolyBevel(self):
        cmds.polyBevel()
    commandDict['PolyBevel'] = 'polyBevel.png'

    def _PolyBridge(self):
        mel.eval("performPolyBridgeEdge 0")
    commandDict['PolyBridge'] = 'polyBridge.png'

    def _PolyCircularize(self):
        cmds.PolyCircularize()
    commandDict['PolyCircularize'] = 'polyCircularize.png'

    def _PolyCollapse(self):
        cmds.PolygonCollapse()
    commandDict['PolyCollapse'] = 'polyCollapseEdge.png'

    def _PolyConnectComponents(self):
        cmds.polyConnectComponents()
    commandDict['PolyConnectComponents'] = 'polyConnectComponents.png'

    def _DetachComponent(self):
        cmds.DetachComponent()
    commandDict['DetachComponent'] = 'polySplitVertex.png'

    def _PolyExtrude(self):
        cmds.PolyExtrude()
    commandDict['PolyExtrude'] = 'polyExtrudeFacet.png'

    def _MergeComponents(self):
        cmds.PolyMerge()
    commandDict['MergeComponents'] = 'polyMerge.png'

    def _MergeComponentsOptions(self):
        cmds.PolyMergeOptions()
    commandDict['MergeComponentsOptions'] = 'polyMerge.png'

    def _MergeToCenter(self):
        cmds.MergeToCenter()
    commandDict['MergeToCenter'] = 'polyMergeToCenter.png'

    def _TransformComponents(self):
        cmds.MovePolygonComponent()
    commandDict['TransformComponents'] = 'polyMoveVertex.png'

    def _TransformComponentsOptions(self):
        cmds.MovePolygonComponentOptions()
    commandDict['TransformComponentsOptions'] = 'polyMoveVertex.png'

    def _PolyFlip(self):
        mel.eval("dR_performSymmetryFlip")
    commandDict['PolyFlip'] = 'polyFlip.png'

    def _PolySymmetrize(self):
        mel.eval("dR_performSymmetrize")
    commandDict['PolySymmetrize'] = 'symmetrize.png'

    # Vertex -------------------------------

    def _AverageVertex(self):
        cmds.AverageVertex()
    commandDict['AverageVertex'] = 'polyAverageVertex.png'

    def _AverageVertexOptions(self):
        mel.eval("performPolyAverageVertex 1")
    commandDict['AverageVertexOptions'] = 'polyAverageVertex.png'

    def _ChamferVertex(self):
        cmds.ChamferVertex()
    commandDict['ChamferVertex'] = 'polyChamfer.png'

    def _ChamferVertexOptions(self):
        cmds.ChamferVertexOptions()
    commandDict['ChamferVertexOptions'] = 'polyChamfer.png'

    # Edge -------------------------------

    def _DetachEdgeComponent(self):
        cmds.DetachEdgeComponent()
    commandDict['DetachEdgeComponent'] = 'polyEditEdgeFlow.png'

    # Face -------------------------------

    def _ExtractFace(self):
        cmds.ExtractFace()
    commandDict['ExtractFace'] = 'polyChipOff.png'

    def _ExtractFaceOptions(self):
        cmds.ExtractFaceOptions()
    commandDict['ExtractFaceOptions'] = 'polyChipOff.png'
