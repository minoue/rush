import maya.cmds as cmds
import maya.mel as mel


class Commands(object):

    mayaNodeDict = {}

    def __init__(self):
        pass
    # ################################ #
    # ###### Maya Default Nodes ###### #
    # ################################ #

    # Surface

    def _ShaderfxShader(self):
        cmds.shadingNode('ShaderfxShader', asShader=True)
    mayaNodeDict['blinn'] = "render_blinn.png"

    def _blinn(self):
        cmds.shadingNode('blinn', asShader=True)
    mayaNodeDict['blinn'] = "render_blinn.png"

    def _anisotropic(self):
        cmds.shadingNode('anisotropic', asShader=True)
    mayaNodeDict['anisotropic'] = "render_anisotropic.png"

    def _bifrostLiquidMaterial(self):
        cmds.shadingNode('bifrostLiquidMaterial', asShader=True)
    mayaNodeDict['bifrostLiquidMaterial'] = "render_blinn.png"

    def _hairTubeShader(self):
        cmds.shadingNode('hairTubeShader', asShader=True)
    mayaNodeDict['hairTubeShader'] = "render_hairTubeShader.png"

    def _lambert(self):
        cmds.shadingNode('lambert', asShader=True)
    mayaNodeDict['lambert'] = "render_lambert.png"

    def _layeredShader(self):
        cmds.shadingNode('layeredShader', asShader=True)
    mayaNodeDict['layeredShader'] = "render_layeredShader.png"

    def _oceanShader(self):
        node = cmds.shadingNode('oceanShader', asTexture=True)
        cmds.connectAttr("time1.outTime", node + ".time")
    mayaNodeDict['oceanShader'] = "render_oceanShader.png"

    def _phong(self):
        cmds.shadingNode('phong', asShader=True)
    mayaNodeDict['phong'] = "render_phong.png"

    def _phongE(self):
        cmds.shadingNode('phongE', asShader=True)
    mayaNodeDict['phongE'] = "render_phongE.png"

    def _rampShader(self):
        cmds.shadingNode('rampShader', asShader=True)
    mayaNodeDict['rampShader'] = "render_ramp.png"

    def _shadingMap(self):
        cmds.shadingNode('shadingMap', asShader=True)
    mayaNodeDict['shadingMap'] = "render_shadingMap.png"

    def _surfaceShader(self):
        cmds.shadingNode('surfaceShader', asShader=True)
    mayaNodeDict['surfaceShader'] = "render_surfaceShader.png"

    def _useBackground(self):
        cmds.shadingNode('useBackground', asShader=True)
    mayaNodeDict['useBackground'] = "render_useBackground.png"

    # vlumetric

    def _envFog(self):
        node = cmds.shadingNode('envFog', asShader=True)
        shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                                empty=True, name=node + "SG")
        cmds.connectAttr(
            node + '.outColor', shaderGroup + '.volumeShader', force=True)
    mayaNodeDict['envFog'] = "render_envFog.png"

    def _fluidShape(self):
        node = cmds.shadingNode('fluidShape', asShader=True)
        shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                                empty=True, name=node + "SG")
        cmds.connectAttr(
            node + '.outColor', shaderGroup + '.volumeShader', force=True)
        cmds.connectAttr("time1.outTime", node + ".currentTime")
    mayaNodeDict['fluidShape'] = "render_fluidShape.png"

    def _lightFog(self):
        node = cmds.shadingNode('lightFog', asShader=True)
        shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                                empty=True, name=node + "SG")
        cmds.connectAttr(
            node + '.outColor', shaderGroup + '.volumeShader', force=True)
    mayaNodeDict['lightFog'] = "render_lightFog.png"

    def _particleCloud(self):
        node = cmds.shadingNode('particleCloud', asShader=True)
        shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                                empty=True, name=node + "SG")
        cmds.connectAttr(
            node + '.outColor', shaderGroup + '.volumeShader', force=True)
    mayaNodeDict['particleCloud'] = "render_particleCloud.png"

    def _volumeFog(self):
        node = cmds.shadingNode('volumeFog', asShader=True)
        shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                                empty=True, name=node + "SG")
        cmds.connectAttr(
            node + '.outColor', shaderGroup + '.volumeShader', force=True)
    mayaNodeDict['volumeFog'] = "render_volumeFog.png"

    def _volumeShader(self):
        node = cmds.shadingNode('volumeShader', asShader=True)
        shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                                empty=True, name=node + "SG")
        cmds.connectAttr(
            node + '.outColor', shaderGroup + '.volumeShader', force=True)
    mayaNodeDict['volumeShader'] = "render_volumeShader.png"

    # Displacement

    def _cMuscleShader(self):
        node = cmds.shadingNode('cMuscleShader', asShader=True)
        shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                                empty=True, name=node + "SG")
        cmds.connectAttr(
            node + '.outColor',
            shaderGroup + '.displacementShader',
            force=True)
    mayaNodeDict['volumeShader'] = "sphere.png"

    def _displacementShader(self):
        node = cmds.shadingNode('displacementShader', asShader=True)
        shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                                empty=True, name=node + "SG")
        cmds.connectAttr(
            node + '.displacement',
            shaderGroup + '.displacementShader',
            force=True)
    mayaNodeDict['displacementShader'] = "render_displacementShader.png"

    # Utilities

    def _addDoubleLinear(self):
        cmds.shadingNode('addDoubleLinear', asUtility=True)
    mayaNodeDict['addDoubleLinear'] = "render_addDoubleLinear.png"

    def _addMatrix(self):
        cmds.shadingNode('addMatrix', asUtility=True)
    mayaNodeDict['addMatrix'] = "render_addMatrix.png"

    def _angleBetween(self):
        cmds.shadingNode('angleBetween', asUtility=True)
    mayaNodeDict['angleBetween'] = "render_angleBetween.png"

    def _arrayMapper(self):
        cmds.shadingNode('arrayMapper', asUtility=True)
    mayaNodeDict['arrayMapper'] = "render_arrayMapper.png"

    def _blendColors(self):
        cmds.shadingNode('blendColors', asUtility=True)
    mayaNodeDict['blendColors'] = "render_blendColors.png"

    def _blendTwoAttr(self):
        cmds.shadingNode('blendTwoAttr', asUtility=True)
    mayaNodeDict['blendTwoAttr'] = "render_blendTwoAttr.png"

    def _bump2d(self):
        cmds.shadingNode('bump2d', asUtility=True)
    mayaNodeDict['bump2d'] = "render_bump2d.png"

    def _bump3d(self):
        cmds.shadingNode('bump3d', asUtility=True)
    mayaNodeDict['bump3d'] = "render_bump3d.png"

    def _choice(self):
        cmds.shadingNode('choice', asUtility=True)
    mayaNodeDict['choice'] = "render_choice.png"

    def _chooser(self):
        cmds.shadingNode('chooser', asUtility=True)
    mayaNodeDict['chooser'] = "render_chooser.png"

    def _clamp(self):
        cmds.shadingNode('clamp', asUtility=True)
    mayaNodeDict['clamp'] = "render_clamp.png"

    def _colorProfile(self):
        cmds.shadingNode('colorProfile', asUtility=True)
    mayaNodeDict['colorProfile'] = "render_colorProfile.png"

    def _composeMatrix(self):
        cmds.shadingNode('composeMatrix', asUtility=True)
    mayaNodeDict['addMatrix'] = "render_addMatrix.png"

    def _condition(self):
        cmds.shadingNode('condition', asUtility=True)
    mayaNodeDict['condition'] = "render_condition.png"

    def _contrast(self):
        cmds.shadingNode('contrast', asUtility=True)
    mayaNodeDict['contrast'] = "render_contrast.png"

    def _curveInfo(self):
        cmds.shadingNode('curveInfo', asUtility=True)
    mayaNodeDict['curveInfo'] = "render_curveInfo.png"

    def _decomposeMatrix(self):
        cmds.shadingNode('decomposeMatrix', asUtility=True)
    mayaNodeDict['decomposeMatrix'] = "render_decomposeMatrix.png"

    def _distanceBetween(self):
        cmds.shadingNode('distanceBetween', asUtility=True)
    mayaNodeDict['distanceBetween'] = "render_distanceDimShape.png"

    def _doubleShadingSwitch(self):
        cmds.shadingNode('doubleShadingSwitch', asUtility=True)
    mayaNodeDict['doubleShadingSwitch'] = "render_doubleShadingSwitch.png"

    def _frameCache(self):
        cmds.shadingNode('frameCache', asUtility=True)
    mayaNodeDict['doubleShadingSwitch'] = ""

    def _gammaCorrect(self):
        cmds.shadingNode('gammaCorrect', asUtility=True)
    mayaNodeDict['gammaCorrect'] = "render_gammaCorrect.png"

    def _heightField(self):
        cmds.shadingNode('heightField', asUtility=True)
    mayaNodeDict['heightField'] = "render_heightField.png"

    def _hsvToRgb(self):
        cmds.shadingNode('hsvToRgb', asUtility=True)
    mayaNodeDict['hsvToRgb'] = "render_hsvToRgb.png"

    def _inverseMatrix(self):
        cmds.shadingNode('inverseMatrix', asUtility=True)
    mayaNodeDict['inverseMatrix'] = "render_addMatrix.png"

    def _lightInfo(self):
        cmds.shadingNode('lightInfo', asUtility=True)
    mayaNodeDict['lightInfo'] = "render_lightInfo.png"

    def _luminance(self):
        cmds.shadingNode('luminance', asUtility=True)
    mayaNodeDict['luminance'] = "render_luminance.png"

    def _multDoubleLinear(self):
        cmds.shadingNode('multDoubleLinear', asUtility=True)
    mayaNodeDict['multDoubleLinear'] = "render_multDoubleLinear.png"

    def _multiplyDivide(self):
        cmds.shadingNode('multiplyDivide', asUtility=True)
    mayaNodeDict['multiplyDivide'] = "render_multiplyDivide.png"

    def _particleSamplerInfo(self):
        cmds.shadingNode('particleSamplerInfo', asUtility=True)
    mayaNodeDict['particleSamplerInfo'] = "render_particleSamplerInfo.png"

    def _place2dTexture(self):
        cmds.shadingNode('place2dTexture', asUtility=True)
    mayaNodeDict['place2dTexture'] = "render_place2dTexture.png"

    def _place3dTexture(self):
        cmds.shadingNode('place3dTexture', asUtility=True)
    mayaNodeDict['place3dTexture'] = "render_place3dTexture.png"

    def _plusMinusAverage(self):
        cmds.shadingNode('plusMinusAverage', asUtility=True)
    mayaNodeDict['plusMinusAverage'] = "render_plusMinusAverage.png"

    def _projection(self):
        cmds.shadingNode('projection', asUtility=True)
    mayaNodeDict['projection'] = "render_projection.png"

    def _quadShadingSwitch(self):
        cmds.shadingNode('quadShadingSwitch', asUtility=True)
    mayaNodeDict['quadShadingSwitch'] = "render_quadShadingSwitch.png"

    def _remapColor(self):
        cmds.shadingNode('remapColor', asUtility=True)
    mayaNodeDict['remapColor'] = "render_remapColor.png"

    def _remapHsv(self):
        cmds.shadingNode('remapHsv', asUtility=True)
    mayaNodeDict['remapHsv'] = "render_remapHsv.png"

    def _remapValue(self):
        cmds.shadingNode('remapValue', asUtility=True)
    mayaNodeDict['remapValue'] = "render_remapValue.png"

    def _reverse(self):
        cmds.shadingNode('reverse', asUtility=True)
    mayaNodeDict['reverse'] = "render_reverse.png"

    def _rgbToHsv(self):
        cmds.shadingNode('rgbToHsv', asUtility=True)
    mayaNodeDict['rgbToHsv'] = "render_rgbToHsv.png"

    def _samplerInfo(self):
        cmds.shadingNode('samplerInfo', asUtility=True)
    mayaNodeDict['samplerInfo'] = "render_samplerInfo.png"

    def _setRange(self):
        cmds.shadingNode('setRange', asUtility=True)
    mayaNodeDict['setRange'] = "render_setRange.png"

    def _singleShadingSwitch(self):
        cmds.shadingNode('singleShadingSwitch', asUtility=True)
    mayaNodeDict['singleShadingSwitch'] = "render_singleShadingSwitch.png"

    def _stencil(self):
        cmds.shadingNode('stencil', asUtility=True)
    mayaNodeDict['stencil'] = "render_stencil.png"

    def _surfaceInfo(self):
        cmds.shadingNode('surfaceInfo', asUtility=True)
    mayaNodeDict['surfaceInfo'] = "render_surfaceInfo.png"

    def _surfaceLuminance(self):
        cmds.shadingNode('surfaceLuminance', asUtility=True)
    mayaNodeDict['surfaceLuminance'] = "render_surfaceLuminance.png"

    def _transposeMatrix(self):
        cmds.shadingNode('transposeMatrix', asUtility=True)
    mayaNodeDict['transposeMatrix'] = "render_addMatrix.png"

    def _tripleShadingSwitch(self):
        cmds.shadingNode('tripleShadingSwitch', asUtility=True)
    mayaNodeDict['tripleShadingSwitch'] = "render_tripleShadingSwitch.png"

    def _unitConversion(self):
        cmds.shadingNode('unitConversion', asUtility=True)
    mayaNodeDict['unitConversion'] = "render_unitConversion.png"

    def _uvChooser(self):
        cmds.shadingNode('uvChooser', asUtility=True)
    mayaNodeDict['uvChooser'] = "render_uvChooser.png"

    def _vectorProduct(self):
        cmds.shadingNode('vectorProduct', asUtility=True)
    mayaNodeDict['vectorProduct'] = "render_vectorProduct.png"

    # 3d texture
    def _brownian(self):
        node = cmds.shadingNode('brownian', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['brownian'] = "render_brownian.png"

    def _cloud(self):
        node = cmds.shadingNode('cloud', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['cloud'] = "render_cloud.png"

    def _crater(self):
        node = cmds.shadingNode('crater', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['crater'] = "render_crater.png"

    def _granite(self):
        node = cmds.shadingNode('granite', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['granite'] = "render_granite.png"

    def _leather(self):
        node = cmds.shadingNode('leather', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['leather'] = "render_leather.png"

    def _mandelbrot3D(self):
        node = cmds.shadingNode('mandelbrot3D', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['mandelbrot3D'] = "render_mandelbrot3D.png"

    def _marble(self):
        node = cmds.shadingNode('marble', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['marble'] = "render_marble.png"

    def _rock(self):
        node = cmds.shadingNode('rock', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['rock'] = "render_rock.png"

    def _snow(self):
        node = cmds.shadingNode('snow', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['snow'] = "render_snow.png"

    def _solidFractal(self):
        node = cmds.shadingNode('solidFractal', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['solidFractal'] = "render_solidFractal.png"

    def _stucco(self):
        node = cmds.shadingNode('stucco', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['stucco'] = "render_stucco.png"

    def _volumeNoise(self):
        node = cmds.shadingNode('volumeNoise', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['volumeNoise'] = "render_volumeNoise.png"

    def _wood(self):
        node = cmds.shadingNode('wood', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['wood'] = "render_wood.png"

    def _fluidTexture3D(self):
        node = cmds.shadingNode('fluidTexture3D', asTexture=True)
        cmds.connectAttr(
            "time1.outTime", node + ".currentTime")
    mayaNodeDict['fluidTexture3D'] = "render_fluidTexture3D.png"

    # env texture
    def _envBall(self):
        node = cmds.shadingNode('envBall', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['envBall'] = "render_envBall.png"

    def _envChrome(self):
        node = cmds.shadingNode('envChrome', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['envChrome'] = "render_envChrome.png"

    def _envCube(self):
        node = cmds.shadingNode('envCube', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['envCube'] = "render_envCube.png"

    def _envSky(self):
        node = cmds.shadingNode('envSky', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['envSky'] = "render_envSky.png"

    def _envSphere(self):
        node = cmds.shadingNode('envSphere', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    mayaNodeDict['envSphere'] = "render_envSphere.png"

    # other textures
    def _layeredTexture(self):
        cmds.shadingNode('layeredTexture', asTexture=True)
    mayaNodeDict['layeredTexture'] = "render_layeredTexture.png"

    # imagePlane
    def _imagePlane(self):
        cmds.shadingNode('imagePlane', asUtility=True)
    mayaNodeDict['imagePlane'] = "render_imagePlane.png"

    # glow
    def _opticalFX(self):
        cmds.shadingNode('opticalFX', asPostProcess=True)
    mayaNodeDict['opticalFX'] = "render_opticalFX.png"

    # 2D textures
    def _bulge(self):
        node = cmds.shadingNode('bulge', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 4)
        cmds.setAttr(tex + '.repeatV', 4)
    mayaNodeDict['bulge'] = "render_bulge.png"

    def _checker(self):
        node = cmds.shadingNode('checker', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 4)
        cmds.setAttr(tex + '.repeatV', 4)
    mayaNodeDict['checker'] = "render_checker.png"

    def _cloth(self):
        node = cmds.shadingNode('cloth', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 4)
        cmds.setAttr(tex + '.repeatV', 4)
    mayaNodeDict['cloth'] = "render_cloth.png"

    def _file(self):
        cmds.shadingNode('file', asTexture=True)
    mayaNodeDict['file'] = "render_file.png"

    def _fluidTexture2D(self):
        node = cmds.shadingNode('fluidTexture2D', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
    mayaNodeDict['fluidTexture2D'] = "render_fluidTexture2D.png"

    def _fractal(self):
        node = cmds.shadingNode('fractal', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    mayaNodeDict['fractal'] = "render_fractal.png"

    def _grid(self):
        node = cmds.shadingNode('grid', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 4)
        cmds.setAttr(tex + '.repeatV', 4)
    mayaNodeDict['grid'] = "render_grid.png"

    def _mandelbrot(self):
        node = cmds.shadingNode('mandelbrot', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
    mayaNodeDict['mandelbrot'] = "render_mandelbrot.png"

    def _mountain(self):
        node = cmds.shadingNode('mountain', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    mayaNodeDict['movie'] = "render_movie.png"

    def _movie(self):
        node = cmds.shadingNode('movie', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    mayaNodeDict['movie'] = "render_movie.png"

    def _noise(self):
        node = cmds.shadingNode('noise', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    mayaNodeDict['noise'] = "render_noise.png"

    def _ocean(self):
        node = cmds.shadingNode('ocean', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    mayaNodeDict['ocean'] = "render_ocean.png"

    def _psdFileTex(self):
        cmds.shadingNode('psdFileTex', asTexture=True)
    mayaNodeDict['psdFileTex'] = "render_psdFileTex.png"

    def _ramp(self):
        node = cmds.shadingNode('ramp', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    mayaNodeDict['ramp'] = "render_ramp.png"

    def _substance(self):
        node = cmds.shadingNode('substance', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    mayaNodeDict['substance'] = "commandButton.png"

    def _substanceOutput(self):
        node = cmds.shadingNode('substanceOutput', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    mayaNodeDict['substanceOutput'] = "commandButton.png"

    def _water(self):
        node = cmds.shadingNode('water', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    mayaNodeDict['water'] = "render_water.png"

    # #################### #
    # ###### LIGHTS ###### #
    # #################### #
    def _ambientLight(self):
        cmds.shadingNode('ambientLight', asLight=True)
    mayaNodeDict['ambientLight'] = "render_ambientLight.png"

    def _areaLight(self):
        cmds.shadingNode('areaLight', asLight=True)
    mayaNodeDict['areaLight'] = "render_areaLight.png"

    def _directionalLight(self):
        cmds.shadingNode('directionalLight', asLight=True)
    mayaNodeDict['directionalLight'] = "render_directionalLight.png"

    def _pointLight(self):
        cmds.shadingNode('pointLight', asLight=True)
    mayaNodeDict['pointLight'] = "render_pointLight.png"

    def _spotLight(self):
        cmds.shadingNode('spotLight', asLight=True)
    mayaNodeDict['spotLight'] = "render_spotLight.png"

    def _volumeLight(self):
        cmds.shadingNode('volumeLight', asLight=True)
    mayaNodeDict['volumeLight'] = "render_volumeLight.png"

    # #################### #
    # ###### CREATE ###### #
    # #################### #

    def _locator(self):
        cmds.spaceLocator(p=[0, 0, 0])
    mayaNodeDict['locator'] = "render_locator.png"

    def _camera(self):
        cmds.camera()
    mayaNodeDict['camera'] = "Camera.png"

    def _polyCube(self):
        cmds.polyCube()
    mayaNodeDict['polyCube'] = "polyCube.png"

    def _polySphere(self):
        cmds.polySphere()
    mayaNodeDict['polySphere'] = "polySphere.png"

    def _polyCylinder(self):
        cmds.polyCylinder()
    mayaNodeDict['polyCylinder'] = "polyCylinder.png"

    def _polyPlane(self):
        cmds.polyPlane()
    mayaNodeDict['polyPlane'] = "polyPlane.png"

    def _polyCone(self):
        cmds.polyCone()
    mayaNodeDict['polyCone'] = "polyCone.png"

    def _polyTorus(self):
        cmds.polyTorus()
    mayaNodeDict['polyTorus'] = "polyTorus.png"

    def _polyPrism(self):
        cmds.polyPrism()
    mayaNodeDict['polyPrism'] = "polyPrism.png"

    def _polyPyramid(self):
        cmds.polyPyramid()
    mayaNodeDict['polyPyramid'] = "polyPyramid.png"

    def _polyPipe(self):
        cmds.polyPipe()
    mayaNodeDict['polyPipe'] = "polyPipe.png"

    def _polyHelix(self):
        cmds.polyHelix()
    mayaNodeDict['polyHelix'] = "polyHelix.png"

    # ################## #
    # ######WINDOW###### #
    # ################## #
    def _preferencesWindow(self):
        cmds.PreferencesWindow()
    mayaNodeDict['preferencesWindow'] = "menuIconWindow.png"

    def _hotkeyEditor(self):
        cmds.HotkeyPreferencesWindow()
    mayaNodeDict['hotkeyEditor'] = "menuIconWindow.png"

    def _pluginManager(self):
        cmds.PluginManager()
    mayaNodeDict['pluginManager'] = "menuIconWindow.png"

    # general
    def _componentEditor(self):
        cmds.ComponentEditor()
    mayaNodeDict['componentEditor'] = "menuIconWindow.png"

    def _spreadSheetEditor(self):
        cmds.SpreadSheetEditor()
    mayaNodeDict['spreadSheetEditor'] = "menuIconWindow.png"

    def _connectionEditor(self):
        cmds.ConnectionEditor()
    mayaNodeDict['connectionEditor'] = "menuIconWindow.png"

    def _visorWindow(self):
        cmds.VisorWindow()
    mayaNodeDict['visorWindow'] = "menuIconWindow.png"

    def _displayLayerEditor(self):
        cmds.DisplayLayerEditorWindow()
    mayaNodeDict['displayLayerEditor'] = "menuIconWindow.png"

    def _assetEditor(self):
        cmds.AssetEditor()
    mayaNodeDict['assetEditor'] = "menuIconWindow.png"

    def _namespaceEditor(self):
        cmds.NamespaceEditor()
    mayaNodeDict['namespaceEditor'] = "menuIconWindow.png"

    def _filePathEditor(self):
        cmds.FilePathEditor()
    mayaNodeDict['filePathEditor'] = "menuIconWindow.png"

    def _blindDataEditor(self):
        cmds.BlindDataEditor()
    mayaNodeDict['blindDataEditor'] = "menuIconWindow.png"

    def _channelControlEditor(self):
        cmds.ChannelControlEditor()
    mayaNodeDict['channelControlEditor'] = "menuIconWindow.png"

    def _scriptEditor(self):
        cmds.ScriptEditor()
    mayaNodeDict['scriptEditor'] = "menuIconWindow.png"

    def _commandShell(self):
        cmds.CommandShell()
    mayaNodeDict['commandShell'] = "menuIconWindow.png"

    def _customStereoRigEditor(self):
        mel.eval(
            'stereoCameraCBwrapper(\
                "stereoRigToolEditor","customRigEditor()");')
    mayaNodeDict['customStereoRigEditor'] = "menuIconWindow.png"

    def _renderingFlags(self):
        cmds.RenderFlagsWindow()
    mayaNodeDict['renderingFlags'] = "menuIconWindow.png"

    # relationship eidots
    def _setsEditor(self):
        cmds.SetEditor()
    mayaNodeDict['setsEditor'] = "menuIconWindow.png"

    def _deformerSetEditor(self):
        cmds.DeformerSetEditor()
    mayaNodeDict['deformerSetEditor'] = "menuIconWindow.png"

    def _characterSetEditor(self):
        cmds.CharacterSetEditor()
    mayaNodeDict['characterSetEditor'] = "menuIconWindow.png"

    def _partitionEditor(self):
        cmds.PartitionEditor()
    mayaNodeDict['partitionEditor'] = "menuIconWindow.png"

    def _layerRelationshipEditor(self):
        cmds.LayerRelationshipEditor()
    mayaNodeDict['layerRelationshipEditor'] = "menuIconWindow.png"

    def _renderLayerRelationshipEditor(self):
        cmds.RenderLayerRelationshipEditor()
    mayaNodeDict['renderLayerRelationshipEditor'] = "menuIconWindow.png"

    def _cameraSetEditor(self):
        cmds.CameraSetEditor()
    mayaNodeDict['cameraSetEditor'] = "menuIconWindow.png"

    def _renderPassSetEditor(self):
        cmds.RenderPassSetEditor()
    mayaNodeDict['renderPassSetEditor'] = "menuIconWindow.png"

    def _animationLayerRelationshipEditor(self):
        cmds.AnimLayerRelationshipEditor()
    mayaNodeDict['animationLayerRelationshipEditor'] = "menuIconWindow.png"

    def _dynamicRelationshipEditor(self):
        cmds.DynamicRelationshipEditor()
    mayaNodeDict['dynamicRelationshipEditor'] = "menuIconWindow.png"

    def _lightCentricLightLinkingEditor(self):
        cmds.LightCentricLightLinkingEditor()
    mayaNodeDict['lightCentricLightLinkingEditor'] = "menuIconWindow.png"

    def _objectCentricLightLinkingEditor(self):
        cmds.ObjectCentricLightLinkingEditor()
    mayaNodeDict['objectCentricLightLinkingEditor'] = "menuIconWindow.png"

    def _textureCentricUVLinkingEditor(self):
        cmds.TextureCentricUVLinkingEditor()
    mayaNodeDict['textureCentricUVLinkingEditor'] = "menuIconWindow.png"

    def _uVCentricUVLinkingEditor(self):
        cmds.UVCentricUVLinkingEditor()
    mayaNodeDict['uVCentricUVLinkingEditor'] = "menuIconWindow.png"

    def _pFXUVSetLinkingEditor(self):
        cmds.PFXUVSetLinkingEditor()
    mayaNodeDict['pFXUVSetLinkingEditor'] = "menuIconWindow.png"

    def _hairUVSetLinkingEditor(self):
        cmds.HairUVSetLinkingEditor()
    mayaNodeDict['hairUVSetLinkingEditor'] = "menuIconWindow.png"

    # rendering
    def _renderViewWindow(self):
        cmds.RenderViewWindow()
    mayaNodeDict['renderViewWindow'] = "menuIconWindow.png"

    def _hyperShade(self):
        cmds.HypershadeWindow()
    mayaNodeDict['hyperShade'] = "menuIconWindow.png"

    def _mentalRayApproxEditor(self):
        cmds.MentalRayApproxEditor()
    mayaNodeDict['mentalRayApproxEditor'] = "menuIconWindow.png"

    def _mentalRayCustomTextEditor(self):
        cmds.MentalRayCustomTextEditor()
    mayaNodeDict['mentalRayCustomTextEditor'] = "menuIconWindow.png"

    def _mentalRayMapVisualizer(self):
        cmds.mrMapVisualizer()
    mayaNodeDict['mentalRayMapVisualizer'] = "menuIconWindow.png"

    def _mentalRayShaderManager(self):
        cmds.mrShaderManager()
    mayaNodeDict['mentalRayShaderManager'] = "menuIconWindow.png"

    # animation
    def _graphEditor(self):
        cmds.GraphEditor()
    mayaNodeDict['graphEditor'] = "menuIconWindow.png"

    def _traxEditor(self):
        cmds.CharacterAnimationEditor()
    mayaNodeDict['traxEditor'] = "menuIconWindow.png"

    def _cameraSequenceEditor(self):
        cmds.SequenceEditor()
    mayaNodeDict['cameraSequenceEditor'] = "menuIconWindow.png"

    def _dopeSheetEditor(self):
        cmds.DopeSheetEditor()
    mayaNodeDict['dopeSheetEditor'] = "menuIconWindow.png"

    def _humanIK(self):
        cmds.HIKCharacterControlsTool()
    mayaNodeDict['humanIK'] = "menuIconWindow.png"

    def _blendShapeEditor(self):
        cmds.BlendShapeEditor()
    mayaNodeDict['blendShapeEditor'] = "menuIconWindow.png"

    def _expressionEditor(self):
        cmds.ExpressionEditor()
    mayaNodeDict['expressionEditor'] = "menuIconWindow.png"
