from maya import mel
from maya import cmds


commandDict = {}


def curve_lockLength():
    cmds.LockCurveLength()


def curve_unlockLength():
    cmds.UnlockCurveLength()


def curve_bend():
    cmds.BendCurves()


def curve_bend_Options():
    cmds.BendCurvesOptions()


def curve_curl():
    cmds.CurlCurves()


def curve_curl_Options():
    cmds.CurlCurvesOptions()


def curve_scaleCurvature():
    cmds.ScaleCurvature()


def curve_scaleCurvature_Options():
    cmds.ScaleCurvatureOptions()


def curve_smooth():
    cmds.SmoothCurve()


def curve_smooth_Options():
    cmds.SmoothCurveOptions()


def curve_straighten():
    cmds.StraightenCurves()


def curve_straighten_Options():
    cmds.StraightenCurvesOptions()


def curve_duplicateSurfaceCurves():
    mel.eval("""duplicateCurvePresetArgList( "2", {"1","0","0","2"} )""")


def curve_align():
    cmds.AlignCurve()


def curve_align_Options():
    cmds.AlignCurveOptions()


def curve_addPointTool():
    cmds.AddPointsTool()


def curve_attach():
    cmds.AttachCurve()


def curve_attach_Options():
    cmds.AttachCurveOptions()


def curve_detach():
    cmds.DetachCurve()


def curve_detach_Options():
    cmds.DetachCurveOptions()


def curve_editCurveTool():
    cmds.CurveEditTool()


def curve_moveSeam():
    mel.eval("""moveNurbsCurveSeam""")


def curve_opneClose():
    cmds.OpenCloseCurve()


def curve_extend():
    cmds.ExtendCurve()


def curve_extend_Options():
    cmds.ExtendCurveOptions()


def curve_extendOnSurface():
    cmds.ExtendCurveOnSurface()


def curve_extendOnSurface_Options():
    cmds.ExtendCurveOnSurfaceOptions()


def curve_rebuild():
    cmds.RebuildCurve()


def curve_rebuild_Options():
    cmds.RebuildCurveOptions()


def curve_reverseDirection():
    cmds.ReverseCurve()


def curve_reverseDirection_Options():
    cmds.ReverseCurveOptions()


commandDict['curve_lockLength'] = "lockLength.png"
commandDict['curve_unlockLength'] = "unlockLength.png"
commandDict['curve_bend'] = "modifyBend.png"
commandDict['curve_bend_Options'] = "modifyBend.png"
commandDict['curve_curl'] = "modifyCurl.png"
commandDict['curve_curl_Options'] = "modifyCurl.png"
commandDict['curve_scaleCurvature'] = "modifyScaleCurvature.png"
commandDict['curve_scaleCurvature_Options'] = "modifyScaleCurvature.png"
commandDict['curve_smooth'] = "modifySmooth.png"
commandDict['curve_smooth_Options'] = "modifySmooth.png"
commandDict['curve_straighten'] = "modifyStraighten.png"
commandDict['curve_duplicateSurfaceCurves'] = "duplicateCurve.png"
commandDict['curve_align'] = "alignCurve.png"
commandDict['curve_align_Options'] = "alignCurve.png"
commandDict['curve_addPointTool'] = "curveAddPt.png"
commandDict['curve_attach'] = "attachCurves.png"
commandDict['curve_attach_Options'] = "attachCurves.png"
commandDict['curve_detach'] = "detachCurve.png"
commandDict['curve_detach_Options'] = "detachCurve.png"
commandDict['curve_editCurveTool'] = "curveEditor.png"
commandDict['curve_moveSeam'] = "newSeamLocation.png"
commandDict['curve_openClose'] = "closeGeom.png"
commandDict['curve_extend'] = "extend.png"
commandDict['curve_extend_Options'] = "extend.png"
commandDict['curve_extendOnSurface'] = "extendCos.png"
commandDict['curve_extendOnSurface_Options'] = "extendCos.png"
commandDict['curve_rebuild'] = "rebuildCurve.png"
commandDict['curve_rebuild_Options'] = "rebuildCurve.png"
commandDict['curve_reverseDirection'] = "reverse.png"
commandDict['curve_reverseDirection_Options'] = "reverse.png"
