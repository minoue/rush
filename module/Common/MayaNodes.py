from maya import cmds


commandDict = {}


# ################################ #
# ###### Maya Default Nodes ###### #
# ################################ #


# Surface

def ShaderfxShader():
    cmds.shadingNode('ShaderfxShader', asShader=True)


commandDict['blinn'] = "render_blinn.png"


def blinn():
    cmds.shadingNode('blinn', asShader=True)


commandDict['blinn'] = "render_blinn.png"


def anisotropic():
    cmds.shadingNode('anisotropic', asShader=True)


commandDict['anisotropic'] = "render_anisotropic.png"


def bifrostLiquidMaterial():
    cmds.shadingNode('bifrostLiquidMaterial', asShader=True)


commandDict['bifrostLiquidMaterial'] = "render_blinn.png"


def hairTubeShader():
    cmds.shadingNode('hairTubeShader', asShader=True)


commandDict['hairTubeShader'] = "render_hairTubeShader.png"


def lambert():
    cmds.shadingNode('lambert', asShader=True)


commandDict['lambert'] = "render_lambert.png"


def layeredShader():
    cmds.shadingNode('layeredShader', asShader=True)


commandDict['layeredShader'] = "render_layeredShader.png"


def oceanShader():
    node = cmds.shadingNode('oceanShader', asTexture=True)
    cmds.connectAttr("time1.outTime", node + ".time")


commandDict['oceanShader'] = "render_oceanShader.png"


def phong():
    cmds.shadingNode('phong', asShader=True)


commandDict['phong'] = "render_phong.png"


def phongE():
    cmds.shadingNode('phongE', asShader=True)


commandDict['phongE'] = "render_phongE.png"


def rampShader():
    cmds.shadingNode('rampShader', asShader=True)


commandDict['rampShader'] = "render_ramp.png"


def shadingMap():
    cmds.shadingNode('shadingMap', asShader=True)


commandDict['shadingMap'] = "render_shadingMap.png"


def surfaceShader():
    cmds.shadingNode('surfaceShader', asShader=True)


commandDict['surfaceShader'] = "render_surfaceShader.png"


def useBackground():
    cmds.shadingNode('useBackground', asShader=True)


commandDict['useBackground'] = "render_useBackground.png"


# vlumetric

def envFog():
    node = cmds.shadingNode('envFog', asShader=True)
    shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                            empty=True, name=node + "SG")
    cmds.connectAttr(
        node + '.outColor', shaderGroup + '.volumeShader', force=True)


commandDict['envFog'] = "render_envFog.png"


def fluidShape():
    node = cmds.shadingNode('fluidShape', asShader=True)
    shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                            empty=True, name=node + "SG")
    cmds.connectAttr(
        node + '.outColor', shaderGroup + '.volumeShader', force=True)
    cmds.connectAttr("time1.outTime", node + ".currentTime")


commandDict['fluidShape'] = "render_fluidShape.png"


def lightFog():
    node = cmds.shadingNode('lightFog', asShader=True)
    shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                            empty=True, name=node + "SG")
    cmds.connectAttr(
        node + '.outColor', shaderGroup + '.volumeShader', force=True)


commandDict['lightFog'] = "render_lightFog.png"


def particleCloud():
    node = cmds.shadingNode('particleCloud', asShader=True)
    shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                            empty=True, name=node + "SG")
    cmds.connectAttr(
        node + '.outColor', shaderGroup + '.volumeShader', force=True)


commandDict['particleCloud'] = "render_particleCloud.png"


def volumeFog():
    node = cmds.shadingNode('volumeFog', asShader=True)
    shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                            empty=True, name=node + "SG")
    cmds.connectAttr(
        node + '.outColor', shaderGroup + '.volumeShader', force=True)


commandDict['volumeFog'] = "render_volumeFog.png"


def volumeShader():
    node = cmds.shadingNode('volumeShader', asShader=True)
    shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                            empty=True, name=node + "SG")
    cmds.connectAttr(
        node + '.outColor', shaderGroup + '.volumeShader', force=True)


