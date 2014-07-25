import maya.cmds as cmds


class Commands(object):

    customDict = {}

    def __init__(self):
        pass

    def _locatorOnSelected(self):
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
    customDict['locatorOnSelected'] = "render_locator.png"

    def _polyCubeOnSelected(self):
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
    customDict['polyCubeOnSelected'] = "polyCube.png"

    def _polySphereOnSelected(self):
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
    customDict['polySphereOnSelected'] = "polySphere.png"

    def _polyCylinderOnSelected(self):
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
    customDict['polyCylinderOnSelected'] = "polyCylinder.png"

    def _polyPlaneOnSelected(self):
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
    customDict['polyPlaneOnSelected'] = "polyPlane.png"
