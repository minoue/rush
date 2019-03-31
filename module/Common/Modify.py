from maya import cmds
from maya import mel


commandDict = {}


def freezeAll():
    cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False)


def freezeOnlyTranslation():
    cmds.makeIdentity(apply=True, t=True, r=False, s=False, n=False)


def freezeOnlyRotation():
    cmds.makeIdentity(apply=True, t=False, r=True, s=False, n=False)


# Snap align
def snapPointToPoint():
    cmds.SnapPointToPoint()


def snap2PointsTo2Points():
    cmds.Snap2PointsTo2Points()


def snap3PointsTo3Points():
    cmds.Snap3PointsTo3Points(0)


def performAlignObjects():
    cmds.perform
    mel.eval("performAlignObjects 0")


def positionAlongCurve():
    cmds.PositionAlongCurve()


def alignTool():
    mel.eval("setToolTo alignToolCtx")


def snapTogetherTool():
    cmds.setToolTo(cmds.snapTogetherCtx())


def centerPivot():
    cmds.CenterPivot()


def prefixHierarchyNames():
    cmds.PrefixHierarchyNames()


def searchReplaceNames():
    mel.eval("performSearchReplaceNames 1")


def addAttribute():
    cmds.AddAttribute()


def editAttribute():
    cmds.RenameAttribute()


def deleteAttribute():
    cmds.DeleteAttribute()


def scriptPaintTool():
    cmds.ScriptPaintTool()


def freezeOnlyScale():
    cmds.makeIdentity(apply=True, t=False, r=False, s=True, n=False)


# Conversions
def convertNurbsToPolygonOptions():
    cmds.NURBSToPolygonsOptions()


def convertNurbsToSubdivOptions():
    cmds.CreateSubdivSurfaceOptions()


def convertPolygonToSubdivOptions():
    cmds.CreateSubdivSurfaceOptions()


def convertPolygonEdgesToCurveOptions():
    cmds.CreateCurveFromPolyOptions()


def convertSubdivToPolygonsOptions():
    cmds.TesselateSubdivSurfaceOptions()


def convertSubdivToNURBSOptions():
    cmds.SubdivToNURBSOptions()


def paintEffectsToPolygonsOptions():
    cmds.PaintEffectsToPolyOptions()


def paintEffectsToNURBSOptions():
    cmds.PaintEffectsToNurbsOptions()


def paintEffectsToCurveOptions():
    cmds.PaintEffectsToCurveOptions()


def textureToGeometryOptions():
    mel.eval("""performTextureToGeom 1""")


commandDict['freezeAll'] = "menuIconModify.png"
commandDict['freezeOnlyTranslation'] = "menuIconModify.png"
commandDict['freezeOnlyRotation'] = "menuIconModify.png"
commandDict['snapPointToPoint'] = "pointToPoint.png"
commandDict['snap2PointsTo2Points'] = "twoPointToPoint.png"
commandDict['snap3PointsTo3Points'] = "threePointToPoint.png"
commandDict['performAlignObjects'] = "alignObjects.png"
commandDict['positionAlongCurve'] = "positionAlongCurve.png"
commandDict['alignTool'] = "alignTool.png"
commandDict['snapTogetherTool'] = "snapTogetherTool.png"
commandDict['centerPivot'] = "menuIconModify.png"
commandDict['prefixHierarchyNames'] = "menuIconModify.png"
commandDict['searchReplaceNames'] = "menuIconModify.png"
commandDict['addAttribute'] = "menuIconModify.png"
commandDict['editAttribute'] = "menuIconModify.png"
commandDict['deleteAttribute'] = "menuIconModify.png"
commandDict['scriptPaintTool'] = "userPaint.png"
commandDict['freezeOnlyScale'] = "menuIconModify.png"
commandDict['convertNurbsToPolygonOptions'] = "nurbsToPolygons.png"
commandDict['convertNurbsToSubdivOptions'] = "nurbsToSubdivs.png"
commandDict['convertPolygonToSubdivOptions'] = "subdivCreate.png"
commandDict['convertPolygonEdgesToCurveOptions'] = "menuIconModify.png"
commandDict['convertSubdivToPolygonsOptions'] = "subdivTessellate.png"
commandDict['convertSubdivToNURBSOptions'] = "subdivToNurbs.png"
commandDict['paintEffectsToPolygonsOptions'] = "paintFXtoPoly.png"
commandDict['paintEffectsToNURBSOptions'] = "paintFXtoNurbs.png"
commandDict['paintEffectsToCurveOptions'] = "paintFXtoCurve.png"
commandDict['textureToGeometryOptions'] = "textureToGeom.png"
