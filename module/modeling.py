import maya.cmds as cmds
import maya.mel as mel


# class name must be 'Commands'
class Commands(object):

    # Name of dictionary must be this module name + 'Dict'
    modelingDict = {}

    def __init__(self):
        pass

    # ############
    # Select Menu
    # ############
    def _polygonSelectionConstraints(self):
        cmds.PolygonSelectionConstraints()
    modelingDict['polygonSelectionConstraints'] = "polySelectUsingConstraints.png"

    # ############
    # Mesh menu
    # ############
    def _polyBooleanUnion(self):
        cmds.PolygonBooleanUnion()
    modelingDict['polyBooleanUnion'] = 'polyBooleansUnion.png'

    def _polyBooleanUnionOptions(self):
        cmds.PolygonBooleanUnionOptions()
    modelingDict['polyBooleanUnionOptions'] = 'polyBooleansUnion.png'

    def _polyBooleanDifference(self):
        cmds.PolygonBooleanDifference()
    modelingDict['polyBooleanDifference'] = 'polyBooleansDifference.png'

    def _polyBooleanDifferenceOptions(self):
        cmds.PolygonBooleanDifferenceOptions()
    modelingDict['polyBooleanDifferenceOptions'] = 'polyBooleansDifference.png'

    def _polyBooleanIntersection(self):
        cmds.PolygonBooleanIntersection()
    modelingDict['polyBooleanIntersection'] = 'polyBooleansIntersection.png'

    def _polyBooleanIntersectionOptions(self):
        cmds.PolygonBooleanIntersectionOptions()
    modelingDict['polyBooleanIntersectionOptions'] = 'polyBooleansIntersection.png'

    def _combinePolygons(self):
        cmds.CombinePolygons()
    modelingDict['combinePolygons'] = 'polyUnite.png'

    def _combinePolygonsOptions(self):
        cmds.CombinePolygonsOptions()
    modelingDict['combinePolygonsOptions'] = 'polyUnite.png'

    def _extractFace(self):
        cmds.ExtractFace()
    modelingDict['extractFace'] = 'polyChipOff.png'

    def _extractFaceOptions(self):
        cmds.ExtractFaceOptions()
    modelingDict['extractFaceOptions'] = 'polyChipOff.png'

    def _separatePolygons(self):
        cmds.SeparatePolygon()
    modelingDict['separatePolygons'] = 'polySeparate.png'

    def _averageVertex(self):
        cmds.AverageVertex()
    modelingDict['averageVertex'] = 'polyAverageVertex.png'

    def _averageVertexOptions(self):
        mel.eval("performPolyAverageVertex 1")
    modelingDict['averageVertexOptions'] = 'polyAverageVertex.png'

    def _fillHole(self):
        cmds.FillHole()
    modelingDict['fillHole'] = 'polyCloseBorder.png'

    def _quadrangulateOptions(self):
        cmds.QuadrangulateOptions()
    modelingDict['quadrangulateOptions'] = "polyQuad.png"

    def _smoothPolygonOptions(self):
        cmds.SmoothPolygonOptions()
    modelingDict['smoothPolygonOptions'] = "polySphere.png"

    def _triangulate(self):
        cmds.Triangulate()
    modelingDict['triangulate'] = "polyTriangulate.png"

    def _mirrorCutPolygonGeometry(self):
        cmds.MirrorCutPolygonGeometry()
    modelingDict['mirrorCutPolygonGeometry'] = "polyMirrorCut.png"

    def _mirrorCutPolygonGeometryOptions(self):
        cmds.MirrorCutPolygonGeometryOptions()
    modelingDict['mirrorCutPolygonGeometryOptions'] = "polyMirrorCut.png"

    def _mirrorPolygonGeometry(self):
        cmds.MirrorPolygonGeometry()
    modelingDict['mirrorPolygonGeometry'] = "polyMirrorGeometry.png"

    def _mirrorPolygonGeometryOptions(self):
        cmds.MirrorPolygonGeometryOptions()
    modelingDict['mirrorPolygonGeometryOptions'] = "polyMirrorGeometry.png"

    def _transferAttributesOptions(self):
        cmds.TransferAttributeValuesOptions()
    modelingDict['transferAttributesOptions'] = "polyTransferAttributes.png"

    def _cleanupPolygon(self):
        cmds.CleanupPolygon()
    modelingDict['cleanupPolygon'] = "polyCleanup.png"

    def _cleanupPolygonOptions(self):
        cmds.CleanupPolygonOptions()
    modelingDict['cleanupPolygonOptions'] = "polyCleanup.png"

    def _reducePolygon(self):
        cmds.ReducePolygon()
    modelingDict['reducePolygon'] = "polyReduce.png"

    def _reducePolygonOptions(self):
        cmds.ReducePolygonOptions()
    modelingDict['reducePolygonOptions'] = "polyReduce.png"

    # ############
    # Mesh Tool Menu
    # ############
    def _mergeComponents(self):
        mel.eval("performPolyMerge 0")
    modelingDict['mergeComponents'] = 'polyMerge.png'

    def _mergeComponentsOptions(self):
        cmds.PolyMergeOptions()
    modelingDict['mergeComponentsOptions'] = 'polyMerge.png'

    def _detachEdgeComponent(self):
        cmds.DetachEdgeComponent()
    modelingDict['detachEdgeComponent'] = 'polyEditEdgeFlow.png'

    def _polyBevel(self):
        cmds.polyBevel()
    modelingDict['polyBevel'] = 'polyBevel.png'

    # ############
    # Normal Menu
    # ############
    def _setNormalAngle(self):
        cmds.SetNormalAngle()
    modelingDict['setNormalAngle'] = "polyNormalSetAngle.png"

