import maya.cmds as cmds
import maya.mel as mel
import os

class Commands(object):

    commandDict = {}

    def _clearHistory(self):
        MAYA_SCRIPT_DIR = cmds.internalVar(userScriptDir=True)
        histFile = os.path.join(MAYA_SCRIPT_DIR, "miExecutorHistory.txt")
        open(histFile, 'w').close()
    commandDict['clearHistory'] = "menuIconEdit.png"

    def _locatorAtSelection(self):
        try:
            sel = cmds.ls(sl=True, fl=True, r=True)
            nodeType = cmds.nodeType(sel[0])
            if nodeType == "transform":
                pivot = cmds.xform(sel[0], q=True, ws=True, rp=True)
                cmds.spaceLocator(p=[0, 0, 0])
                loc = cmds.ls(sl=True, r=True)[0]
                cmds.setAttr(loc + ".translate", *pivot)
                cmds.CenterPivot()
            elif nodeType == "mesh":
                sel = cmds.ls(sl=True, fl=True, r=True)
                verts = [cmds.xform(i, q=True, ws=True, t=True) for i in sel]
                xs = [i[0] for i in verts]
                ys = [i[1] for i in verts]
                zs = [i[2] for i in verts]
                pos = [sum(xs) / len(sel),
                       sum(ys) / len(sel),
                       sum(zs) / len(sel)]
                cmds.spaceLocator(p=[0, 0, 0])
                loc = cmds.ls(sl=True, r=True)[0]
                cmds.setAttr(loc + ".translate", *pos)
                cmds.CenterPivot()
        except IndexError:
            cmds.spaceLocator(p=[0, 0, 0])
    commandDict['locatorAtSelection'] = "render_locator.png"

    def _polyCubeAtSelection(self):
        try:
            sel = cmds.ls(sl=True, fl=True, r=True)
            nodeType = cmds.nodeType(sel[0])
            if nodeType == "transform":
                pivot = cmds.xform(sel[0], q=True, ws=True, rp=True)
                cmds.polyCube()
                cube = cmds.ls(sl=True, r=True)[0]
                cmds.setAttr(cube + ".translate", *pivot)
                cmds.CenterPivot()
            elif nodeType == "mesh":
                sel = cmds.ls(sl=True, fl=True, r=True)
                verts = [cmds.xform(i, q=True, ws=True, t=True) for i in sel]
                xs = [i[0] for i in verts]
                ys = [i[1] for i in verts]
                zs = [i[2] for i in verts]
                pos = [sum(xs) / len(sel),
                       sum(ys) / len(sel),
                       sum(zs) / len(sel)]
                cmds.polyCube()
                cube = cmds.ls(sl=True, r=True)[0]
                cmds.setAttr(cube + ".translate", *pos)
                cmds.CenterPivot()
        except IndexError:
            cmds.polyCube()
    commandDict['polyCubeAtSelection'] = "polyCube.png"

    def _polySphereAtSelection(self):
        try:
            print "test2"
            sel = cmds.ls(sl=True, fl=True, r=True)
            nodeType = cmds.nodeType(sel[0])
            if nodeType == "transform":
                pivot = cmds.xform(sel[0], q=True, ws=True, rp=True)
                cmds.polySphere()
                sphere = cmds.ls(sl=True, r=True)[0]
                cmds.setAttr(sphere + ".translate", *pivot)
                cmds.CenterPivot()
            elif nodeType == "mesh":
                sel = cmds.ls(sl=True, fl=True, r=True)
                verts = [cmds.xform(i, q=True, ws=True, t=True) for i in sel]
                xs = [i[0] for i in verts]
                ys = [i[1] for i in verts]
                zs = [i[2] for i in verts]
                pos = [sum(xs) / len(sel),
                       sum(ys) / len(sel),
                       sum(zs) / len(sel)]
                cmds.polySphere()
                sphere = cmds.ls(sl=True, r=True)[0]
                cmds.setAttr(sphere + ".translate", *pos)
                cmds.CenterPivot()
        except IndexError:
            cmds.polySphere()
    commandDict['polySphereAtSelection'] = "polySphere.png"

    def _polyCylinderAtSelection(self):
        try:
            sel = cmds.ls(sl=True, fl=True, r=True)
            nodeType = cmds.nodeType(sel[0])
            if nodeType == "transform":
                pivot = cmds.xform(sel[0], q=True, ws=True, rp=True)
                cmds.polyCylinder()
                cylinder = cmds.ls(sl=True, r=True)[0]
                cmds.setAttr(cylinder + ".translate", *pivot)
                cmds.CenterPivot()
            elif nodeType == "mesh":
                sel = cmds.ls(sl=True, fl=True, r=True)
                verts = [cmds.xform(i, q=True, ws=True, t=True) for i in sel]
                xs = [i[0] for i in verts]
                ys = [i[1] for i in verts]
                zs = [i[2] for i in verts]
                pos = [sum(xs) / len(sel),
                       sum(ys) / len(sel),
                       sum(zs) / len(sel)]
                cmds.polyCylinder()
                cylinder = cmds.ls(sl=True, r=True)[0]
                cmds.setAttr(cylinder + ".translate", *pos)
                cmds.CenterPivot()
        except IndexError:
            cmds.polyCylinder()
    commandDict['polyCylinderAtSelection'] = "polyCylinder.png"

    def _polyPlaneAtSelection(self):
        try:
            sel = cmds.ls(sl=True, fl=True, r=True)
            nodeType = cmds.nodeType(sel[0])
            if nodeType == "transform":
                pivot = cmds.xform(sel[0], q=True, ws=True, rp=True)
                cmds.polyPlane()
                plane = cmds.ls(sl=True, r=True)[0]
                cmds.setAttr(plane + ".translate", *pivot)
                cmds.CenterPivot()
            elif nodeType == "mesh":
                sel = cmds.ls(sl=True, fl=True, r=True)
                verts = [cmds.xform(i, q=True, ws=True, t=True) for i in sel]
                xs = [i[0] for i in verts]
                ys = [i[1] for i in verts]
                zs = [i[2] for i in verts]
                pos = [sum(xs) / len(sel),
                       sum(ys) / len(sel),
                       sum(zs) / len(sel)]
                cmds.polyPlane()
                plane = cmds.ls(sl=True, r=True)[0]
                cmds.setAttr(plane + ".translate", *pos)
                cmds.CenterPivot
        except IndexError:
            cmds.polyPlane()
    commandDict['polyPlaneAtSelection'] = "polyPlane.png"

    def _rebuildCurveOptions(self):
        cmds.RebuildCurveOptions()
    commandDict['rebuildCurveOptions'] = "rebuildCurve.png"

    def _createSet(self):
        cmds.CreateSet()
    commandDict['createSet'] = 'menuIconEdit.png'

    def _rebuildSurfacesOptions(self):
        cmds.RebuildSurfacesOptions()
    commandDict['rebuildSurfacesOptions'] = 'rebuildSurface.png'

    def _aTob(self):
        sel = cmds.ls(sl=True, fl=True)
        source = sel[0]
        target = sel[-1]
        pos = cmds.getAttr(target + ".translate")[0]
        rot = cmds.getAttr(target + ".rotate")[0]
        scl = cmds.getAttr(target + ".scale")[0]
        cmds.setAttr(source + ".translate", *pos)
        cmds.setAttr(source + ".rotate", *rot)
        cmds.setAttr(source + ".scale", *scl)
    commandDict['aTob'] = 'sphere.png'

    def _attachBrushToCurves(self, *args):
        cmds.AttachBrushToCurves()
    commandDict['attachBrushToCurves'] = 'rebuildCurve.png'

    def _convertPaintFxToPolygons(self, *args):
        mel.eval("doPaintEffectsToPoly( 1,0,1,1,100000);")
    commandDict['convertPaintFxToPolygons'] = 'polySphere.png'

    def _loadObjPlugin(self):
        if cmds.pluginInfo('objExport', q=True, loaded=True):
            pass
        else:
            cmds.loadPlugin('objExport')
    commandDict['loadObjPlugin'] = 'sphere.png'

    def _showAllHeadsup(self):
        toggle = 1
        mel.eval("setSelectDetailsVisibility(%s);" % toggle)
        mel.eval("setObjectDetailsVisibility(%s);" % toggle)
        mel.eval("setParticleCountVisibility(%s);" % toggle)
        mel.eval("setPolyCountVisibility(%s);" % toggle)
        mel.eval("setAnimationDetailsVisibility(%s);" % toggle)
        mel.eval("setHikDetailsVisibility(%s);" % toggle)
        mel.eval("setFrameRateVisibility(%s);" % toggle)
        mel.eval("setCurrentFrameVisibility(%s);" % toggle)
        mel.eval("setSceneTimecodeVisibility(%s);" % toggle)
        mel.eval("setCurrentContainerVisibility(%s);" % toggle)
        mel.eval("setViewportRendererVisibility(%s);" % toggle)
        mel.eval("setCameraNamesVisibility(%s);" % toggle)
        mel.eval("setFocalLengthVisibility(%s);" % toggle)
        mel.eval("setViewAxisVisibility(%s);" % toggle)
        if toggle == 1:
            cmds.viewManip(v=1)
        else:
            cmds.viewManip(v=0)
        cmds.ToggleOriginAxis()
    commandDict['showAllHeadsup'] = 'sphere.png'

    def _hideAllHeadsup(self):
        toggle = 0
        mel.eval("setSelectDetailsVisibility(%s);" % toggle)
        mel.eval("setObjectDetailsVisibility(%s);" % toggle)
        mel.eval("setParticleCountVisibility(%s);" % toggle)
        mel.eval("setPolyCountVisibility(%s);" % toggle)
        mel.eval("setAnimationDetailsVisibility(%s);" % toggle)
        mel.eval("setHikDetailsVisibility(%s);" % toggle)
        mel.eval("setFrameRateVisibility(%s);" % toggle)
        mel.eval("setCurrentFrameVisibility(%s);" % toggle)
        mel.eval("setSceneTimecodeVisibility(%s);" % toggle)
        mel.eval("setCurrentContainerVisibility(%s);" % toggle)
        mel.eval("setViewportRendererVisibility(%s);" % toggle)
        mel.eval("setCameraNamesVisibility(%s);" % toggle)
        mel.eval("setFocalLengthVisibility(%s);" % toggle)
        mel.eval("setViewAxisVisibility(%s);" % toggle)
        if toggle == 1:
            cmds.viewManip(v=1)
        else:
            cmds.viewManip(v=0)
        cmds.ToggleOriginAxis()
    commandDict['hideAllHeadsup'] = 'sphere.png'
