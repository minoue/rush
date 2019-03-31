from maya import cmds
from maya import mel


commandDict = {}

# Booleans


def polyBooleanUnion():
    cmds.PolygonBooleanUnion()


def polyBooleanUnionOptions():
    cmds.PolygonBooleanUnionOptions()


def polyBooleanDifference():
    cmds.PolygonBooleanDifference()


def polyBooleanDifferenceOptions():
    cmds.PolygonBooleanDifferenceOptions()


def polyBooleanIntersection():
    cmds.PolygonBooleanIntersection()


def polyBooleanIntersectionOptions():
    cmds.PolygonBooleanIntersectionOptions()


# Combine -------------------------------


def combinePolygons():
    cmds.CombinePolygons()


def combinePolygonsOptions():
    cmds.CombinePolygonsOptions()


def separatePolygons():
    cmds.SeparatePolygon()

# Remesh -------------------------------


def conformPolygon():
    cmds.ConformPolygon()


def conformPolygonOptions():
    cmds.ConformPolygonOptions()


def fillHole():
    cmds.FillHole()


def reducePolygon():
    cmds.ReducePolygon()


def reducePolygonOptions():
    cmds.ReducePolygonOptions()


def smoothPolygon():
    cmds.SmoothPolygon()


def smoothPolygonOptions():
    cmds.SmoothPolygonOptions()


def triangulate():
    cmds.Triangulate()


def quadrangulateOptions():
    cmds.QuadrangulateOptions()


# Mirror -------------------------------


def mirrorPolygonGeometry():
    cmds.MirrorPolygonGeometry()


def mirrorPolygonGeometryOptions():
    cmds.MirrorPolygonGeometryOptions()


def mirrorCutPolygonGeometry():
    cmds.MirrorCutPolygonGeometry()


def mirrorCutPolygonGeometryOptions():
    cmds.MirrorCutPolygonGeometryOptions()


# Transfer -------------------------------


def transferAttributesOptions():
    mel.eval("performTransferAttributes 1")


# Optimize -------------------------------


def cleanupPolygon():
    cmds.CleanupPolygon()


def cleanupPolygonOptions():
    cmds.CleanupPolygonOptions()


commandDict['polyBooleanUnion'] = 'polyBooleansUnion.png'
commandDict['polyBooleanUnionOptions'] = 'polyBooleansUnion.png'
commandDict['polyBooleanDifference'] = 'polyBooleansDifference.png'
commandDict['polyBooleanDifferenceOptions'] = 'polyBooleansDifference.png'
commandDict['polyBooleanIntersection'] = 'polyBooleansIntersection.png'
commandDict['polyBooleanIntersectionOptions'] = 'polyBooleansIntersection.png'
commandDict['combinePolygons'] = 'polyUnite.png'
commandDict['combinePolygonsOptions'] = 'polyUnite.png'
commandDict['separatePolygons'] = 'polySeparate.png'
commandDict['conformPolygon'] = 'menuIconPolygoons.png'
commandDict['conformPolygonOptions'] = 'menuIconPolygoons.png'
commandDict['fillHole'] = 'polyCloseBorder.png'
commandDict['reducePolygon'] = "polyReduce.png"
commandDict['reducePolygonOptions'] = "polyReduce.png"
commandDict['smoothPolygon'] = "polySmooth.png"
commandDict['smoothPolygonOptions'] = "polySmooth.png"
commandDict['triangulate'] = "polyTriangulate.png"
commandDict['quadrangulateOptions'] = "polyQuad.png"
commandDict['mirrorPolygonGeometry'] = "polyMirrorGeometry.png"
commandDict['mirrorPolygonGeometryOptions'] = "polyMirrorGeometry.png"
commandDict['mirrorCutPolygonGeometry'] = "polyMirrorCut.png"
commandDict['mirrorCutPolygonGeometryOptions'] = "polyMirrorCut.png"
commandDict['transferAttributesOptions'] = "polyTransferAttributes.png"
commandDict['cleanupPolygon'] = "polyCleanup.png"
commandDict['cleanupPolygonOptions'] = "polyCleanup.png"
