import maya.cmds as cmds
import os
import sys

iconPaths = os.environ['XBMLANGPATH']
if sys.platform == "linux2":
    for path in iconPaths.split(":"):
        if 'solidangle' in path:
            iconPath = path
            break
        else:
            iconPath = ""
elif sys.platform == "darwin":
    for path in iconPaths.split(":"):
        if 'solidangle' in path:
            iconPath = path
            break
        else:
            iconPath = ""
elif sys.platform == "win32":
    for path in iconPaths.split(";"):
        if 'solidangle' in path:
            iconPath = path
            break
        else:
            iconPath = ""
else:
    iconPath = ""


class Commands(object):

    commandDict = {}

    def _aiMeshLightMaterial(self):
        cmds.shadingNode('aiMeshLightMaterial', asShader=True)
    commandDict['aiMeshLightMaterial'] = "%s/MtoA_Logo.png" % iconPath

    def _aiAmbientOcclusion(self):
        cmds.shadingNode('aiAmbientOcclusion', asShader=True)
    commandDict['aiAmbientOcclusion'] = "%s/MtoA_Logo.png" % iconPath

    def _aiHair(self):
        cmds.shadingNode('aiHair', asShader=True)
    commandDict['aiHair'] = "%s/MtoA_Logo.png" % iconPath

    def _aiRaySwitch(self):
        cmds.shadingNode('aiRaySwitch', asShader=True)
    commandDict['aiRaySwitch'] = "%s/MtoA_Logo.png" % iconPath

    def _aiShadowCatcher(self):
        cmds.shadingNode('aiShadowCatcher', asShader=True)
    commandDict['aiShadowCatcher'] = "%s/MtoA_Logo.png" % iconPath

    def _aiSkin(self):
        cmds.shadingNode('aiSkin', asShader=True)
    commandDict['aiSkin'] = "%s/MtoA_Logo.png" % iconPath

    def _aiSkinSss(self):
        cmds.shadingNode('aiSkinSss', asShader=True)
    commandDict['aiSkinSss'] = "%s/MtoA_Logo.png" % iconPath

    def _aiStandard(self):
        cmds.shadingNode('aiStandard', asShader=True)
    commandDict['aiStandard'] = "%s/MtoA_Logo.png" % iconPath

    def _aiUtility(self):
        cmds.shadingNode('aiUtility', asShader=True)
    commandDict['aiUtility'] = "%s/MtoA_Logo.png" % iconPath

    def _aiWireframe(self):
        cmds.shadingNode('aiWireframe', asShader=True)
    commandDict['aiWireframe'] = "%s/MtoA_Logo.png" % iconPath

    def _aiBump2d(self):
        cmds.shadingNode('aiBump2d', asShader=True)
    commandDict['aiBump2d'] = "%s/MtoA_Logo.png" % iconPath

    def _aiBump3d(self):
        cmds.shadingNode('aiBump3d', asShader=True)
    commandDict['aiBump3d'] = "%s/MtoA_Logo.png" % iconPath

    def _aiMotionVector(self):
        cmds.shadingNode('aiMotionVector', asShader=True)
    commandDict['aiMotionVector'] = "%s/MtoA_Logo.png" % iconPath

    def _aiUserDataBool(self):
        cmds.shadingNode('aiUserDataBool', asShader=True)
    commandDict['aiUserDataBool'] = "%s/MtoA_Logo.png" % iconPath

    def _aiUserDataColor(self):
        cmds.shadingNode('aiUserDataColor', asShader=True)
    commandDict['aiUserDataColor'] = "%s/MtoA_Logo.png" % iconPath

    def _aiUserDataFloat(self):
        cmds.shadingNode('aiUserDataFloat', asShader=True)
    commandDict['aiUserDataFloat'] = "%s/MtoA_Logo.png" % iconPath

    def _aiUserDataInt(self):
        cmds.shadingNode('aiUserDataInt', asShader=True)
    commandDict['aiUserDataInt'] = "%s/MtoA_Logo.png" % iconPath

    def _aiUserDataPnt2(self):
        cmds.shadingNode('aiUserDataPnt2', asShader=True)
    commandDict['aiUserDataPnt2'] = "%s/MtoA_Logo.png" % iconPath

    def _aiUserDataString(self):
        cmds.shadingNode('aiUserDataString', asShader=True)
    commandDict['aiUserDataString'] = "%s/MtoA_Logo.png" % iconPath

    def _aiUserDataVector(self):
        cmds.shadingNode('aiUserDataVector', asShader=True)
    commandDict['aiUserDataVector'] = "%s/MtoA_Logo.png" % iconPath

    def _aiVolumeCollector(self):
        cmds.shadingNode('aiVolumeCollector', asShader=True)
    commandDict['aiVolumeCollector'] = "%s/MtoA_Logo.png" % iconPath

    def _aiWriteColor(self):
        cmds.shadingNode('aiWriteColor', asShader=True)
    commandDict['aiWriteColor'] = "%s/MtoA_Logo.png" % iconPath

    def _aiWriteFloat(self):
        cmds.shadingNode('aiWriteFloat', asShader=True)
    commandDict['aiWriteFloat'] = "%s/MtoA_Logo.png" % iconPath

    def _aiFog(self):
        cmds.shadingNode('aiFog', asShader=True)
    commandDict['aiFog'] = "%s/MtoA_Logo.png" % iconPath

    def _aiVolumeScattering(self):
        cmds.shadingNode('aiVolumeScattering', asShader=True)
    commandDict['aiVolumeScattering'] = "%s/MtoA_Logo.png" % iconPath

    # texture
    def _aiImage(self):
        cmds.shadingNode('aiImage', asTexture=True)
    commandDict['aiImage'] = "%s/MtoA_Logo.png" % iconPath

    def _aiNoise(self):
        cmds.shadingNode('aiNoise', asTexture=True)
    commandDict['aiNoise'] = "%s/MtoA_Logo.png" % iconPath

    def _aiPhysicalSky(self):
        cmds.shadingNode('aiPhysicalSky', asTexture=True)
    commandDict['aiPhysicalSky'] = "%s/MtoA_Logo.png" % iconPath

    def _aiSky(self):
        cmds.shadingNode('aiSky', asTexture=True)
    commandDict['aiSky'] = "%s/MtoA_Logo.png" % iconPath

    # Light
    def _aiAreaLight(self):
        cmds.shadingNode('aiAreaLight', asLight=True)
    commandDict['aiAreaLight'] = "%s/MtoA_Logo.png" % iconPath

    def _aiPhotometricLight(self):
        cmds.shadingNode('aiPhotometricLight', asLight=True)
    commandDict['aiPhotometricLight'] = "%s/MtoA_Logo.png" % iconPath

    def _aiSkyDomeLight(self):
        cmds.shadingNode('aiSkyDomeLight', asLight=True)
    commandDict['aiSkyDomeLight'] = "%s/MtoA_Logo.png" % iconPath

    def _aiBarndoor(self):
        cmds.shadingNode('aiBarndoor', asLight=True)
    commandDict['aiBarndoor'] = "%s/MtoA_Logo.png" % iconPath

    def _aiGobo(self):
        cmds.shadingNode('aiGobo', asLight=True)
    commandDict['aiGobo'] = "%s/MtoA_Logo.png" % iconPath

    def _aiLightBlocker(self):
        cmds.shadingNode('aiLightBlocker', asLight=True)
    commandDict['aiLightBlocker'] = "%s/MtoA_Logo.png" % iconPath

    def _aiLightDecay(self):
        cmds.shadingNode('aiLightDecay', asLight=True)
    commandDict['aiLightDecay'] = "%s/MtoA_Logo.png" % iconPath
