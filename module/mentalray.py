import maya.cmds as cmds
import os
import sys

iconPaths = os.environ['XBMLANGPATH']
try:
    if sys.platform == "linux2":
        for path in iconPaths.split(":"):
            if 'mentalray/icons' in path:
                iconPath = path
    elif sys.platform == "darwin":
        for path in iconPaths.split(":"):
            if 'mentalray/icons' in path:
                iconPath = path
    elif sys.platform == "win32":
        for path in iconPaths.split(";"):
            if '/mentalray/icons' in path:
                iconPath = path
    else:
        iconPath = ""
except NameError:
    iconPath = ""

# iconPath = r"C:\Program Files\Autodesk\Maya2013\mentalray\icons"


class Commands(object):

    mentalrayDict = {}

    def __init__(self):
        pass

    ####################
    # MENTAL RAY
    ####################
    def _mi_car_paint_phen_x(self):
        cmds.shadingNode('mi_car_paint_phen_x', asShader=True)
    mentalrayDict[
        'mi_car_paint_phen_x'] = ("%s"
                                  "/render_mi_car_paint_phen_x.png"
                                  ) % iconPath

    def _mi_car_paint_phen_x_passes(self):
        cmds.shadingNode('mi_car_paint_phen_x_passes', asShader=True)
    mentalrayDict[
        'mi_car_paint_phen_x_passes'] = ("%s"
                                         "/render_mi_car"
                                         "_paint_phen_x_passes.png"
                                         ) % iconPath

    def _mi_metallic_paint_x(self):
        cmds.shadingNode('mi_metallic_paint_x', asShader=True)
    mentalrayDict[
        'mi_metallic_paint_x'] = ("%s"
                                  "/render_mi_metallic_paint_x.png"
                                  ) % iconPath

    def _mi_metallic_paint_x_passes(self):
        cmds.shadingNode('mi_metallic_paint_x_passes', asShader=True)
    mentalrayDict[
        'mi_metallic_paint_x_passes'] = ("%s"
                                         "/render_mi_metallic"
                                         "_paint_x_passes.png"
                                         ) % iconPath

    def _mia_material_x(self):
        cmds.shadingNode('mia_material_x', asShader=True)
    mentalrayDict[
        'mia_material_x'] = ("%s"
                             "/render_mia_material_x.png"
                             ) % iconPath

    def _mia_material_x_passes(self):
        cmds.shadingNode('mia_material_x_passes', asShader=True)
    mentalrayDict[
        'mia_material_x_passes'] = ("%s"
                                    "/render_mia_material_x_passes.png"
                                    ) % iconPath

    def _mib_illum_hair(self):
        cmds.shadingNode('mib_illum_hair', asShader=True)
    mentalrayDict[
        'mib_illum_hair'] = ("%s"
                             "/render_mib_illum_hair.png"
                             ) % iconPath

    def _mib_illum_hair_x(self):
        cmds.shadingNode('mib_illum_hair_x', asShader=True)
    mentalrayDict[
        'mib_illum_hair_x'] = ("%s"
                               "/render_mib_illum_hair.png"
                               ) % iconPath

    def _mib_ptex_lookup(self):
        cmds.shadingNode('mib_ptex_lookup', asShader=True)
    mentalrayDict['mib_ptex_lookup'] = "render_unknown.png"

    def _mila_material(self):
        cmds.shadingNode('mila_material', asShader=True)
    mentalrayDict['mila_material'] = "render_unknown.png"

    def _misss_fast_shader2_x(self):
        cmds.shadingNode('misss_fast_shader2_x', asShader=True)
    mentalrayDict['misss_fast_shader2_x'] = "render_unknown.png"

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
    mentalrayDict[
        'misss_fast_shader_x'] = ("%s"
                                  "/render_misss_fast_shader_x.png"
                                  ) % iconPath

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
    mentalrayDict[
        'misss_fast_shader_x_passes'] = ("%s"
                                         "/render_misss_fast"
                                         "_shader_x_passes.png"
                                         ) % iconPath

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
    mentalrayDict[
        'misss_fast_simple_maya'] = ("%s"
                                     "/render_misss_fast_simple_maya.png"
                                     ) % iconPath

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
    mentalrayDict[
        'misss_fast_skin_maya'] = ("%s"
                                   "/render_misss_fast_skin_maya.png"
                                   ) % iconPath

    def _xgen_hair_phen(self):
        cmds.shadingNode('xgen_hair_phen', asShader=True)
    mentalrayDict['xgen_hair_phen'] = 'commandButton.png'

    def _mib_ray_marcher(self):
        cmds.shadingNode('mib_ray_marcher', asShader=True)
    mentalrayDict[
        'mib_ray_marcher'] = ('%s'
                              '/render_mib_ray_marcher.png'
                              ) % iconPath

    def _mib_volume(self):
        cmds.shadingNode('mib_volume', asShader=True)
    mentalrayDict[
        'mib_volume'] = '%s/render_mib_volume.png' % iconPath

    def _parti_volume(self):
        cmds.shadingNode('parti_volume', asShader=True)
    mentalrayDict[
        'parti_volume'] = '%s/render_parti_volume.png' % iconPath

    def _parti_volume_photon(self):
        cmds.shadingNode('parti_volume_photon', asShader=True)
    mentalrayDict[
        'parti_volume_photon'] = ('%s'
                                  '/render_parti_volume_photon.png'
                                  ) % iconPath

    def _bifrost_color_channel(self):
        cmds.shadingNode('bifrost_color_channel', asShader=True)
    mentalrayDict['bifrost_color_channel'] = 'render_unknown.png'

    def _bifrost_scalar_channel(self):
        cmds.shadingNode('bifrost_scalar_channel', asShader=True)
    mentalrayDict['bifrost_scalar_channel'] = 'render_unknown.png'

    def _bifrost_scalar_channel_grad(self):
        cmds.shadingNode('bifrost_scalar_channel_grad', asShader=True)
    mentalrayDict['bifrost_scalar_channel_grad'] = 'render_unknown.png'

    def _bifrost_vector_channel(self):
        cmds.shadingNode('bifrost_vector_channel', asShader=True)
    mentalrayDict['bifrost_vector_channel'] = 'render_unknown.png'

    def _mentalrayTexture(self):
        cmds.shadingNode('mentalrayTexture', asTexture=True)
    mentalrayDict[
        'mentalrayTexture'] = ('%s'
                               '/render_mentalrayTexture.png'
                               ) % iconPath

    def _mentalrayVertexColors(self):
        cmds.shadingNode('mentalrayVertexColors', asTexture=True)
    mentalrayDict[
        'mentalrayVertexColors'] = ('%s'
                                    '/render_mentalrayVertexColors.png'
                                    ) % iconPath

    def _mia_exposure_photographic_rev(self):
        cmds.shadingNode('mia_exposure_photographic_rev', asTexture=True)
    mentalrayDict[
        'mia_exposure_photographic_rev'] = 'render_unknown.png'

    def _mia_light_surface(self):
        cmds.shadingNode('mia_light_surface', asTexture=True)
    mentalrayDict[
        'mia_light_surface'] = ('%s'
                                '/render_mia_light_surface.png'
                                ) % iconPath

    def _mia_roundcorners(self):
        cmds.shadingNode('mia_roundcorners', asTexture=True)
    mentalrayDict[
        'mia_roundcorners'] = ('%s'
                               '/render_mia_roundcorners.png'
                               ) % iconPath

    def _mib_amb_occlusion(self):
        cmds.shadingNode('mib_amb_occlusion', asTexture=True)
    mentalrayDict[
        'mib_amb_occlusion'] = ('%s'
                                '/render_mib_amb_occlusion.png'
                                ) % iconPath

    def _mib_fast_occlusion(self):
        cmds.shadingNode('mib_fast_occlusion', asTexture=True)
    mentalrayDict[
        'mib_fast_occlusion'] = ('%s'
                                 'render_mib_fast_occlusion.png'
                                 ) % iconPath

    def _mila_bump_flakes(self):
        cmds.shadingNode('mila_bump_flakes', asTexture=True)
    mentalrayDict['mila_bump_flakes'] = 'render_unknown.png'

    def _mila_flakes_adapter(self):
        cmds.shadingNode('mila_flakes_adapter', asTexture=True)
    mentalrayDict['mila_flakes_adapter'] = 'render_unknown.png'

    def _xgen_seexpr(self):
        cmds.shadingNode('xgen_seexpr', asTexture=True)
    mentalrayDict['xgen_seexpr'] = 'render_unknown.png'

    def _mia_ciesky(self):
        cmds.shadingNode('mia_ciesky', asTexture=True)
    mentalrayDict[
        'mia_ciesky'] = '%s/render_mia_ciesky.png' % iconPath

    def _mia_envblur(self):
        cmds.shadingNode('mia_envblur', asShader=True)
    mentalrayDict[
        'mia_envblur'] = '%s/render_mia_envblur.png' % iconPath

    def _mia_photometric_light(self):
        cmds.shadingNode('mia_photometric_light', asUtility=True)
    mentalrayDict[
        'mia_photometric_light'] = ('%s'
                                    '/render_mia_photometric_light.png'
                                    ) % iconPath

    def _mia_physicalsun(self):
        cmds.shadingNode('mia_physicalsun', asUtility=True)
    mentalrayDict[
        'mia_physicalsun'] = ('%s'
                              '/render_mia_physicalsun.png'
                              ) % iconPath

    def _mia_portal_light(self):
        cmds.shadingNode('mia_portal_light', asUtility=True)
    mentalrayDict[
        'mia_portal_light'] = ('%s'
                               '/render_mia_portal_light.png'
                               ) % iconPath

    def _mib_blackbody(self):
        cmds.shadingNode('mib_blackbody', asUtility=True)
    mentalrayDict[
        'mib_blackbody'] = ('%s'
                            '/render_mib_blackbody.png'
                            ) % iconPath

    def _mib_cie_d(self):
        cmds.shadingNode('mib_cie_d', asUtility=True)
    mentalrayDict[
        'mib_cie_d'] = '%s/render_mib_cie_d.png' % iconPath

    def _physical_light(self):
        cmds.shadingNode('physical_light', asUtility=True)
    mentalrayDict[
        'physical_light'] = '%s/render_physical_light.png' % iconPath

    def _user_ibl_env(self):
        cmds.shadingNode('user_ibl_env', asUtility=True)
    mentalrayDict['user_ibl_env'] = 'render_unknown.png'

    def _user_ibl_rect(self):
        cmds.shadingNode('user_ibl_rect', asUtility=True)
    mentalrayDict['user_ibl_rect'] = 'render_unknown.png'
