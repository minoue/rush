import maya.cmds as cmds
import os
import sys

iconPaths = os.environ['XBMLANGPATH']
if sys.platform == "linux2":
    for path in iconPaths.split(":"):
        if 'vray/icons' in path:
            iconPath = path
            break
        else:
            iconPath = ""
elif sys.platform == "darwin":
    for path in iconPaths.split(":"):
        if 'vray/icons' in path:
            iconPath = path
            break
        else:
            iconPath = ""
elif sys.platform == "win32":
    for path in iconPaths.split(";"):
        if 'vray/icons' in path:
            iconPath = path
            break
        else:
            iconPath = ""
else:
    iconPath = ""

# iconPath = r"C:\Program Files\Autodesk\Maya2013\vray\icons"


class Commands(object):

    vrayDict = {}

    def __init__(self):
        pass

    def _VRayBlendMtl(self):
        cmds.shadingNode('VRayBlendMtl', asShader=True)
    vrayDict[
        'VRayBlendMtl'] = "%s/render_VRayBlendMtl.png" % iconPath

    def _VRayBumpMtl(self):
        cmds.shadingNode('VRayBumpMtl', asShader=True)
    vrayDict['VRayBumpMtl'] = "%s/render_VRayBumpMtl.png" % iconPath

    def _VRayCarPaintMtl(self):
        cmds.shadingNode('VRayCarPaintMtl', asShader=True)
    vrayDict[
        'VRayCarPaintMtl'] = "%s/render_VRayCarPaintMtl.png" % iconPath

    def _VRayFastSSS2(self):
        cmds.shadingNode('VRayFastSSS2', asShader=True)
    vrayDict[
        'VRayFastSSS2'] = "%s/render_VRayFastSSS2.png" % iconPath

    def _VRayFlakesMtl(self):
        cmds.shadingNode('VRayFlakesMtl', asShader=True)
    vrayDict[
        'VRayFlakesMtl'] = "%s/render_VRayFlakesMtl.png" % iconPath

    def _VRayLightMtl(self):
        cmds.shadingNode('VRayLightMtl', asShader=True)
    vrayDict[
        'VRayLightMtl'] = "%s/render_VRayLightMtl.png" % iconPath

    def _VRayMeshMaterial(self):
        cmds.shadingNode('VRayMeshMaterial', asShader=True)
    vrayDict[
        'VRayMeshMaterial'] = "%s/render_VRayMeshMaterial.png" % iconPath

    def _VRayMtl(self):
        cmds.shadingNode('VRayMtl', asShader=True)
    vrayDict['VRayMtl'] = "%s/render_VRayMtl.png" % iconPath

    def _VRayMtl2Sided(self):
        cmds.shadingNode('VRayMtl2Sided', asShader=True)
    vrayDict[
        'VRayMtl2Sided'] = "%s/render_VRayMtl2Sided.png" % iconPath

    def _VRayMtlHair2(self):
        cmds.shadingNode('VRayMtlHair2', asShader=True)
    vrayDict['VRayMtlHair2'] = "render_unknown.png"

    def _VRayMtlHair3(self):
        cmds.shadingNode('VRayMtlHair3', asShader=True)
    vrayDict['VRayMtlHair3'] = "render_unknown.png"

    def _VRayMtlWrapper(self):
        cmds.shadingNode('VRayMtlWrapper', asShader=True)
    vrayDict[
        'VRayMtlWrapper'] = "%s/render_VRayMtlWrapper.png" % iconPath

    def _VRayPluginNodeMtl(self):
        cmds.shadingNode('VRayPluginNodeMtl', asShader=True)
    vrayDict[
        'VRayPluginNodeMtl'] = "%s/render_VRayPluginNodeTex.png" % iconPath

    def _VRaySimbiont(self):
        cmds.shadingNode('VRaySimbiont', asShader=True)
    vrayDict[
        'VRaySimbiont'] = "%s/render_VRaySimbiont.png" % iconPath

    def _VRayEnvironmentFog(self):
        cmds.shadingNode('VRayEnvironmentFog', asShader=True)
    vrayDict[
        'VRayEnvironmentFog'] = ("%s"
                                 "/render_VRayEnvironmentFog.png"
                                 ) % iconPath

    def _VRayScatterFog(self):
        cmds.shadingNode('VRayScatterFog', asShader=True)
    vrayDict[
        'VRayScatterFog'] = "%s/render_VRayScatterFog.png" % iconPath

    def _VRaySimpleFog(self):
        cmds.shadingNode('VRaySimpleFog', asShader=True)
    vrayDict[
        'VRaySimpleFog'] = "%s/render_VRaySimpleFog.png" % iconPath

    def _VRaySphereFadeVolume(self):
        cmds.shadingNode('VRaySphereFadeVolume', asShader=True)
    vrayDict[
        'VRaySphereFadeVolume'] = ("%s"
                                   "/render_VRaySphereFadeVolume.png"
                                   ) % iconPath

    def _VRayDirt(self):
        node = cmds.shadingNode('VRayDirt', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    vrayDict['VRayDirt'] = "%s/render_VRayDirt.png" % iconPath

    def _VRayEdges(self):
        node = cmds.shadingNode('VRayEdges', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    vrayDict['VRayEdges'] = "%s/render_VRayEdges.png" % iconPath

    def _VRayFresnel(self):
        node = cmds.shadingNode('VRayFresnel', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    vrayDict[
        'VRayFresnel'] = ("%s"
                          "/render_VRayFresnel.png"
                          ) % iconPath

    def _VRayVertexColors(self):
        node = cmds.shadingNode('VRayVertexColors', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    vrayDict[
        'VRayVertexColors'] = ("%s"
                               "/render_VRayVertexColors.png"
                               ) % iconPath

    def _VRayWater(self):
        node = cmds.shadingNode('VRayWater', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    vrayDict[
        'VRayWater'] = ("%s"
                        "/render_VRayWater.png"
                        ) % iconPath

    def _VRayParticleTex(self):
        node = cmds.shadingNode('VRayParticleTex', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    vrayDict[
        'VRayParticleTex'] = ("%s"
                              "/render_VRayParticleTex.png"
                              ) % iconPath

    def _VRaySky(self):
        cmds.shadingNode('VRaySky', asTexture=True)
    vrayDict['VRaySky'] = "%s/render_VRaySky.png" % iconPath

    def _VRayPtex(self):
        cmds.shadingNode('VRayPtex', asTexture=True)
    vrayDict['VRayPtex'] = "%s/render_VRayPtex.png" % iconPath

    def _VRayLightDomeShape(self):
        cmds.shadingNode('VRayLightDomeShape', asLight=True)
    vrayDict[
        'VRayLightDomeShape'] = ("%s"
                                 "/render_VRayLightDomeShape.png"
                                 ) % iconPath

    def _VRayLightIESShape(self):
        cmds.shadingNode('VRayLightIESShape', asLight=True)
    vrayDict[
        'VRayLightIESShape'] = ("%s"
                                "/render_VRayLightIESShape.png"
                                ) % iconPath

    def _VRayLightRectShape(self):
        cmds.shadingNode('VRayLightRectShape', asLight=True)
    vrayDict[
        'VRayLightRectShape'] = ("%s"
                                 "/render_VRayLightRectShape.png"
                                 ) % iconPath

    def _VRayLightSphereShape(self):
        cmds.shadingNode('VRayLightSphereShape', asLight=True)
    vrayDict[
        'VRayLightSphereShape'] = ("%s"
                                   "/render_VRayLightSphereShape.png"
                                   ) % iconPath

    def _VRaySunShape(self):
        cmds.shadingNode('VRaySunShape', asLight=True)
    vrayDict[
        'VRaySunShape'] = "%s/render_VRaySunShape.png" % iconPath

    def _VRayDistanceTex(self):
        cmds.shadingNode('VRayDistanceTex', asUtility=True)
    vrayDict[
        'VRayDistanceTex'] = "render_unknown.png"

    def _VRayFurSampler(self):
        cmds.shadingNode('VRayFurSampler', asUtility=True)
    vrayDict[
        'VRayFurSampler'] = "%s/render_VRayFurSampler.png" % iconPath

    def _VRayHairSampler(self):
        cmds.shadingNode('VRayHairSampler', asUtility=True)
    vrayDict[
        'VRayHairSampler'] = "%s/render_VRayHairSampler.png" % iconPath

    def _VRayObjectProperties(self):
        cmds.shadingNode('VRayObjectProperties', asUtility=True)
    vrayDict[
        'VRayObjectProperties'] = "render_unknown.png"

    def _VRayPlaceEnvTex(self):
        cmds.shadingNode('VRayPlaceEnvTex', asUtility=True)
    vrayDict[
        'VRayPlaceEnvTex'] = "%s/render_VRayPlaceEnvTex.png" % iconPath

    def _VRayRenderElementSet(self):
        cmds.shadingNode('VRayRenderElementSet', asUtility=True)
    vrayDict[
        'VRayRenderElementSet'] = "render_unknown.png"

    def _VRayShInfo(self):
        cmds.shadingNode('VRayShInfo', asUtility=True)
    vrayDict['VRayShInfo'] = "render_unknown.png"

    def _VRaySwitchTransform(self):
        cmds.shadingNode('VRaySwitchTransform', asUtility=True)
    vrayDict[
        'VRaySwitchTransform'] = ("%s"
                                  "/render_VRaySwitchTransform.png"
                                  ) % iconPath

    def _VRayUserColor(self):
        cmds.shadingNode('VRayUserColor', asUtility=True)
    vrayDict[
        'VRayUserColor'] = "render_unknown.png"

    def _VRayUserScalar(self):
        cmds.shadingNode('VRayUserScalar', asUtility=True)
    vrayDict[
        'VRayUserScalar'] = "render_unknown.png"
