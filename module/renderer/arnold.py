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

# iconPath = r"C:\solidangle\mtoadeploy\2013\icons"


class Commands(object):

    arnoldDict = {}

    def __init__(self):
        pass

    def _aiMeshLightMaterial(self):
        cmds.shadingNode('aiMeshLightMaterial', asShader=True)
    arnoldDict['aiMeshLightMaterial'] = "%s/MtoA_Logo.png" % iconPath

    def _aiAmbientOcclusion(self):
        cmds.shadingNode('aiAmbientOcclusion', asShader=True)
    arnoldDict['aiAmbientOcclusion'] = "%s/MtoA_Logo.png" % iconPath

    def _aiHair(self):
        cmds.shadingNode('aiHair', asShader=True)
    arnoldDict['aiHair'] = "%s/MtoA_Logo.png" % iconPath

    def _aiRaySwitch(self):
        cmds.shadingNode('aiRaySwitch', asShader=True)
    arnoldDict['aiRaySwitch'] = "%s/MtoA_Logo.png" % iconPath

    def _aiShadowCatcher(self):
        cmds.shadingNode('aiShadowCatcher', asShader=True)
    arnoldDict['aiShadowCatcher'] = "%s/MtoA_Logo.png" % iconPath

    def _aiSkin(self):
        cmds.shadingNode('aiSkin', asShader=True)
    arnoldDict['aiSkin'] = "%s/MtoA_Logo.png" % iconPath

    def _aiSkinSss(self):
        cmds.shadingNode('aiSkinSss', asShader=True)
    arnoldDict['aiSkinSss'] = "%s/MtoA_Logo.png" % iconPath

    def _aiStandard(self):
        cmds.shadingNode('aiStandard', asShader=True)
    arnoldDict['aiStandard'] = "%s/MtoA_Logo.png" % iconPath

    def _aiUtility(self):
        cmds.shadingNode('aiUtility', asShader=True)
    arnoldDict['aiUtility'] = "%s/MtoA_Logo.png" % iconPath

    def _aiWireframe(self):
        cmds.shadingNode('aiWireframe', asShader=True)
    arnoldDict['aiWireframe'] = "%s/MtoA_Logo.png" % iconPath

    def _aiBump2d(self):
        cmds.shadingNode('aiBump2d', asShader=True)
    arnoldDict['aiBump2d'] = "%s/MtoA_Logo.png" % iconPath

    def _aiBump3d(self):
        cmds.shadingNode('aiBump3d', asShader=True)
    arnoldDict['aiBump3d'] = "%s/MtoA_Logo.png" % iconPath

    def _aiMotionVector(self):
        cmds.shadingNode('aiMotionVector', asShader=True)
    arnoldDict['aiMotionVector'] = "%s/MtoA_Logo.png" % iconPath

    def _aiUserDataBool(self):
        cmds.shadingNode('aiUserDataBool', asShader=True)
    arnoldDict['aiUserDataBool'] = "%s/MtoA_Logo.png" % iconPath

    def _aiUserDataColor(self):
        cmds.shadingNode('aiUserDataColor', asShader=True)
    arnoldDict['aiUserDataColor'] = "%s/MtoA_Logo.png" % iconPath

    def _aiUserDataFloat(self):
        cmds.shadingNode('aiUserDataFloat', asShader=True)
    arnoldDict['aiUserDataFloat'] = "%s/MtoA_Logo.png" % iconPath

    def _aiUserDataInt(self):
        cmds.shadingNode('aiUserDataInt', asShader=True)
    arnoldDict['aiUserDataInt'] = "%s/MtoA_Logo.png" % iconPath

    def _aiUserDataPnt2(self):
        cmds.shadingNode('aiUserDataPnt2', asShader=True)
    arnoldDict['aiUserDataPnt2'] = "%s/MtoA_Logo.png" % iconPath

    def _aiUserDataString(self):
        cmds.shadingNode('aiUserDataString', asShader=True)
    arnoldDict['aiUserDataString'] = "%s/MtoA_Logo.png" % iconPath

    def _aiUserDataVector(self):
        cmds.shadingNode('aiUserDataVector', asShader=True)
    arnoldDict['aiUserDataVector'] = "%s/MtoA_Logo.png" % iconPath

    def _aiVolumeCollector(self):
        cmds.shadingNode('aiVolumeCollector', asShader=True)
    arnoldDict['aiVolumeCollector'] = "%s/MtoA_Logo.png" % iconPath

    def _aiWriteColor(self):
        cmds.shadingNode('aiWriteColor', asShader=True)
    arnoldDict['aiWriteColor'] = "%s/MtoA_Logo.png" % iconPath

    def _aiWriteFloat(self):
        cmds.shadingNode('aiWriteFloat', asShader=True)
    arnoldDict['aiWriteFloat'] = "%s/MtoA_Logo.png" % iconPath

    def _aiFog(self):
        cmds.shadingNode('aiFog', asShader=True)
    arnoldDict['aiFog'] = "%s/MtoA_Logo.png" % iconPath

    def _aiVolumeScattering(self):
        cmds.shadingNode('aiVolumeScattering', asShader=True)
    arnoldDict['aiVolumeScattering'] = "%s/MtoA_Logo.png" % iconPath

    # texture
    def _aiImage(self):
        cmds.shadingNode('aiImage', asTexture=True)
    arnoldDict['aiImage'] = "%s/MtoA_Logo.png" % iconPath

    def _aiNoise(self):
        cmds.shadingNode('aiNoise', asTexture=True)
    arnoldDict['aiNoise'] = "%s/MtoA_Logo.png" % iconPath

    def _aiPhysicalSky(self):
        cmds.shadingNode('aiPhysicalSky', asTexture=True)
    arnoldDict['aiPhysicalSky'] = "%s/MtoA_Logo.png" % iconPath

    def _aiSky(self):
        cmds.shadingNode('aiSky', asTexture=True)
    arnoldDict['aiSky'] = "%s/MtoA_Logo.png" % iconPath

    # Light
    def _aiAreaLight(self):
        cmds.shadingNode('aiAreaLight', asLight=True)
    arnoldDict['aiAreaLight'] = "%s/MtoA_Logo.png" % iconPath

    def _aiPhotometricLight(self):
        cmds.shadingNode('aiPhotometricLight', asLight=True)
    arnoldDict['aiPhotometricLight'] = "%s/MtoA_Logo.png" % iconPath

    def _aiSkyDomeLight(self):
        cmds.shadingNode('aiSkyDomeLight', asLight=True)
    arnoldDict['aiSkyDomeLight'] = "%s/MtoA_Logo.png" % iconPath

    def _aiBarndoor(self):
        cmds.shadingNode('aiBarndoor', asLight=True)
    arnoldDict['aiBarndoor'] = "%s/MtoA_Logo.png" % iconPath

    def _aiGobo(self):
        cmds.shadingNode('aiGobo', asLight=True)
    arnoldDict['aiGobo'] = "%s/MtoA_Logo.png" % iconPath

    def _aiLightBlocker(self):
        cmds.shadingNode('aiLightBlocker', asLight=True)
    arnoldDict['aiLightBlocker'] = "%s/MtoA_Logo.png" % iconPath

    def _aiLightDecay(self):
        cmds.shadingNode('aiLightDecay', asLight=True)
    arnoldDict['aiLightDecay'] = "%s/MtoA_Logo.png" % iconPath
