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

    def _freezeOnlyScale(self):
        cmds.makeIdentity(apply=True, t=False, r=False, s=True, n=False)
    commandDict['freezeOnlyScale'] = "menuIconModify.png"

    def _nurbsToPolygonOptions(self):
        cmds.NURBSToPolygonsOptions()
    commandDict['nurbsToPolygonOptions'] = "nurbsToPolygons.png"

    def _nurbsToSubdivOptions(self):
        cmds.CreateSubdivSurfaceOptions()
    commandDict['nurbsToSubdivOptions'] = "nurbsToSubdivs.png"

    def _polygonToSubdivOptions(self):
        cmds.CreateSubdivSurfaceOptions()
    commandDict['polygonToSubdivOptions'] = "subdivCreate.png"

    def _polygonEdgesToCurveOptions(self):
        cmds.CreateCurveFromPolyOptions()
    commandDict['polygonEdgesToCurveOptions'] = "menuIconModify.png"

    def _subdivToPolygonsOptions(self):
        cmds.TesselateSubdivSurfaceOptions()
    commandDict['subdivToPolygonsOptions'] = "subdivTessellate.png"

    def _subdivToNURBSOptions(self):
        cmds.SubdivToNURBSOptions()
    commandDict['subdivToNURBSOptions'] = "subdivToNurbs.png"

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