commandDict['volumeShader'] = "render_volumeShader.png"


# Displacement

def cMuscleShader():
    node = cmds.shadingNode('cMuscleShader', asShader=True)
    shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                            empty=True, name=node + "SG")
    cmds.connectAttr(
        node + '.outColor',
        shaderGroup + '.displacementShader',
        force=True)


commandDict['volumeShader'] = "sphere.png"


def displacementShader():
    node = cmds.shadingNode('displacementShader', asShader=True)
    shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                            empty=True, name=node + "SG")
    cmds.connectAttr(
        node + '.displacement',
        shaderGroup + '.displacementShader',
        force=True)


commandDict['displacementShader'] = "render_displacementShader.png"


# Utilities

def addDoubleLinear():
    cmds.shadingNode('addDoubleLinear', asUtility=True)


commandDict['addDoubleLinear'] = "render_addDoubleLinear.png"


def addMatrix():
    cmds.shadingNode('addMatrix', asUtility=True)


commandDict['addMatrix'] = "render_addMatrix.png"


def angleBetween():
    cmds.shadingNode('angleBetween', asUtility=True)


commandDict['angleBetween'] = "render_angleBetween.png"


def arrayMapper():
    cmds.shadingNode('arrayMapper', asUtility=True)


commandDict['arrayMapper'] = "render_arrayMapper.png"


def blendColors():
    cmds.shadingNode('blendColors', asUtility=True)


commandDict['blendColors'] = "render_blendColors.png"


def blendTwoAttr():
    cmds.shadingNode('blendTwoAttr', asUtility=True)


commandDict['blendTwoAttr'] = "render_blendTwoAttr.png"


def bump2d():
    cmds.shadingNode('bump2d', asUtility=True)


commandDict['bump2d'] = "render_bump2d.png"


def bump3d():
    cmds.shadingNode('bump3d', asUtility=True)


commandDict['bump3d'] = "render_bump3d.png"


def choice():
    cmds.shadingNode('choice', asUtility=True)


commandDict['choice'] = "render_choice.png"


def chooser():
    cmds.shadingNode('chooser', asUtility=True)


commandDict['chooser'] = "render_chooser.png"


def clamp():
    cmds.shadingNode('clamp', asUtility=True)


commandDict['clamp'] = "render_clamp.png"


def colorProfile():
    cmds.shadingNode('colorProfile', asUtility=True)


commandDict['colorProfile'] = "render_colorProfile.png"


def composeMatrix():
    cmds.shadingNode('composeMatrix', asUtility=True)


commandDict['addMatrix'] = "render_addMatrix.png"


def condition():
    cmds.shadingNode('condition', asUtility=True)


commandDict['condition'] = "render_condition.png"


def contrast():
    cmds.shadingNode('contrast', asUtility=True)


commandDict['contrast'] = "render_contrast.png"


def curveInfo():
    cmds.shadingNode('curveInfo', asUtility=True)


commandDict['curveInfo'] = "render_curveInfo.png"


def decomposeMatrix():
    cmds.shadingNode('decomposeMatrix', asUtility=True)


commandDict['decomposeMatrix'] = "render_decomposeMatrix.png"


def distanceBetween():
    cmds.shadingNode('distanceBetween', asUtility=True)


commandDict['distanceBetween'] = "render_distanceDimShape.png"


def doubleShadingSwitch():
    cmds.shadingNode('doubleShadingSwitch', asUtility=True)


commandDict['doubleShadingSwitch'] = "render_doubleShadingSwitch.png"


def frameCache():
    cmds.shadingNode('frameCache', asUtility=True)


commandDict['doubleShadingSwitch'] = ""


def gammaCorrect():
    cmds.shadingNode('gammaCorrect', asUtility=True)


commandDict['gammaCorrect'] = "render_gammaCorrect.png"


def heightField():
    cmds.shadingNode('heightField', asUtility=True)


commandDict['heightField'] = "render_heightField.png"


def hsvToRgb():
    cmds.shadingNode('hsvToRgb', asUtility=True)


commandDict['hsvToRgb'] = "render_hsvToRgb.png"


