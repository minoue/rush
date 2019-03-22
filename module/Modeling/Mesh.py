import maya.cmds as cmds
import maya.mel as mel


# class name must be 'Commands'
class Commands(object):

    commandDict = {}

    # Boolean -------------------------------

    def _polyBooleanUnion(self):
        cmds.PolygonBooleanUnion()
    commandDict['polyBooleanUnion'] = 'polyBooleansUnion.png'

    def _polyBooleanUnionOptions(self):
        cmds.PolygonBooleanUnionOptions()
    commandDict['polyBooleanUnionOptions'] = 'polyBooleansUnion.png'

    def _polyBooleanDifference(self):
        cmds.PolygonBooleanDifference()
    commandDict['polyBooleanDifference'] = 'polyBooleansDifference.png'

    def _polyBooleanDifferenceOptions(self):
        cmds.PolygonBooleanDifferenceOptions()
    commandDict['polyBooleanDifferenceOptions'] = 'polyBooleansDifference.png'

    def _polyBooleanIntersection(self):
        cmds.PolygonBooleanIntersection()
    commandDict['polyBooleanIntersection'] = 'polyBooleansIntersection.png'

    def _polyBooleanIntersectionOptions(self):
        cmds.PolygonBooleanIntersectionOptions()
    commandDict['polyBooleanIntersectionOptions'] = 'polyBooleansIntersection.png'

    # Combine -------------------------------

    def _combinePolygons(self):
        cmds.CombinePolygons()
    commandDict['combinePolygons'] = 'polyUnite.png'

    def _combinePolygonsOptions(self):
        cmds.CombinePolygonsOptions()
    commandDict['combinePolygonsOptions'] = 'polyUnite.png'

    def _separatePolygons(self):
        cmds.SeparatePolygon()
    commandDict['separatePolygons'] = 'polySeparate.png'

    # Remesh -------------------------------

    def _conformPolygon(self):
        cmds.ConformPolygon()
    commandDict['conformPolygon'] = 'menuIconPolygoons.png'

    def _conformPolygonOptions(self):
        cmds.ConformPolygonOptions()
    commandDict['conformPolygonOptions'] = 'menuIconPolygoons.png'

    def _fillHole(self):
        cmds.FillHole()
    commandDict['fillHole'] = 'polyCloseBorder.png'

    def _reducePolygon(self):
        cmds.ReducePolygon()
    commandDict['reducePolygon'] = "polyReduce.png"

    def _reducePolygonOptions(self):
        cmds.ReducePolygonOptions()
    commandDict['reducePolygonOptions'] = "polyReduce.png"

    def _smoothPolygon(self):
        cmds.SmoothPolygon()
    commandDict['smoothPolygon'] = "polySmooth.png"

    def _smoothPolygonOptions(self):
        cmds.SmoothPolygonOptions()
    commandDict['smoothPolygonOptions'] = "polySmooth.png"

    def _triangulate(self):
        cmds.Triangulate()
    commandDict['triangulate'] = "polyTriangulate.png"

    def _quadrangulateOptions(self):
        cmds.QuadrangulateOptions()
    commandDict['quadrangulateOptions'] = "polyQuad.png"

    # Mirror -------------------------------

    def _mirrorPolygonGeometry(self):
        cmds.MirrorPolygonGeometry()
    commandDict['mirrorPolygonGeometry'] = "polyMirrorGeometry.png"

    def _mirrorPolygonGeometryOptions(self):
        cmds.MirrorPolygonGeometryOptions()
    commandDict['mirrorPolygonGeometryOptions'] = "polyMirrorGeometry.png"

    def _mirrorCutPolygonGeometry(self):
        cmds.MirrorCutPolygonGeometry()
    commandDict['mirrorCutPolygonGeometry'] = "polyMirrorCut.png"

    def _mirrorCutPolygonGeometryOptions(self):
        cmds.MirrorCutPolygonGeometryOptions()
    commandDict['mirrorCutPolygonGeometryOptions'] = "polyMirrorCut.png"

    # Transfer -------------------------------

    def _transferAttributesOptions(self):
        mel.eval("performTransferAttributes 1")
    commandDict['transferAttributesOptions'] = "polyTransferAttributes.png"

    # Optimize -------------------------------

    def _cleanupPolygon(self):
        cmds.CleanupPolygon()
    commandDict['cleanupPolygon'] = "polyCleanup.png"

    def _cleanupPolygonOptions(self):
        cmds.CleanupPolygonOptions()
    commandDict['cleanupPolygonOptions'] = "polyCleanup.png"
