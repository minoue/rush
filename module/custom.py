import maya.cmds as cmds


class Commands(object):

    customDict = {}

    def __init__(self):
        pass

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
    customDict['locatorAtSelection'] = "render_locator.png"

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
    customDict['polyCubeAtSelection'] = "polyCube.png"

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
    customDict['polySphereAtSelection'] = "polySphere.png"

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
    customDict['polyCylinderAtSelection'] = "polyCylinder.png"

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
    customDict['polyPlaneAtSelection'] = "polyPlane.png"

    def _rebuildCurveOptions(self):
        cmds.RebuildCurveOptions()
    customDict['rebuildCurveOptions'] = "rebuildCurve.png"

    def _createSet(self):
        cmds.CreateSet()
    customDict['createSet'] = 'menuIconEdit.png'

    def _rebuildSurfacesOptions(self):
        cmds.RebuildSurfacesOptions()
    customDict['rebuildSurfacesOptions'] = 'rebuildSurface.png'

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
    customDict['aTob'] = 'sphere.png'