def inverseMatrix():
    cmds.shadingNode('inverseMatrix', asUtility=True)


commandDict['inverseMatrix'] = "render_addMatrix.png"


def lightInfo():
    cmds.shadingNode('lightInfo', asUtility=True)


commandDict['lightInfo'] = "render_lightInfo.png"


def luminance():
    cmds.shadingNode('luminance', asUtility=True)


commandDict['luminance'] = "render_luminance.png"


def multDoubleLinear():
    cmds.shadingNode('multDoubleLinear', asUtility=True)


commandDict['multDoubleLinear'] = "render_multDoubleLinear.png"


def multiplyDivide():
    cmds.shadingNode('multiplyDivide', asUtility=True)


commandDict['multiplyDivide'] = "render_multiplyDivide.png"


def particleSamplerInfo():
    cmds.shadingNode('particleSamplerInfo', asUtility=True)


commandDict['particleSamplerInfo'] = "render_particleSamplerInfo.png"


def place2dTexture():
    cmds.shadingNode('place2dTexture', asUtility=True)


commandDict['place2dTexture'] = "render_place2dTexture.png"


def place3dTexture():
    cmds.shadingNode('place3dTexture', asUtility=True)


commandDict['place3dTexture'] = "render_place3dTexture.png"


def plusMinusAverage():
    cmds.shadingNode('plusMinusAverage', asUtility=True)


commandDict['plusMinusAverage'] = "render_plusMinusAverage.png"


def projection():
    cmds.shadingNode('projection', asUtility=True)


commandDict['projection'] = "render_projection.png"


def quadShadingSwitch():
    cmds.shadingNode('quadShadingSwitch', asUtility=True)


commandDict['quadShadingSwitch'] = "render_quadShadingSwitch.png"


def remapColor():
    cmds.shadingNode('remapColor', asUtility=True)


commandDict['remapColor'] = "render_remapColor.png"


def remapHsv():
    cmds.shadingNode('remapHsv', asUtility=True)


commandDict['remapHsv'] = "render_remapHsv.png"


def remapValue():
    cmds.shadingNode('remapValue', asUtility=True)


commandDict['remapValue'] = "render_remapValue.png"


def reverse():
    cmds.shadingNode('reverse', asUtility=True)


commandDict['reverse'] = "render_reverse.png"


def rgbToHsv():
    cmds.shadingNode('rgbToHsv', asUtility=True)


commandDict['rgbToHsv'] = "render_rgbToHsv.png"


def samplerInfo():
    cmds.shadingNode('samplerInfo', asUtility=True)


commandDict['samplerInfo'] = "render_samplerInfo.png"


def setRange():
    cmds.shadingNode('setRange', asUtility=True)


commandDict['setRange'] = "render_setRange.png"


def singleShadingSwitch():
    cmds.shadingNode('singleShadingSwitch', asUtility=True)


commandDict['singleShadingSwitch'] = "render_singleShadingSwitch.png"


def stencil():
    cmds.shadingNode('stencil', asUtility=True)


commandDict['stencil'] = "render_stencil.png"


def surfaceInfo():
    cmds.shadingNode('surfaceInfo', asUtility=True)


commandDict['surfaceInfo'] = "render_surfaceInfo.png"


def surfaceLuminance():
    cmds.shadingNode('surfaceLuminance', asUtility=True)


commandDict['surfaceLuminance'] = "render_surfaceLuminance.png"


def transposeMatrix():
    cmds.shadingNode('transposeMatrix', asUtility=True)


commandDict['transposeMatrix'] = "render_addMatrix.png"


def tripleShadingSwitch():
    cmds.shadingNode('tripleShadingSwitch', asUtility=True)


commandDict['tripleShadingSwitch'] = "render_tripleShadingSwitch.png"


def unitConversion():
    cmds.shadingNode('unitConversion', asUtility=True)


commandDict['unitConversion'] = "render_unitConversion.png"


def uvChooser():
    cmds.shadingNode('uvChooser', asUtility=True)


commandDict['uvChooser'] = "render_uvChooser.png"


