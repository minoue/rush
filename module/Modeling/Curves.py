from maya import mel
from maya import cmds


class Commands(object):
    """ class name must be 'Commands' """

    commandDict = {}

    def _curve_lockLength(self):
        cmds.LockCurveLength()
    commandDict['curve_lockLength'] = "lockLength.png"

    def _curve_unlockLength(self):
        cmds.UnlockCurveLength()
    commandDict['curve_unlockLength'] = "unlockLength.png"

    def _curve_bend(self):
        cmds.BendCurves()
    commandDict['curve_bend'] = "modifyBend.png"

    def _curve_bend_Options(self):
        cmds.BendCurvesOptions()
    commandDict['curve_bend_Options'] = "modifyBend.png"

    def _curve_curl(self):
        cmds.CurlCurves()
    commandDict['curve_curl'] = "modifyCurl.png"

    def _curve_curl_Options(self):
        cmds.CurlCurvesOptions()
    commandDict['curve_curl_Options'] = "modifyCurl.png"

    def _curve_scaleCurvature(self):
        cmds.ScaleCurvature()
    commandDict['curve_scaleCurvature'] = "modifyScaleCurvature.png"

    def _curve_scaleCurvature_Options(self):
        cmds.ScaleCurvatureOptions()
    commandDict['curve_scaleCurvature_Options'] = "modifyScaleCurvature.png"

    def _curve_smooth(self):
        cmds.SmoothCurve()
    commandDict['curve_smooth'] = "modifySmooth.png"

    def _curve_smooth_Options(self):
        cmds.SmoothCurveOptions()
    commandDict['curve_smooth_Options'] = "modifySmooth.png"

    def _curve_straighten(self):
        cmds.StraightenCurves()
    commandDict['curve_straighten'] = "modifyStraighten.png"

    def _curve_straighten_Options(self):
        cmds.StraightenCurvesOptions()
    commandDict['curve_straighten_Options'] = "modifyStraighten.png"

    def _curve_duplicateSurfaceCurves(self):
        mel.eval("""duplicateCurvePresetArgList( "2", {"1","0","0","2"} )""")
    commandDict['curve_duplicateSurfaceCurves'] = "duplicateCurve.png"

    def _curve_align(self):
        cmds.AlignCurve()
    commandDict['curve_align'] = "alignCurve.png"

    def _curve_align_Options(self):
        cmds.AlignCurveOptions()
    commandDict['curve_align_Options'] = "alignCurve.png"

    def _curve_addPointTool(self):
        cmds.AddPointsTool()
    commandDict['curve_addPointTool'] = "curveAddPt.png"

    def _curve_attach(self):
        cmds.AttachCurve()
    commandDict['curve_attach'] = "attachCurves.png"

    def _curve_attach_Options(self):
        cmds.AttachCurveOptions()
    commandDict['curve_attach_Options'] = "attachCurves.png"

    def _curve_detach(self):
        cmds.DetachCurve()
    commandDict['curve_detach'] = "detachCurve.png"

    def _curve_detach_Options(self):
        cmds.DetachCurveOptions()
    commandDict['curve_detach_Options'] = "detachCurve.png"

    def _curve_editCurveTool(self):
        cmds.CurveEditTool()
    commandDict['curve_editCurveTool'] = "curveEditor.png"

    def _curve_moveSeam(self):
        mel.eval("""moveNurbsCurveSeam""")
    commandDict['curve_moveSeam'] = "newSeamLocation.png"

    def _curve_opneClose(self):
        cmds.OpenCloseCurve()
    commandDict['curve_openClose'] = "closeGeom.png"

    def _curve_extend(self):
        cmds.ExtendCurve()
    commandDict['curve_extend'] = "extend.png"

    def _curve_extend_Options(self):
        cmds.ExtendCurveOptions()
    commandDict['curve_extend_Options'] = "extend.png"

    def _curve_extendOnSurface(self):
        cmds.ExtendCurveOnSurface()
    commandDict['curve_extendOnSurface'] = "extendCos.png"

    def _curve_extendOnSurface_Options(self):
        cmds.ExtendCurveOnSurfaceOptions()
    commandDict['curve_extendOnSurface_Options'] = "extendCos.png"

    def _curve_rebuild(self):
        cmds.RebuildCurve()
    commandDict['curve_rebuild'] = "rebuildCurve.png"

    def _curve_rebuild_Options(self):
        cmds.RebuildCurveOptions()
    commandDict['curve_rebuild_Options'] = "rebuildCurve.png"

    def _curve_reverseDirection(self):
        cmds.ReverseCurve()
    commandDict['curve_reverseDirection'] = "reverse.png"

    def _curve_reverseDirection_Options(self):
        cmds.ReverseCurveOptions()
    commandDict['curve_reverseDirection_Options'] = "reverse.png"
