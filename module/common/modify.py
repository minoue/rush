import maya.cmds as cmds
import maya.mel as mel


class Commands(object):

    commandDict = {}

    def _freezeAll(self):
        cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False)
    commandDict['freezeAll'] = "menuIconModify.png"

    def _freezeOnlyTranslation(self):
        cmds.makeIdentity(apply=True, t=True, r=False, s=False, n=False)
    commandDict['freezeOnlyTranslation'] = "menuIconModify.png"

    def _freezeOnlyRotation(self):
        cmds.makeIdentity(apply=True, t=False, r=True, s=False, n=False)
    commandDict['freezeOnlyRotation'] = "menuIconModify.png"

    # Snap align
    def _snapPointToPoint(self):
        cmds.SnapPointToPoint()
    commandDict['snapPointToPoint'] = "pointToPoint.png"

    def _snap2PointsTo2Points(self):
        cmds.Snap2PointsTo2Points()
    commandDict['snap2PointsTo2Points'] = "twoPointToPoint.png"

    def _snap3PointsTo3Points(self):
        cmds.Snap3PointsTo3Points(0)
    commandDict['snap3PointsTo3Points'] = "threePointToPoint.png"

    def _performAlignObjects(self):
        cmds.perform
        mel.eval("performAlignObjects 0")
    commandDict['performAlignObjects'] = "alignObjects.png"

    def _positionAlongCurve(self):
        cmds.PositionAlongCurve()
    commandDict['positionAlongCurve'] = "positionAlongCurve.png"

    def _alignTool(self):
        mel.eval("setToolTo alignToolCtx")
    commandDict['alignTool'] = "alignTool.png"

    def _snapTogetherTool(self):
        cmds.setToolTo(cmds.snapTogetherCtx())
    commandDict['snapTogetherTool'] = "snapTogetherTool.png"

    def _centerPivot(self):
        cmds.CenterPivot()
    commandDict['centerPivot'] = "menuIconModify.png"

    def _prefixHierarchyNames(self):
        cmds.PrefixHierarchyNames()
    commandDict['prefixHierarchyNames'] = "menuIconModify.png"

    def _searchReplaceNames(self):
        mel.eval("performSearchReplaceNames 1")
    commandDict['searchReplaceNames'] = "menuIconModify.png"

    def _addAttribute(self):
        cmds.AddAttribute()
    commandDict['addAttribute'] = "menuIconModify.png"

    def _editAttribute(self):
        cmds.RenameAttribute()
    commandDict['editAttribute'] = "menuIconModify.png"

    def _deleteAttribute(self):
        cmds.DeleteAttribute()
    commandDict['deleteAttribute'] = "menuIconModify.png"

    def _scriptPaintTool(self):
        cmds.ScriptPaintTool()
    commandDict['scriptPaintTool'] = "userPaint.png"

    def _freezeOnlyScale(self):
        cmds.makeIdentity(apply=True, t=False, r=False, s=True, n=False)
    commandDict['freezeOnlyScale'] = "menuIconModify.png"

    # Conversions
    def _convertNurbsToPolygonOptions(self):
        cmds.NURBSToPolygonsOptions()
    commandDict['convertNurbsToPolygonOptions'] = "nurbsToPolygons.png"

    def _convertNurbsToSubdivOptions(self):
        cmds.CreateSubdivSurfaceOptions()
    commandDict['convertNurbsToSubdivOptions'] = "nurbsToSubdivs.png"

    def _convertPolygonToSubdivOptions(self):
        cmds.CreateSubdivSurfaceOptions()
    commandDict['convertPolygonToSubdivOptions'] = "subdivCreate.png"

    def _convertPolygonEdgesToCurveOptions(self):
        cmds.CreateCurveFromPolyOptions()
    commandDict['convertPolygonEdgesToCurveOptions'] = "menuIconModify.png"

    def _convertSubdivToPolygonsOptions(self):
        cmds.TesselateSubdivSurfaceOptions()
    commandDict['convertSubdivToPolygonsOptions'] = "subdivTessellate.png"

    def _convertSubdivToNURBSOptions(self):
        cmds.SubdivToNURBSOptions()
    commandDict['convertSubdivToNURBSOptions'] = "subdivToNurbs.png"

    def _paintEffectsToPolygonsOptions(self):
        cmds.PaintEffectsToPolyOptions()
    commandDict['paintEffectsToPolygonsOptions'] = "paintFXtoPoly.png"

    def _paintEffectsToNURBSOptions(self):
        cmds.PaintEffectsToNurbsOptions()
    commandDict['paintEffectsToNURBSOptions'] = "paintFXtoNurbs.png"

    def _paintEffectsToCurveOptions(self):
        cmds.PaintEffectsToCurveOptions()
    commandDict['paintEffectsToCurveOptions'] = "paintFXtoCurve.png"

    def _textureToGeometryOptions(self):
        mel.eval("""performTextureToGeom 1""")
    commandDict['textureToGeometryOptions'] = "textureToGeom.png"