def vectorProduct():
    cmds.shadingNode('vectorProduct', asUtility=True)


commandDict['vectorProduct'] = "render_vectorProduct.png"


# 3d texture
def brownian():
    node = cmds.shadingNode('brownian', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['brownian'] = "render_brownian.png"


def cloud():
    node = cmds.shadingNode('cloud', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['cloud'] = "render_cloud.png"


def crater():
    node = cmds.shadingNode('crater', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['crater'] = "render_crater.png"


def granite():
    node = cmds.shadingNode('granite', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['granite'] = "render_granite.png"


def leather():
    node = cmds.shadingNode('leather', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['leather'] = "render_leather.png"


def mandelbrot3D():
    node = cmds.shadingNode('mandelbrot3D', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['mandelbrot3D'] = "render_mandelbrot3D.png"


def marble():
    node = cmds.shadingNode('marble', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['marble'] = "render_marble.png"


def rock():
    node = cmds.shadingNode('rock', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['rock'] = "render_rock.png"


def snow():
    node = cmds.shadingNode('snow', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['snow'] = "render_snow.png"


def solidFractal():
    node = cmds.shadingNode('solidFractal', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['solidFractal'] = "render_solidFractal.png"


def stucco():
    node = cmds.shadingNode('stucco', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['stucco'] = "render_stucco.png"


def volumeNoise():
    node = cmds.shadingNode('volumeNoise', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['volumeNoise'] = "render_volumeNoise.png"


def wood():
    node = cmds.shadingNode('wood', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['wood'] = "render_wood.png"


def fluidTexture3D():
    node = cmds.shadingNode('fluidTexture3D', asTexture=True)
    cmds.connectAttr(
        "time1.outTime", node + ".currentTime")


commandDict['fluidTexture3D'] = "render_fluidTexture3D.png"


# env texture
def envBall():
    node = cmds.shadingNode('envBall', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['envBall'] = "render_envBall.png"


def envChrome():
    node = cmds.shadingNode('envChrome', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['envChrome'] = "render_envChrome.png"


def envCube():
    node = cmds.shadingNode('envCube', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['envCube'] = "render_envCube.png"


def envSky():
    node = cmds.shadingNode('envSky', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['envSky'] = "render_envSky.png"


def envSphere():
    node = cmds.shadingNode('envSphere', asTexture=True)
    tex = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(
        tex + '.worldInverseMatrix', node + '.placementMatrix')


commandDict['envSphere'] = "render_envSphere.png"


# other textures
def layeredTexture():
    cmds.shadingNode('layeredTexture', asTexture=True)


commandDict['layeredTexture'] = "render_layeredTexture.png"


# imagePlane
def imagePlane():
    cmds.shadingNode('imagePlane', asUtility=True)


commandDict['imagePlane'] = "render_imagePlane.png"


# glow
def opticalFX():
    cmds.shadingNode('opticalFX', asPostProcess=True)


commandDict['opticalFX'] = "render_opticalFX.png"


# 2D textures
def bulge():
    node = cmds.shadingNode('bulge', asTexture=True)
    tex = cmds.shadingNode('place2dTexture', asUtility=True)
    cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
    cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
    cmds.setAttr(tex + '.repeatU', 4)
    cmds.setAttr(tex + '.repeatV', 4)


commandDict['bulge'] = "render_bulge.png"


def checker():
    node = cmds.shadingNode('checker', asTexture=True)
    tex = cmds.shadingNode('place2dTexture', asUtility=True)
    cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
    cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
    cmds.setAttr(tex + '.repeatU', 4)
    cmds.setAttr(tex + '.repeatV', 4)


commandDict['checker'] = "render_checker.png"


def cloth():
    node = cmds.shadingNode('cloth', asTexture=True)
    tex = cmds.shadingNode('place2dTexture', asUtility=True)
    cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
    cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
    cmds.setAttr(tex + '.repeatU', 4)
    cmds.setAttr(tex + '.repeatV', 4)


commandDict['cloth'] = "render_cloth.png"


def file():
    cmds.shadingNode('file', asTexture=True)


commandDict['file'] = "render_file.png"


def fluidTexture2D():
    node = cmds.shadingNode('fluidTexture2D', asTexture=True)
    tex = cmds.shadingNode('place2dTexture', asUtility=True)
    cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
    cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')


commandDict['fluidTexture2D'] = "render_fluidTexture2D.png"


def fractal():
    node = cmds.shadingNode('fractal', asTexture=True)
    tex = cmds.shadingNode('place2dTexture', asUtility=True)
    cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
    cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
    cmds.setAttr(tex + '.repeatU', 1)
    cmds.setAttr(tex + '.repeatV', 1)


commandDict['fractal'] = "render_fractal.png"


def grid():
    node = cmds.shadingNode('grid', asTexture=True)
    tex = cmds.shadingNode('place2dTexture', asUtility=True)
    cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
    cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
    cmds.setAttr(tex + '.repeatU', 4)
    cmds.setAttr(tex + '.repeatV', 4)


commandDict['grid'] = "render_grid.png"


def mandelbrot():
    node = cmds.shadingNode('mandelbrot', asTexture=True)
    tex = cmds.shadingNode('place2dTexture', asUtility=True)
    cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
    cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')


commandDict['mandelbrot'] = "render_mandelbrot.png"


def mountain():
    node = cmds.shadingNode('mountain', asTexture=True)
    tex = cmds.shadingNode('place2dTexture', asUtility=True)
    cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
    cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
    cmds.setAttr(tex + '.repeatU', 1)
    cmds.setAttr(tex + '.repeatV', 1)


commandDict['movie'] = "render_movie.png"


def movie():
    node = cmds.shadingNode('movie', asTexture=True)
    tex = cmds.shadingNode('place2dTexture', asUtility=True)
    cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
    cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
    cmds.setAttr(tex + '.repeatU', 1)
    cmds.setAttr(tex + '.repeatV', 1)


commandDict['movie'] = "render_movie.png"


def noise():
    node = cmds.shadingNode('noise', asTexture=True)
    tex = cmds.shadingNode('place2dTexture', asUtility=True)
    cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
    cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
    cmds.setAttr(tex + '.repeatU', 1)
    cmds.setAttr(tex + '.repeatV', 1)


commandDict['noise'] = "render_noise.png"


def ocean():
    node = cmds.shadingNode('ocean', asTexture=True)
    tex = cmds.shadingNode('place2dTexture', asUtility=True)
    cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
    cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
    cmds.setAttr(tex + '.repeatU', 1)
    cmds.setAttr(tex + '.repeatV', 1)


commandDict['ocean'] = "render_ocean.png"


def psdFileTex():
    cmds.shadingNode('psdFileTex', asTexture=True)


commandDict['psdFileTex'] = "render_psdFileTex.png"


def ramp():
    node = cmds.shadingNode('ramp', asTexture=True)
    tex = cmds.shadingNode('place2dTexture', asUtility=True)
    cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
    cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
    cmds.setAttr(tex + '.repeatU', 1)
    cmds.setAttr(tex + '.repeatV', 1)


commandDict['ramp'] = "render_ramp.png"


def substance():
    node = cmds.shadingNode('substance', asTexture=True)
    tex = cmds.shadingNode('place2dTexture', asUtility=True)
    cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
    cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
    cmds.setAttr(tex + '.repeatU', 1)
    cmds.setAttr(tex + '.repeatV', 1)


commandDict['substance'] = "commandButton.png"


def substanceOutput():
    node = cmds.shadingNode('substanceOutput', asTexture=True)
    tex = cmds.shadingNode('place2dTexture', asUtility=True)
    cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
    cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
    cmds.setAttr(tex + '.repeatU', 1)
    cmds.setAttr(tex + '.repeatV', 1)


commandDict['substanceOutput'] = "commandButton.png"


def water():
    node = cmds.shadingNode('water', asTexture=True)
    tex = cmds.shadingNode('place2dTexture', asUtility=True)
    cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
    cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
    cmds.setAttr(tex + '.repeatU', 1)
    cmds.setAttr(tex + '.repeatV', 1)


commandDict['water'] = "render_water.png"
