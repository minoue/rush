import maya.cmds as cmds


class Commands(object):

    commandDict = {}

    # ################################ #
    # ###### Maya Default Nodes ###### #
    # ################################ #

    # Surface

    def _ShaderfxShader(self):
        cmds.shadingNode('ShaderfxShader', asShader=True)
    commandDict['blinn'] = "render_blinn.png"

    def _blinn(self):
        cmds.shadingNode('blinn', asShader=True)
    commandDict['blinn'] = "render_blinn.png"

    def _anisotropic(self):
        cmds.shadingNode('anisotropic', asShader=True)
    commandDict['anisotropic'] = "render_anisotropic.png"

    def _bifrostLiquidMaterial(self):
        cmds.shadingNode('bifrostLiquidMaterial', asShader=True)
    commandDict['bifrostLiquidMaterial'] = "render_blinn.png"

    def _hairTubeShader(self):
        cmds.shadingNode('hairTubeShader', asShader=True)
    commandDict['hairTubeShader'] = "render_hairTubeShader.png"

    def _lambert(self):
        cmds.shadingNode('lambert', asShader=True)
    commandDict['lambert'] = "render_lambert.png"

    def _layeredShader(self):
        cmds.shadingNode('layeredShader', asShader=True)
    commandDict['layeredShader'] = "render_layeredShader.png"

    def _oceanShader(self):
        node = cmds.shadingNode('oceanShader', asTexture=True)
        cmds.connectAttr("time1.outTime", node + ".time")
    commandDict['oceanShader'] = "render_oceanShader.png"

    def _phong(self):
        cmds.shadingNode('phong', asShader=True)
    commandDict['phong'] = "render_phong.png"

    def _phongE(self):
        cmds.shadingNode('phongE', asShader=True)
    commandDict['phongE'] = "render_phongE.png"

    def _rampShader(self):
        cmds.shadingNode('rampShader', asShader=True)
    commandDict['rampShader'] = "render_ramp.png"

    def _shadingMap(self):
        cmds.shadingNode('shadingMap', asShader=True)
    commandDict['shadingMap'] = "render_shadingMap.png"

    def _surfaceShader(self):
        cmds.shadingNode('surfaceShader', asShader=True)
    commandDict['surfaceShader'] = "render_surfaceShader.png"

    def _useBackground(self):
        cmds.shadingNode('useBackground', asShader=True)
    commandDict['useBackground'] = "render_useBackground.png"

    # vlumetric

    def _envFog(self):
        node = cmds.shadingNode('envFog', asShader=True)
        shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                                empty=True, name=node + "SG")
        cmds.connectAttr(
            node + '.outColor', shaderGroup + '.volumeShader', force=True)
    commandDict['envFog'] = "render_envFog.png"

    def _fluidShape(self):
        node = cmds.shadingNode('fluidShape', asShader=True)
        shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                                empty=True, name=node + "SG")
        cmds.connectAttr(
            node + '.outColor', shaderGroup + '.volumeShader', force=True)
        cmds.connectAttr("time1.outTime", node + ".currentTime")
    commandDict['fluidShape'] = "render_fluidShape.png"

    def _lightFog(self):
        node = cmds.shadingNode('lightFog', asShader=True)
        shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                                empty=True, name=node + "SG")
        cmds.connectAttr(
            node + '.outColor', shaderGroup + '.volumeShader', force=True)
    commandDict['lightFog'] = "render_lightFog.png"

    def _particleCloud(self):
        node = cmds.shadingNode('particleCloud', asShader=True)
        shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                                empty=True, name=node + "SG")
        cmds.connectAttr(
            node + '.outColor', shaderGroup + '.volumeShader', force=True)
    commandDict['particleCloud'] = "render_particleCloud.png"

    def _volumeFog(self):
        node = cmds.shadingNode('volumeFog', asShader=True)
        shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                                empty=True, name=node + "SG")
        cmds.connectAttr(
            node + '.outColor', shaderGroup + '.volumeShader', force=True)
    commandDict['volumeFog'] = "render_volumeFog.png"

    def _volumeShader(self):
        node = cmds.shadingNode('volumeShader', asShader=True)
        shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                                empty=True, name=node + "SG")
        cmds.connectAttr(
            node + '.outColor', shaderGroup + '.volumeShader', force=True)
    commandDict['volumeShader'] = "render_volumeShader.png"

    # Displacement

    def _cMuscleShader(self):
        node = cmds.shadingNode('cMuscleShader', asShader=True)
        shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                                empty=True, name=node + "SG")
        cmds.connectAttr(
            node + '.outColor',
            shaderGroup + '.displacementShader',
            force=True)
    commandDict['volumeShader'] = "sphere.png"

    def _displacementShader(self):
        node = cmds.shadingNode('displacementShader', asShader=True)
        shaderGroup = cmds.sets(renderable=True, noSurfaceShader=True,
                                empty=True, name=node + "SG")
        cmds.connectAttr(
            node + '.displacement',
            shaderGroup + '.displacementShader',
            force=True)
    commandDict['displacementShader'] = "render_displacementShader.png"

    # Utilities

    def _addDoubleLinear(self):
        cmds.shadingNode('addDoubleLinear', asUtility=True)
    commandDict['addDoubleLinear'] = "render_addDoubleLinear.png"

    def _addMatrix(self):
        cmds.shadingNode('addMatrix', asUtility=True)
    commandDict['addMatrix'] = "render_addMatrix.png"

    def _angleBetween(self):
        cmds.shadingNode('angleBetween', asUtility=True)
    commandDict['angleBetween'] = "render_angleBetween.png"

    def _arrayMapper(self):
        cmds.shadingNode('arrayMapper', asUtility=True)
    commandDict['arrayMapper'] = "render_arrayMapper.png"

    def _blendColors(self):
        cmds.shadingNode('blendColors', asUtility=True)
    commandDict['blendColors'] = "render_blendColors.png"

    def _blendTwoAttr(self):
        cmds.shadingNode('blendTwoAttr', asUtility=True)
    commandDict['blendTwoAttr'] = "render_blendTwoAttr.png"

    def _bump2d(self):
        cmds.shadingNode('bump2d', asUtility=True)
    commandDict['bump2d'] = "render_bump2d.png"

    def _bump3d(self):
        cmds.shadingNode('bump3d', asUtility=True)
    commandDict['bump3d'] = "render_bump3d.png"

    def _choice(self):
        cmds.shadingNode('choice', asUtility=True)
    commandDict['choice'] = "render_choice.png"

    def _chooser(self):
        cmds.shadingNode('chooser', asUtility=True)
    commandDict['chooser'] = "render_chooser.png"

    def _clamp(self):
        cmds.shadingNode('clamp', asUtility=True)
    commandDict['clamp'] = "render_clamp.png"

    def _colorProfile(self):
        cmds.shadingNode('colorProfile', asUtility=True)
    commandDict['colorProfile'] = "render_colorProfile.png"

    def _composeMatrix(self):
        cmds.shadingNode('composeMatrix', asUtility=True)
    commandDict['addMatrix'] = "render_addMatrix.png"

    def _condition(self):
        cmds.shadingNode('condition', asUtility=True)
    commandDict['condition'] = "render_condition.png"

    def _contrast(self):
        cmds.shadingNode('contrast', asUtility=True)
    commandDict['contrast'] = "render_contrast.png"

    def _curveInfo(self):
        cmds.shadingNode('curveInfo', asUtility=True)
    commandDict['curveInfo'] = "render_curveInfo.png"

    def _decomposeMatrix(self):
        cmds.shadingNode('decomposeMatrix', asUtility=True)
    commandDict['decomposeMatrix'] = "render_decomposeMatrix.png"

    def _distanceBetween(self):
        cmds.shadingNode('distanceBetween', asUtility=True)
    commandDict['distanceBetween'] = "render_distanceDimShape.png"

    def _doubleShadingSwitch(self):
        cmds.shadingNode('doubleShadingSwitch', asUtility=True)
    commandDict['doubleShadingSwitch'] = "render_doubleShadingSwitch.png"

    def _frameCache(self):
        cmds.shadingNode('frameCache', asUtility=True)
    commandDict['doubleShadingSwitch'] = ""

    def _gammaCorrect(self):
        cmds.shadingNode('gammaCorrect', asUtility=True)
    commandDict['gammaCorrect'] = "render_gammaCorrect.png"

    def _heightField(self):
        cmds.shadingNode('heightField', asUtility=True)
    commandDict['heightField'] = "render_heightField.png"

    def _hsvToRgb(self):
        cmds.shadingNode('hsvToRgb', asUtility=True)
    commandDict['hsvToRgb'] = "render_hsvToRgb.png"

    def _inverseMatrix(self):
        cmds.shadingNode('inverseMatrix', asUtility=True)
    commandDict['inverseMatrix'] = "render_addMatrix.png"

    def _lightInfo(self):
        cmds.shadingNode('lightInfo', asUtility=True)
    commandDict['lightInfo'] = "render_lightInfo.png"

    def _luminance(self):
        cmds.shadingNode('luminance', asUtility=True)
    commandDict['luminance'] = "render_luminance.png"

    def _multDoubleLinear(self):
        cmds.shadingNode('multDoubleLinear', asUtility=True)
    commandDict['multDoubleLinear'] = "render_multDoubleLinear.png"

    def _multiplyDivide(self):
        cmds.shadingNode('multiplyDivide', asUtility=True)
    commandDict['multiplyDivide'] = "render_multiplyDivide.png"

    def _particleSamplerInfo(self):
        cmds.shadingNode('particleSamplerInfo', asUtility=True)
    commandDict['particleSamplerInfo'] = "render_particleSamplerInfo.png"

    def _place2dTexture(self):
        cmds.shadingNode('place2dTexture', asUtility=True)
    commandDict['place2dTexture'] = "render_place2dTexture.png"

    def _place3dTexture(self):
        cmds.shadingNode('place3dTexture', asUtility=True)
    commandDict['place3dTexture'] = "render_place3dTexture.png"

    def _plusMinusAverage(self):
        cmds.shadingNode('plusMinusAverage', asUtility=True)
    commandDict['plusMinusAverage'] = "render_plusMinusAverage.png"

    def _projection(self):
        cmds.shadingNode('projection', asUtility=True)
    commandDict['projection'] = "render_projection.png"

    def _quadShadingSwitch(self):
        cmds.shadingNode('quadShadingSwitch', asUtility=True)
    commandDict['quadShadingSwitch'] = "render_quadShadingSwitch.png"

    def _remapColor(self):
        cmds.shadingNode('remapColor', asUtility=True)
    commandDict['remapColor'] = "render_remapColor.png"

    def _remapHsv(self):
        cmds.shadingNode('remapHsv', asUtility=True)
    commandDict['remapHsv'] = "render_remapHsv.png"

    def _remapValue(self):
        cmds.shadingNode('remapValue', asUtility=True)
    commandDict['remapValue'] = "render_remapValue.png"

    def _reverse(self):
        cmds.shadingNode('reverse', asUtility=True)
    commandDict['reverse'] = "render_reverse.png"

    def _rgbToHsv(self):
        cmds.shadingNode('rgbToHsv', asUtility=True)
    commandDict['rgbToHsv'] = "render_rgbToHsv.png"

    def _samplerInfo(self):
        cmds.shadingNode('samplerInfo', asUtility=True)
    commandDict['samplerInfo'] = "render_samplerInfo.png"

    def _setRange(self):
        cmds.shadingNode('setRange', asUtility=True)
    commandDict['setRange'] = "render_setRange.png"

    def _singleShadingSwitch(self):
        cmds.shadingNode('singleShadingSwitch', asUtility=True)
    commandDict['singleShadingSwitch'] = "render_singleShadingSwitch.png"

    def _stencil(self):
        cmds.shadingNode('stencil', asUtility=True)
    commandDict['stencil'] = "render_stencil.png"

    def _surfaceInfo(self):
        cmds.shadingNode('surfaceInfo', asUtility=True)
    commandDict['surfaceInfo'] = "render_surfaceInfo.png"

    def _surfaceLuminance(self):
        cmds.shadingNode('surfaceLuminance', asUtility=True)
    commandDict['surfaceLuminance'] = "render_surfaceLuminance.png"

    def _transposeMatrix(self):
        cmds.shadingNode('transposeMatrix', asUtility=True)
    commandDict['transposeMatrix'] = "render_addMatrix.png"

    def _tripleShadingSwitch(self):
        cmds.shadingNode('tripleShadingSwitch', asUtility=True)
    commandDict['tripleShadingSwitch'] = "render_tripleShadingSwitch.png"

    def _unitConversion(self):
        cmds.shadingNode('unitConversion', asUtility=True)
    commandDict['unitConversion'] = "render_unitConversion.png"

    def _uvChooser(self):
        cmds.shadingNode('uvChooser', asUtility=True)
    commandDict['uvChooser'] = "render_uvChooser.png"

    def _vectorProduct(self):
        cmds.shadingNode('vectorProduct', asUtility=True)
    commandDict['vectorProduct'] = "render_vectorProduct.png"

    # 3d texture
    def _brownian(self):
        node = cmds.shadingNode('brownian', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['brownian'] = "render_brownian.png"

    def _cloud(self):
        node = cmds.shadingNode('cloud', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['cloud'] = "render_cloud.png"

    def _crater(self):
        node = cmds.shadingNode('crater', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['crater'] = "render_crater.png"

    def _granite(self):
        node = cmds.shadingNode('granite', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['granite'] = "render_granite.png"

    def _leather(self):
        node = cmds.shadingNode('leather', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['leather'] = "render_leather.png"

    def _mandelbrot3D(self):
        node = cmds.shadingNode('mandelbrot3D', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['mandelbrot3D'] = "render_mandelbrot3D.png"

    def _marble(self):
        node = cmds.shadingNode('marble', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['marble'] = "render_marble.png"

    def _rock(self):
        node = cmds.shadingNode('rock', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['rock'] = "render_rock.png"

    def _snow(self):
        node = cmds.shadingNode('snow', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['snow'] = "render_snow.png"

    def _solidFractal(self):
        node = cmds.shadingNode('solidFractal', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['solidFractal'] = "render_solidFractal.png"

    def _stucco(self):
        node = cmds.shadingNode('stucco', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['stucco'] = "render_stucco.png"

    def _volumeNoise(self):
        node = cmds.shadingNode('volumeNoise', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['volumeNoise'] = "render_volumeNoise.png"

    def _wood(self):
        node = cmds.shadingNode('wood', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['wood'] = "render_wood.png"

    def _fluidTexture3D(self):
        node = cmds.shadingNode('fluidTexture3D', asTexture=True)
        cmds.connectAttr(
            "time1.outTime", node + ".currentTime")
    commandDict['fluidTexture3D'] = "render_fluidTexture3D.png"

    # env texture
    def _envBall(self):
        node = cmds.shadingNode('envBall', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['envBall'] = "render_envBall.png"

    def _envChrome(self):
        node = cmds.shadingNode('envChrome', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['envChrome'] = "render_envChrome.png"

    def _envCube(self):
        node = cmds.shadingNode('envCube', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['envCube'] = "render_envCube.png"

    def _envSky(self):
        node = cmds.shadingNode('envSky', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['envSky'] = "render_envSky.png"

    def _envSphere(self):
        node = cmds.shadingNode('envSphere', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict['envSphere'] = "render_envSphere.png"

    # other textures
    def _layeredTexture(self):
        cmds.shadingNode('layeredTexture', asTexture=True)
    commandDict['layeredTexture'] = "render_layeredTexture.png"

    # imagePlane
    def _imagePlane(self):
        cmds.shadingNode('imagePlane', asUtility=True)
    commandDict['imagePlane'] = "render_imagePlane.png"

    # glow
    def _opticalFX(self):
        cmds.shadingNode('opticalFX', asPostProcess=True)
    commandDict['opticalFX'] = "render_opticalFX.png"

    # 2D textures
    def _bulge(self):
        node = cmds.shadingNode('bulge', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 4)
        cmds.setAttr(tex + '.repeatV', 4)
    commandDict['bulge'] = "render_bulge.png"

    def _checker(self):
        node = cmds.shadingNode('checker', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 4)
        cmds.setAttr(tex + '.repeatV', 4)
    commandDict['checker'] = "render_checker.png"

    def _cloth(self):
        node = cmds.shadingNode('cloth', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 4)
        cmds.setAttr(tex + '.repeatV', 4)
    commandDict['cloth'] = "render_cloth.png"

    def _file(self):
        cmds.shadingNode('file', asTexture=True)
    commandDict['file'] = "render_file.png"

    def _fluidTexture2D(self):
        node = cmds.shadingNode('fluidTexture2D', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
    commandDict['fluidTexture2D'] = "render_fluidTexture2D.png"

    def _fractal(self):
        node = cmds.shadingNode('fractal', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    commandDict['fractal'] = "render_fractal.png"

    def _grid(self):
        node = cmds.shadingNode('grid', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 4)
        cmds.setAttr(tex + '.repeatV', 4)
    commandDict['grid'] = "render_grid.png"

    def _mandelbrot(self):
        node = cmds.shadingNode('mandelbrot', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
    commandDict['mandelbrot'] = "render_mandelbrot.png"

    def _mountain(self):
        node = cmds.shadingNode('mountain', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    commandDict['movie'] = "render_movie.png"

    def _movie(self):
        node = cmds.shadingNode('movie', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    commandDict['movie'] = "render_movie.png"

    def _noise(self):
        node = cmds.shadingNode('noise', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    commandDict['noise'] = "render_noise.png"

    def _ocean(self):
        node = cmds.shadingNode('ocean', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    commandDict['ocean'] = "render_ocean.png"

    def _psdFileTex(self):
        cmds.shadingNode('psdFileTex', asTexture=True)
    commandDict['psdFileTex'] = "render_psdFileTex.png"

    def _ramp(self):
        node = cmds.shadingNode('ramp', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    commandDict['ramp'] = "render_ramp.png"

    def _substance(self):
        node = cmds.shadingNode('substance', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    commandDict['substance'] = "commandButton.png"

    def _substanceOutput(self):
        node = cmds.shadingNode('substanceOutput', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    commandDict['substanceOutput'] = "commandButton.png"

    def _water(self):
        node = cmds.shadingNode('water', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    commandDict['water'] = "render_water.png"
