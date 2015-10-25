import maya.cmds as cmds
import maya.mel as mel


# class name must be 'Commands'
class Commands(object):

    # Name of dictionary must be this module name + 'Dict'
    meshDict = {}

    def __init__(self):
        pass

    # ############
    # Mesh menu
    # ############
    def _polyBooleanUnion(self):
        cmds.PolygonBooleanUnion()
    meshDict['polyBooleanUnion'] = 'polyBooleansUnion.png'

    def _polyBooleanUnionOptions(self):
        cmds.PolygonBooleanUnionOptions()
    meshDict['polyBooleanUnionOptions'] = 'polyBooleansUnion.png'

    def _polyBooleanDifference(self):
        cmds.PolygonBooleanDifference()
    meshDict['polyBooleanDifference'] = 'polyBooleansDifference.png'

    def _polyBooleanDifferenceOptions(self):
        cmds.PolygonBooleanDifferenceOptions()
    meshDict['polyBooleanDifferenceOptions'] = 'polyBooleansDifference.png'

    def _polyBooleanIntersection(self):
        cmds.PolygonBooleanIntersection()
    meshDict['polyBooleanIntersection'] = 'polyBooleansIntersection.png'

    def _polyBooleanIntersectionOptions(self):
        cmds.PolygonBooleanIntersectionOptions()
    meshDict['polyBooleanIntersectionOptions'] = 'polyBooleansIntersection.png'

    def _combinePolygons(self):
        cmds.CombinePolygons()
    meshDict['combinePolygons'] = 'polyUnite.png'

    def _combinePolygonsOptions(self):
        cmds.CombinePolygonsOptions()
    meshDict['combinePolygonsOptions'] = 'polyUnite.png'

    def _extractFace(self):
        cmds.ExtractFace()
    meshDict['extractFace'] = 'polyChipOff.png'

    def _extractFaceOptions(self):
        cmds.ExtractFaceOptions()
    meshDict['extractFaceOptions'] = 'polyChipOff.png'

    def _separatePolygons(self):
        cmds.SeparatePolygon()
    meshDict['separatePolygons'] = 'polySeparate.png'

    def _averageVertex(self):
        cmds.AverageVertex()
    meshDict['averageVertex'] = 'polyAverageVertex.png'

    def _averageVertexOptions(self):
        mel.eval("performPolyAverageVertex 1")
    meshDict['averageVertexOptions'] = 'polyAverageVertex.png'

    def _fillHole(self):
        cmds.FillHole()
    meshDict['fillHole'] = 'polyCloseBorder.png'

    def _quadrangulateOptions(self):
        cmds.QuadrangulateOptions()
    meshDict['quadrangulateOptions'] = "polyQuad.png"

    def _smoothPolygonOptions(self):
        cmds.SmoothPolygonOptions()
    meshDict['smoothPolygonOptions'] = "polySphere.png"

    def _triangulate(self):
        cmds.Triangulate()
    meshDict['triangulate'] = "polyTriangulate.png"

    def _mirrorCutPolygonGeometry(self):
        cmds.MirrorCutPolygonGeometry()
    meshDict['mirrorCutPolygonGeometry'] = "polyMirrorCut.png"

    def _mirrorCutPolygonGeometryOptions(self):
        cmds.MirrorCutPolygonGeometryOptions()
    meshDict['mirrorCutPolygonGeometryOptions'] = "polyMirrorCut.png"

    def _mirrorPolygonGeometry(self):
        cmds.MirrorPolygonGeometry()
    meshDict['mirrorPolygonGeometry'] = "polyMirrorGeometry.png"

    def _mirrorPolygonGeometryOptions(self):
        cmds.MirrorPolygonGeometryOptions()
    meshDict['mirrorPolygonGeometryOptions'] = "polyMirrorGeometry.png"

    def _transferAttributesOptions(self):
        cmds.TransferAttributeValuesOptions()
    meshDict['transferAttributesOptions'] = "polyTransferAttributes.png"

    def _cleanupPolygon(self):
        cmds.CleanupPolygon()
    meshDict['cleanupPolygon'] = "polyCleanup.png"

    def _cleanupPolygonOptions(self):
        cmds.CleanupPolygonOptions()
    meshDict['cleanupPolygonOptions'] = "polyCleanup.png"

    def _reducePolygon(self):
        cmds.ReducePolygon()
    meshDict['reducePolygon'] = "polyReduce.png"

    def _reducePolygonOptions(self):
        cmds.ReducePolygonOptions()
    meshDict['reducePolygonOptions'] = "polyReduce.png"
