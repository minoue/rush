# -*- coding: utf-8 -*-

import maya.cmds as cmds
import maya.mel as mel
import os
import json

current_dir = os.path.dirname(__file__)

commandDict = {}

iconPaths = os.environ["XBMLANGPATH"]

vrayIconPath = [i for i in iconPaths.split(":") if '/vray/icons' in i][0]
mentalrayIconPath = [i for i in iconPaths.split(":") if 'mentalray' in i][0]


class Commands(object):
    ################################
    # Maya Default Nodes
    ################################

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

    ####################
    # CREATE
    ####################
    def _locator(self):
        cmds.spaceLocator(p=[0, 0, 0])
    commandDict['locator'] = "render_locator.png"

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
    commandDict['locatorOnSelected'] = "render_locator.png"

    def _camera(self):
        cmds.camera()
    commandDict['camera'] = "Camera.png"

    # LIGHTS
    def _ambientLight(self):
        cmds.shadingNode('ambientLight', asLight=True)
    commandDict['ambientLight'] = "render_ambientLight.png"

    def _areaLight(self):
        cmds.shadingNode('areaLight', asLight=True)
    commandDict['areaLight'] = "render_areaLight.png"

    def _directionalLight(self):
        cmds.shadingNode('directionalLight', asLight=True)
    commandDict['directionalLight'] = "render_directionalLight.png"

    def _pointLight(self):
        cmds.shadingNode('pointLight', asLight=True)
    commandDict['pointLight'] = "render_pointLight.png"

    def _spotLight(self):
        cmds.shadingNode('spotLight', asLight=True)
    commandDict['spotLight'] = "render_spotLight.png"

    def _volumeLight(self):
        cmds.shadingNode('volumeLight', asLight=True)
    commandDict['volumeLight'] = "render_volumeLight.png"

    # Create Geometries
    def _polyCube(self):
        cmds.polyCube()
    commandDict['polyCube'] = "polyCube.png"

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
    commandDict['polyCubeOnSelected'] = "polyCube.png"

    def _polySphere(self):
        cmds.polySphere()
    commandDict['polySphere'] = "polySphere.png"

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
    commandDict['polySphereOnSelected'] = "polySphere.png"

    def _polyCylinder(self):
        cmds.polyCylinder()
    commandDict['polyCylinder'] = "polyCylinder.png"

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
    commandDict['polyCylinderOnSelected'] = "polyCylinder.png"

    def _polyPlane(self):
        cmds.polyPlane()
    commandDict['polyPlane'] = "polyPlane.png"

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
    commandDict['polyPlaneOnSelected'] = "polyPlane.png"

    def _polyCone(self):
        cmds.polyCone()
    commandDict['polyCone'] = "polyCone.png"

    def _polyTorus(self):
        cmds.polyTorus()
    commandDict['polyTorus'] = "polyTorus.png"

    def _polyPrism(self):
        cmds.polyPrism()
    commandDict['polyPrism'] = "polyPrism.png"

    def _polyPyramid(self):
        cmds.polyPyramid()
    commandDict['polyPyramid'] = "polyPyramid.png"

    def _polyPipe(self):
        cmds.polyPipe()
    commandDict['polyPipe'] = "polyPipe.png"

    def _polyHelix(self):
        cmds.polyHelix()
    commandDict['polyHelix'] = "polyHelix.png"

    ####################
    # WINDOW
    ####################
    def _preferencesWindow(self):
        cmds.PreferencesWindow()
    commandDict['preferencesWindow'] = "menuIconWindow.png"

    def _hotkeyEditor(self):
        cmds.HotkeyPreferencesWindow()
    commandDict['hotkeyEditor'] = "menuIconWindow.png"

    def _pluginManager(self):
        cmds.PluginManager()
    commandDict['pluginManager'] = "menuIconWindow.png"

    # general
    def _componentEditor(self):
        cmds.ComponentEditor()
    commandDict['componentEditor'] = "menuIconWindow.png"

    def _spreadSheetEditor(self):
        cmds.SpreadSheetEditor()
    commandDict['spreadSheetEditor'] = "menuIconWindow.png"

    def _connectionEditor(self):
        cmds.ConnectionEditor()
    commandDict['connectionEditor'] = "menuIconWindow.png"

    def _visorWindow(self):
        cmds.VisorWindow()
    commandDict['visorWindow'] = "menuIconWindow.png"

    def _displayLayerEditor(self):
        cmds.DisplayLayerEditorWindow()
    commandDict['displayLayerEditor'] = "menuIconWindow.png"

    def _assetEditor(self):
        cmds.AssetEditor()
    commandDict['assetEditor'] = "menuIconWindow.png"

    def _namespaceEditor(self):
        cmds.NamespaceEditor()
    commandDict['namespaceEditor'] = "menuIconWindow.png"

    def _filePathEditor(self):
        cmds.FilePathEditor()
    commandDict['filePathEditor'] = "menuIconWindow.png"

    def _blindDataEditor(self):
        cmds.BlindDataEditor()
    commandDict['blindDataEditor'] = "menuIconWindow.png"

    def _channelControlEditor(self):
        cmds.ChannelControlEditor()
    commandDict['channelControlEditor'] = "menuIconWindow.png"

    def _scriptEditor(self):
        cmds.ScriptEditor()
    commandDict['scriptEditor'] = "menuIconWindow.png"

    def _commandShell(self):
        cmds.CommandShell()
    commandDict['commandShell'] = "menuIconWindow.png"

    def _customStereoRigEditor(self):
        mel.eval(
            'stereoCameraCBwrapper(\
                "stereoRigToolEditor","customRigEditor()");')
    commandDict['customStereoRigEditor'] = "menuIconWindow.png"

    def _renderingFlags(self):
        cmds.RenderFlagsWindow()
    commandDict['renderingFlags'] = "menuIconWindow.png"

    # relationship eidots
    def _setsEditor(self):
        cmds.SetEditor()
    commandDict['setsEditor'] = "menuIconWindow.png"

    def _deformerSetEditor(self):
        cmds.DeformerSetEditor()
    commandDict['deformerSetEditor'] = "menuIconWindow.png"

    def _characterSetEditor(self):
        cmds.CharacterSetEditor()
    commandDict['characterSetEditor'] = "menuIconWindow.png"

    def _partitionEditor(self):
        cmds.PartitionEditor()
    commandDict['partitionEditor'] = "menuIconWindow.png"

    def _layerRelationshipEditor(self):
        cmds.LayerRelationshipEditor()
    commandDict['layerRelationshipEditor'] = "menuIconWindow.png"

    def _renderLayerRelationshipEditor(self):
        cmds.RenderLayerRelationshipEditor()
    commandDict['renderLayerRelationshipEditor'] = "menuIconWindow.png"

    def _cameraSetEditor(self):
        cmds.CameraSetEditor()
    commandDict['cameraSetEditor'] = "menuIconWindow.png"

    def _renderPassSetEditor(self):
        cmds.RenderPassSetEditor()
    commandDict['renderPassSetEditor'] = "menuIconWindow.png"

    def _animationLayerRelationshipEditor(self):
        cmds.AnimLayerRelationshipEditor()
    commandDict['animationLayerRelationshipEditor'] = "menuIconWindow.png"

    def _dynamicRelationshipEditor(self):
        cmds.DynamicRelationshipEditor()
    commandDict['dynamicRelationshipEditor'] = "menuIconWindow.png"

    def _lightCentricLightLinkingEditor(self):
        cmds.LightCentricLightLinkingEditor()
    commandDict['lightCentricLightLinkingEditor'] = "menuIconWindow.png"

    def _objectCentricLightLinkingEditor(self):
        cmds.ObjectCentricLightLinkingEditor()
    commandDict['objectCentricLightLinkingEditor'] = "menuIconWindow.png"

    def _textureCentricUVLinkingEditor(self):
        cmds.TextureCentricUVLinkingEditor()
    commandDict['textureCentricUVLinkingEditor'] = "menuIconWindow.png"

    def _uVCentricUVLinkingEditor(self):
        cmds.UVCentricUVLinkingEditor()
    commandDict['uVCentricUVLinkingEditor'] = "menuIconWindow.png"

    def _pFXUVSetLinkingEditor(self):
        cmds.PFXUVSetLinkingEditor()
    commandDict['pFXUVSetLinkingEditor'] = "menuIconWindow.png"

    def _hairUVSetLinkingEditor(self):
        cmds.HairUVSetLinkingEditor()
    commandDict['hairUVSetLinkingEditor'] = "menuIconWindow.png"

    # rendering
    def _renderViewWindow(self):
        cmds.RenderViewWindow()
    commandDict['renderViewWindow'] = "menuIconWindow.png"

    def _hyperShade(self):
        cmds.HypershadeWindow()
    commandDict['hyperShade'] = "menuIconWindow.png"

    def _mentalRayApproxEditor(self):
        cmds.MentalRayApproxEditor()
    commandDict['mentalRayApproxEditor'] = "menuIconWindow.png"

    def _mentalRayCustomTextEditor(self):
        cmds.MentalRayCustomTextEditor()
    commandDict['mentalRayCustomTextEditor'] = "menuIconWindow.png"

    def _mentalRayMapVisualizer(self):
        cmds.mrMapVisualizer()
    commandDict['mentalRayMapVisualizer'] = "menuIconWindow.png"

    def _mentalRayShaderManager(self):
        cmds.mrShaderManager()
    commandDict['mentalRayShaderManager'] = "menuIconWindow.png"

    # animation
    def _graphEditor(self):
        cmds.GraphEditor()
    commandDict['graphEditor'] = "menuIconWindow.png"

    def _traxEditor(self):
        cmds.CharacterAnimationEditor()
    commandDict['traxEditor'] = "menuIconWindow.png"

    def _cameraSequenceEditor(self):
        cmds.SequenceEditor()
    commandDict['cameraSequenceEditor'] = "menuIconWindow.png"

    def _dopeSheetEditor(self):
        cmds.DopeSheetEditor()
    commandDict['dopeSheetEditor'] = "menuIconWindow.png"

    def _humanIK(self):
        cmds.HIKCharacterControlsTool()
    commandDict['humanIK'] = "menuIconWindow.png"

    def _blendShapeEditor(self):
        cmds.BlendShapeEditor()
    commandDict['blendShapeEditor'] = "menuIconWindow.png"

    def _expressionEditor(self):
        cmds.ExpressionEditor()
    commandDict['expressionEditor'] = "menuIconWindow.png"

    #########################
    # Plugin Load
    #########################
    def _loadObjExport(self):
        if cmds.pluginInfo("objExport", q=True, l=True) == 0:
            mel.eval('loadPlugin objExport')
    commandDict['loadObjExport'] = "commandButton.png"

    def _loadFbx(self):
        if cmds.pluginInfo("fbxmaya", q=True, l=True) == 0:
            mel.eval('loadPlugin fbxmaya')
    commandDict['loadFbx'] = "commandButton.png"

    def _loadArnold(self):
        if cmds.pluginInfo("mtoa", q=True, l=True) == 0:
            mel.eval('loadPlugin mtoa')
    commandDict['loadArnold'] = "commandButton.png"

    def _loadRealflow(self):
        if cmds.pluginInfo("realflow", q=True, l=True) == 0:
            mel.eval('loadPlugin realflow')
    commandDict['loadRealflow'] = "commandButton.png"

    def _loadMentalray(self):
        if cmds.pluginInfo("Mayatomr", q=True, l=True) == 0:
            mel.eval('loadPlugin Mayatomr')
    commandDict['loadMentalray'] = "commandButton.png"

    def _loadSOuP(self):
        if cmds.pluginInfo("SOuP", q=True, l=True) == 0:
            mel.eval('loadPlugin SOuP')
    commandDict['loadSOuP'] = "commandButton.png"

    ##################
    # VRAY
    ##################
    def _VRayBlendMtl(self):
        cmds.shadingNode('VRayBlendMtl', asShader=True)
    # commandDict['VRayBlendMtl'] = "render_VRayBlendMtl.png"
    commandDict['VRayBlendMtl'] = "%s/render_VRayBlendMtl.png" % vrayIconPath

    def _VRayBumpMtl(self):
        cmds.shadingNode('VRayBumpMtl', asShader=True)
    commandDict['VRayBumpMtl'] = "%s/render_VRayBumpMtl.png" % vrayIconPath

    def _VRayCarPaintMtl(self):
        cmds.shadingNode('VRayCarPaintMtl', asShader=True)
    commandDict[
        'VRayCarPaintMtl'] = "%s/render_VRayCarPaintMtl.png" % vrayIconPath

    def _VRayFastSSS2(self):
        cmds.shadingNode('VRayFastSSS2', asShader=True)
    commandDict['VRayFastSSS2'] = "%s/render_VRayFastSSS2.png" % vrayIconPath

    def _VRayFlakesMtl(self):
        cmds.shadingNode('VRayFlakesMtl', asShader=True)
    commandDict['VRayFlakesMtl'] = "%s/render_VRayFlakesMtl.png" % vrayIconPath

    def _VRayLightMtl(self):
        cmds.shadingNode('VRayLightMtl', asShader=True)
    commandDict['VRayLightMtl'] = "%s/render_VRayLightMtl.png" % vrayIconPath

    def _VRayMeshMaterial(self):
        cmds.shadingNode('VRayMeshMaterial', asShader=True)
    commandDict[
        'VRayMeshMaterial'] = "%s/render_VRayMeshMaterial.png" % vrayIconPath

    def _VRayMtl(self):
        cmds.shadingNode('VRayMtl', asShader=True)
    commandDict['VRayMtl'] = "%s/render_VRayMtl.png" % vrayIconPath

    def _VRayMtl2Sided(self):
        cmds.shadingNode('VRayMtl2Sided', asShader=True)
    commandDict['VRayMtl2Sided'] = "%s/render_VRayMtl2Sided.png" % vrayIconPath

    def _VRayMtlHair2(self):
        cmds.shadingNode('VRayMtlHair2', asShader=True)
    commandDict['VRayMtlHair2'] = "%s/render_unknown.png" % vrayIconPath

    def _VRayMtlHair3(self):
        cmds.shadingNode('VRayMtlHair3', asShader=True)
    commandDict['VRayMtlHair3'] = "%s/render_unknown.png" % vrayIconPath

    def _VRayMtlWrapper(self):
        cmds.shadingNode('VRayMtlWrapper', asShader=True)
    commandDict[
        'VRayMtlWrapper'] = "%s/render_VRayMtlWrapper.png" % vrayIconPath

    def _VRayPluginNodeMtl(self):
        cmds.shadingNode('VRayPluginNodeMtl', asShader=True)
    commandDict[
        'VRayPluginNodeMtl'] = "%s/render_VRayPluginNodeTex.png" % vrayIconPath

    def _VRaySimbiont(self):
        cmds.shadingNode('VRaySimbiont', asShader=True)
    commandDict['VRaySimbiont'] = "%s/render_VRaySimbiont.png" % vrayIconPath

    def _VRayEnvironmentFog(self):
        cmds.shadingNode('VRayEnvironmentFog', asShader=True)
    commandDict[
        'VRayEnvironmentFog'] = ("%s"
                                 "/render_VRayEnvironmentFog.png"
                                 ) % vrayIconPath

    def _VRayScatterFog(self):
        cmds.shadingNode('VRayScatterFog', asShader=True)
    commandDict[
        'VRayScatterFog'] = "%s/render_VRayScatterFog.png" % vrayIconPath

    def _VRaySimpleFog(self):
        cmds.shadingNode('VRaySimpleFog', asShader=True)
    commandDict['VRaySimpleFog'] = "%s/render_VRaySimpleFog.png" % vrayIconPath

    def _VRaySphereFadeVolume(self):
        cmds.shadingNode('VRaySphereFadeVolume', asShader=True)
    commandDict[
        'VRaySphereFadeVolume'] = ("%s"
                                   "/render_VRaySphereFadeVolume.png"
                                   ) % vrayIconPath

    def _VRayDirt(self):
        node = cmds.shadingNode('VRayDirt', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    commandDict['VRayDirt'] = "%s/render_VRayDirt.png" % vrayIconPath

    def _VRayEdges(self):
        node = cmds.shadingNode('VRayEdges', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    commandDict['VRayEdges'] = "%s/render_VRayEdges.png" % vrayIconPath

    def _VRayFresnel(self):
        node = cmds.shadingNode('VRayFresnel', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    commandDict[
        'VRayFresnel'] = ("%s"
                          "/render_VRayFresnel.png"
                          ) % vrayIconPath

    def _VRayVertexColors(self):
        node = cmds.shadingNode('VRayVertexColors', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    commandDict[
        'VRayVertexColors'] = ("%s"
                               "/render_VRayVertexColors.png"
                               ) % vrayIconPath

    def _VRayWater(self):
        node = cmds.shadingNode('VRayWater', asTexture=True)
        tex = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(tex + '.outUV', node + '.uvCoord')
        cmds.connectAttr(tex + '.outUvFilterSize', node + '.uvFilterSize')
        cmds.setAttr(tex + '.repeatU', 1)
        cmds.setAttr(tex + '.repeatV', 1)
    commandDict[
        'VRayWater'] = ("%s"
                        "/render_VRayWater.png"
                        ) % vrayIconPath

    def _VRayParticleTex(self):
        node = cmds.shadingNode('VRayParticleTex', asTexture=True)
        tex = cmds.shadingNode('place3dTexture', asUtility=True)
        cmds.connectAttr(
            tex + '.worldInverseMatrix', node + '.placementMatrix')
    commandDict[
        'VRayParticleTex'] = ("%s"
                              "/render_VRayParticleTex.png"
                              ) % vrayIconPath

    def _VRaySky(self):
        cmds.shadingNode('VRaySky', asTexture=True)
    commandDict['VRaySky'] = "%s/render_VRaySky.png" % vrayIconPath

    def _VRayPtex(self):
        cmds.shadingNode('VRayPtex', asTexture=True)
    commandDict['VRayPtex'] = "%s/render_VRayPtex.png" % vrayIconPath

    def _VRayLightDomeShape(self):
        cmds.shadingNode('VRayLightDomeShape', asLight=True)
    commandDict[
        'VRayLightDomeShape'] = ("%s"
                                 "/render_VRayLightDomeShape.png"
                                 ) % vrayIconPath

    def _VRayLightIESShape(self):
        cmds.shadingNode('VRayLightIESShape', asLight=True)
    commandDict[
        'VRayLightIESShape'] = ("%s"
                                "/render_VRayLightIESShape.png"
                                ) % vrayIconPath

    def _VRayLightRectShape(self):
        cmds.shadingNode('VRayLightRectShape', asLight=True)
    commandDict[
        'VRayLightRectShape'] = ("%s"
                                 "/render_VRayLightRectShape.png"
                                 ) % vrayIconPath

    def _VRayLightSphereShape(self):
        cmds.shadingNode('VRayLightSphereShape', asLight=True)
    commandDict[
        'VRayLightSphereShape'] = ("%s"
                                   "/render_VRayLightSphereShape.png"
                                   ) % vrayIconPath

    def _VRaySunShape(self):
        cmds.shadingNode('VRaySunShape', asLight=True)
    commandDict[
        'VRaySunShape'] = "%s/render_VRaySunShape.png" % vrayIconPath

    def _VRayDistanceTex(self):
        cmds.shadingNode('VRayDistanceTex', asUtility=True)
    commandDict[
        'VRayDistanceTex'] = "%s/render_unknown.png" % vrayIconPath

    def _VRayFurSampler(self):
        cmds.shadingNode('VRayFurSampler', asUtility=True)
    commandDict[
        'VRayFurSampler'] = "%s/render_VRayFurSampler.png" % vrayIconPath

    def _VRayHairSampler(self):
        cmds.shadingNode('VRayHairSampler', asUtility=True)
    commandDict[
        'VRayHairSampler'] = "%s/render_VRayHairSampler.png" % vrayIconPath

    def _VRayObjectProperties(self):
        cmds.shadingNode('VRayObjectProperties', asUtility=True)
    commandDict[
        'VRayObjectProperties'] = "%s/render_unknown.png" % vrayIconPath

    def _VRayPlaceEnvTex(self):
        cmds.shadingNode('VRayPlaceEnvTex', asUtility=True)
    commandDict[
        'VRayPlaceEnvTex'] = "%s/render_VRayPlaceEnvTex.png" % vrayIconPath

    def _VRayRenderElementSet(self):
        cmds.shadingNode('VRayRenderElementSet', asUtility=True)
    commandDict[
        'VRayRenderElementSet'] = "%s/render_unknown.png" % vrayIconPath

    def _VRayShInfo(self):
        cmds.shadingNode('VRayShInfo', asUtility=True)
    commandDict['VRayShInfo'] = "%s/render_unknown.png" % vrayIconPath

    def _VRaySwitchTransform(self):
        cmds.shadingNode('VRaySwitchTransform', asUtility=True)
    commandDict[
        'VRaySwitchTransform'] = ("%s"
                                  "/render_VRaySwitchTransform.png"
                                  ) % vrayIconPath

    def _VRayUserColor(self):
        cmds.shadingNode('VRayUserColor', asUtility=True)
    commandDict[
        'VRayUserColor'] = "%s/render_unknown.png" % vrayIconPath

    def _VRayUserScalar(self):
        cmds.shadingNode('VRayUserScalar', asUtility=True)
    commandDict[
        'VRayUserScalar'] = "%s/render_unknown.png" % vrayIconPath

    ####################
    # ARNOLD
    ####################
    # Shader
    def _aiMeshLightMaterial(self):
        cmds.shadingNode('aiMeshLightMaterial', asShader=True)
    commandDict['aiMeshLightMaterial'] = "commandButton.png"

    def _aiAmbientOcclusion(self):
        cmds.shadingNode('aiAmbientOcclusion', asShader=True)
    commandDict['aiAmbientOcclusion'] = "commandButton.png"

    def _aiHair(self):
        cmds.shadingNode('aiHair', asShader=True)
    commandDict['aiHair'] = "commandButton.png"

    def _aiRaySwitch(self):
        cmds.shadingNode('aiRaySwitch', asShader=True)
    commandDict['aiRaySwitch'] = "commandButton.png"

    def _aiShadowCatcher(self):
        cmds.shadingNode('aiShadowCatcher', asShader=True)
    commandDict['aiShadowCatcher'] = "commandButton.png"

    def _aiSkin(self):
        cmds.shadingNode('aiSkin', asShader=True)
    commandDict['aiSkin'] = "commandButton.png"

    def _aiSkinSss(self):
        cmds.shadingNode('aiSkinSss', asShader=True)
    commandDict['aiSkinSss'] = "commandButton.png"

    def _aiStandard(self):
        cmds.shadingNode('aiStandard', asShader=True)
    commandDict['aiStandard'] = "commandButton.png"

    def _aiUtility(self):
        cmds.shadingNode('aiUtility', asShader=True)
    commandDict['aiUtility'] = "commandButton.png"

    def _aiWireframe(self):
        cmds.shadingNode('aiWireframe', asShader=True)
    commandDict['aiWireframe'] = "commandButton.png"

    def _aiBump2d(self):
        cmds.shadingNode('aiBump2d', asShader=True)
    commandDict['aiBump2d'] = "commandButton.png"

    def _aiBump3d(self):
        cmds.shadingNode('aiBump3d', asShader=True)
    commandDict['aiBump3d'] = "commandButton.png"

    def _aiMotionVector(self):
        cmds.shadingNode('aiMotionVector', asShader=True)
    commandDict['aiMotionVector'] = "commandButton.png"

    def _aiUserDataBool(self):
        cmds.shadingNode('aiUserDataBool', asShader=True)
    commandDict['aiUserDataBool'] = "commandButton.png"

    def _aiUserDataColor(self):
        cmds.shadingNode('aiUserDataColor', asShader=True)
    commandDict['aiUserDataColor'] = "commandButton.png"

    def _aiUserDataFloat(self):
        cmds.shadingNode('aiUserDataFloat', asShader=True)
    commandDict['aiUserDataFloat'] = "commandButton.png"

    def _aiUserDataInt(self):
        cmds.shadingNode('aiUserDataInt', asShader=True)
    commandDict['aiUserDataInt'] = "commandButton.png"

    def _aiUserDataPnt2(self):
        cmds.shadingNode('aiUserDataPnt2', asShader=True)
    commandDict['aiUserDataPnt2'] = "commandButton.png"

    def _aiUserDataString(self):
        cmds.shadingNode('aiUserDataString', asShader=True)
    commandDict['aiUserDataString'] = "commandButton.png"

    def _aiUserDataVector(self):
        cmds.shadingNode('aiUserDataVector', asShader=True)
    commandDict['aiUserDataVector'] = "commandButton.png"

    def _aiVolumeCollector(self):
        cmds.shadingNode('aiVolumeCollector', asShader=True)
    commandDict['aiVolumeCollector'] = "commandButton.png"

    def _aiWriteColor(self):
        cmds.shadingNode('aiWriteColor', asShader=True)
    commandDict['aiWriteColor'] = "commandButton.png"

    def _aiWriteFloat(self):
        cmds.shadingNode('aiWriteFloat', asShader=True)
    commandDict['aiWriteFloat'] = "commandButton.png"

    def _aiFog(self):
        cmds.shadingNode('aiFog', asShader=True)
    commandDict['aiFog'] = "commandButton.png"

    def _aiVolumeScattering(self):
        cmds.shadingNode('aiVolumeScattering', asShader=True)
    commandDict['aiVolumeScattering'] = "commandButton.png"

    # texture
    def _aiImage(self):
        cmds.shadingNode('aiImage', asTexture=True)
    commandDict['aiImage'] = "commandButton.png"

    def _aiNoise(self):
        cmds.shadingNode('aiNoise', asTexture=True)
    commandDict['aiNoise'] = "commandButton.png"

    def _aiPhysicalSky(self):
        cmds.shadingNode('aiPhysicalSky', asTexture=True)
    commandDict['aiPhysicalSky'] = "commandButton.png"

    def _aiSky(self):
        cmds.shadingNode('aiSky', asTexture=True)
    commandDict['aiSky'] = "commandButton.png"

    # Light
    def _aiAreaLight(self):
        cmds.shadingNode('aiAreaLight', asLight=True)
    commandDict['aiAreaLight'] = "commandButton.png"

    def _aiPhotometricLight(self):
        cmds.shadingNode('aiPhotometricLight', asLight=True)
    commandDict['aiPhotometricLight'] = "commandButton.png"

    def _aiSkyDomeLight(self):
        cmds.shadingNode('aiSkyDomeLight', asLight=True)
    commandDict['aiSkyDomeLight'] = "commandButton.png"

    def _aiBarndoor(self):
        cmds.shadingNode('aiBarndoor', asLight=True)
    commandDict['aiBarndoor'] = "commandButton.png"

    def _aiGobo(self):
        cmds.shadingNode('aiGobo', asLight=True)
    commandDict['aiGobo'] = "commandButton.png"

    def _aiLightBlocker(self):
        cmds.shadingNode('aiLightBlocker', asLight=True)
    commandDict['aiLightBlocker'] = "commandButton.png"

    def _aiLightDecay(self):
        cmds.shadingNode('aiLightDecay', asLight=True)
    commandDict['aiLightDecay'] = "commandButton.png"

    ####################
    # MENTAL RAY
    ####################
    def _mi_car_paint_phen_x(self):
        cmds.shadingNode('mi_car_paint_phen_x', asShader=True)
    commandDict[
        'mi_car_paint_phen_x'] = ("%s"
                                  "/render_mi_car_paint_phen_x.png"
                                  ) % mentalrayIconPath

    def _mi_car_paint_phen_x_passes(self):
        cmds.shadingNode('mi_car_paint_phen_x_passes', asShader=True)
    commandDict[
        'mi_car_paint_phen_x_passes'] = ("%s"
                                         "/render_mi_car"
                                         "_paint_phen_x_passes.png"
                                         ) % mentalrayIconPath

    def _mi_metallic_paint_x(self):
        cmds.shadingNode('mi_metallic_paint_x', asShader=True)
    commandDict[
        'mi_metallic_paint_x'] = ("%s"
                                  "/render_mi_metallic_paint_x.png"
                                  ) % mentalrayIconPath

    def _mi_metallic_paint_x_passes(self):
        cmds.shadingNode('mi_metallic_paint_x_passes', asShader=True)
    commandDict[
        'mi_metallic_paint_x_passes'] = ("%s"
                                         "/render_mi_metallic"
                                         "_paint_x_passes.png"
                                         ) % mentalrayIconPath

    def _mia_material_x(self):
        cmds.shadingNode('mia_material_x', asShader=True)
    commandDict[
        'mia_material_x'] = ("%s"
                             "/render_mia_material_x.png"
                             ) % mentalrayIconPath

    def _mia_material_x_passes(self):
        cmds.shadingNode('mia_material_x_passes', asShader=True)
    commandDict[
        'mia_material_x_passes'] = ("%s"
                                    "/render_mia_material_x_passes.png"
                                    ) % mentalrayIconPath

    def _mib_illum_hair(self):
        cmds.shadingNode('mib_illum_hair', asShader=True)
    commandDict[
        'mib_illum_hair'] = ("%s"
                             "/render_mib_illum_hair.png"
                             ) % mentalrayIconPath

    def _mib_illum_hair_x(self):
        cmds.shadingNode('mib_illum_hair_x', asShader=True)
    commandDict[
        'mib_illum_hair_x'] = ("%s"
                               "/render_mib_illum_hair.png"
                               ) % mentalrayIconPath

    def _mib_ptex_lookup(self):
        cmds.shadingNode('mib_ptex_lookup', asShader=True)
    commandDict['mib_ptex_lookup'] = "render_unknown.png"

    def _mila_material(self):
        cmds.shadingNode('mila_material', asShader=True)
    commandDict['mila_material'] = "render_unknown.png"

    def _misss_fast_shader2_x(self):
        cmds.shadingNode('misss_fast_shader2_x', asShader=True)
    commandDict['misss_fast_shader2_x'] = "render_unknown.png"

    def _misss_fast_shader_x(self):
        node = cmds.shadingNode('misss_fast_shader_x', asShader=True)
        tex = cmds.shadingNode('mentalrayTexture', asTexture=True)
        cmds.expression(
            string="%s.miWidth  = defaultResolution.width * 2" % tex)
        cmds.expression(string="%s.miHeight = defaultResolution.height" % tex)
        cmds.setAttr(tex + ".miWritable", 1)
        cmds.setAttr(tex + ".miDepth", 4)
        lmap = cmds.shadingNode('misss_fast_lmap_maya', asUtility=True)
        cmds.connectAttr(tex + '.message', node + '.lightmap')
        cmds.connectAttr(tex + '.message', lmap + '.lightmap')
    commandDict[
        'misss_fast_shader_x'] = ("%s"
                                  "/render_misss_fast_shader_x.png"
                                  ) % mentalrayIconPath

    def _misss_fast_shader_x_passes(self):
        node = cmds.shadingNode('misss_fast_shader_x_passes', asShader=True)
        tex = cmds.shadingNode('mentalrayTexture', asTexture=True)
        cmds.expression(
            string="%s.miWidth  = defaultResolution.width * 2" % tex)
        cmds.expression(string="%s.miHeight = defaultResolution.height" % tex)
        cmds.setAttr(tex + ".miWritable", 1)
        cmds.setAttr(tex + ".miDepth", 4)
        lmap = cmds.shadingNode('misss_fast_lmap_maya', asUtility=True)
        cmds.connectAttr(tex + '.message', node + '.lightmap')
        cmds.connectAttr(tex + '.message', lmap + '.lightmap')
    commandDict[
        'misss_fast_shader_x_passes'] = ("%s"
                                         "/render_misss_fast"
                                         "_shader_x_passes.png"
                                         ) % mentalrayIconPath

    def _misss_fast_simple_maya(self):
        node = cmds.shadingNode('misss_fast_simple_maya', asShader=True)
        tex = cmds.shadingNode('mentalrayTexture', asTexture=True)
        cmds.expression(
            string="%s.miWidth  = defaultResolution.width * 2" % tex)
        cmds.expression(string="%s.miHeight = defaultResolution.height" % tex)
        cmds.setAttr(tex + ".miWritable", 1)
        cmds.setAttr(tex + ".miDepth", 4)
        lmap = cmds.shadingNode('misss_fast_lmap_maya', asUtility=True)
        cmds.connectAttr(tex + '.message', node + '.lightmap')
        cmds.connectAttr(tex + '.message', lmap + '.lightmap')
    commandDict[
        'misss_fast_simple_maya'] = ("%s"
                                     "/render_misss_fast_simple_maya.png"
                                     ) % mentalrayIconPath

    def _misss_fast_skin_maya(self):
        node = cmds.shadingNode('misss_fast_skin_maya', asShader=True)
        tex = cmds.shadingNode('mentalrayTexture', asTexture=True)
        cmds.expression(
            string="%s.miWidth  = defaultResolution.width * 2" % tex)
        cmds.expression(string="%s.miHeight = defaultResolution.height" % tex)
        cmds.setAttr(tex + ".miWritable", 1)
        cmds.setAttr(tex + ".miDepth", 4)
        lmap = cmds.shadingNode('misss_fast_lmap_maya', asUtility=True)
        cmds.connectAttr(tex + '.message', node + '.lightmap')
        cmds.connectAttr(tex + '.message', lmap + '.lightmap')
    commandDict[
        'misss_fast_skin_maya'] = ("%s"
                                   "/render_misss_fast_skin_maya.png"
                                   ) % mentalrayIconPath

    ###################
    # OTHER
    ###################
    def _importObj(self):
        if cmds.pluginInfo("objExport", q=True, l=True) == 0:
            mel.eval('loadPlugin objExport')
        basicFilter = "OBJ(*.obj)"  # "*All(*.*);;OBJ(*.obj)"
        returnPath = cmds.fileDialog2(
            fileFilter=basicFilter, ds=2, cc="CANCEL", okc="IMPORT")[0]
        cmds.file(returnPath,
                  i=True,
                  mergeNamespacesOnClash=False,
                  type='OBJ',
                  ra=True,
                  pr=True)
    commandDict['importObj'] = "pythonFamily.png"

    def _renderThumbnailUpdate(self):
        if cmds.renderThumbnailUpdate(q=True):
            mel.eval("renderThumbnailUpdate 0")
        else:
            mel.eval("renderThumbnailUpdate 1")
    commandDict['renderThumbnailUpdate'] = "pythonFamily.png"

    ##################
    # MENU
    ##################
    def _reGenerateCommands(self):
        outFilePath = os.path.normpath(
            os.path.join(current_dir, "commands.json"))

        with open(outFilePath, 'w') as outFile:
            json.dump(commandDict,
                      outFile,
                      indent=4,
                      separators=(',', ':'),
                      sort_keys=True)
        print "command file updated"

    commandDict['reGenerateCommands'] = "pythonFamily.png"
