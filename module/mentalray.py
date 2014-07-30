import maya.cmds as cmds
import os
import sys

iconPaths = os.environ['XBMLANGPATH']
if sys.platform == "linux2":
    for path in iconPaths.split(":"):
        if 'mentalray/icons' in path:
            iconPath = path
            break
        else:
            iconPath = ""
elif sys.platform == "darwin":
    for path in iconPaths.split(":"):
        if 'mentalray/icons' in path:
            iconPath = path
            break
        else:
            iconPath = ""
elif sys.platform == "win32":
    for path in iconPaths.split(";"):
        if 'mentalray/icons' in path:
            iconPath = path
            break
        else:
            iconPath = ""
else:
    iconPath = ""

# iconPath = r"C:\Program Files\Autodesk\Maya2013\mentalray\icons"


class Commands(object):

    mentalrayDict = {}

    def __init__(self):
        pass

    ####################
    # MENTAL RAY
    ####################
    def _builtin_bsdf_architectural(self):
        cmds.shadingNode('builtin_bsdf_architectural', asShader=True)
    mentalrayDict['builtin_bsdf_architectural'] = 'render_unknown.png'

    def _builtin_bsdf_architectural_comp(self):
        cmds.shadingNode('builtin_bsdf_architectural_comp', asShader=True)
    mentalrayDict['builtin_bsdf_architectural_comp'] = 'render_unknown.png'

    def _builtin_bsdf_ashikhmin(self):
        cmds.shadingNode('builtin_bsdf_ashikhmin', asShader=True)
    mentalrayDict['builtin_bsdf_ashikhmin'] = 'render_unknown.png'

    def _builtin_bsdf_carpaint(self):
        cmds.shadingNode('builtin_bsdf_carpaint', asShader=True)
    mentalrayDict['builtin_bsdf_carpaint'] = 'render_unknown.png'

    def _builtin_bsdf_lambert(self):
        cmds.shadingNode('builtin_bsdf_lambert', asShader=True)
    mentalrayDict['builtin_bsdf_lambert'] = 'render_unknown.png'

    def _builtin_bsdf_mirror(self):
        cmds.shadingNode('builtin_bsdf_mirror', asShader=True)
    mentalrayDict['builtin_bsdf_mirror'] = 'render_unknown.png'

    def _builtin_bsdf_phong(self):
        cmds.shadingNode('builtin_bsdf_phong', asShader=True)
    mentalrayDict['builtin_bsdf_phong'] = 'render_unknown.png'

    def _dgs_material(self):
        cmds.shadingNode('dgs_material', asShader=True)
    mentalrayDict['dgs_material'] = '%s/render_dgs_material.png' % iconPath

    def _dielectric_material(self):
        cmds.shadingNode('dielectric_material', asShader=True)
    mentalrayDict[
        'dielectric_material'] = '%s/render_dielectric_material.png' % iconPath

    def _mi_car_paint_phen(self):
        cmds.shadingNode('mi_car_paint_phen', asShader=True)
    mentalrayDict[
        'mi_car_paint_phen'] = ("%s"
                                "/render_mi_car_paint_phen.png"
                                ) % iconPath

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

    def _mi_metallic_paint(self):
        cmds.shadingNode('mi_metallic_paint', asShader=True)
    mentalrayDict[
        'mi_metallic_paint'] = ("%s"
                                "/render_mi_metallic_paint.png"
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

    def _mia_material(self):
        cmds.shadingNode('mia_material', asShader=True)
    mentalrayDict[
        'mia_material'] = ("%s"
                           "/render_mia_material.png"
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

    def _mib_glossy_reflection(self):
        cmds.shadingNode('mib_glossy_reflection', asShader=True)
    mentalrayDict['mib_glossy_reflection'] = '%s/render_mib_glossy_reflection.png' % iconPath

    def _mib_glossy_refraction(self):
        cmds.shadingNode('mib_glossy_refraction', asShader=True)
    mentalrayDict['mib_glossy_refraction'] = '%s/render_mib_glossy_refraction.png' % iconPath

    def _mib_illum_blinn(self):
        cmds.shadingNode('mib_illum_blinn', asShader=True)
    mentalrayDict['mib_illum_blinn'] = '%s/render_mib_illum_blinn.png' % iconPath

    def _mib_illum_cooktorr(self):
        cmds.shadingNode('mib_illum_cooktorr', asShader=True)
    mentalrayDict['mib_illum_cooktorr'] = '%s/render_mib_illum_cooktorr.png' % iconPath

    def _mib_illum_lambert(self):
        cmds.shadingNode('mib_illum_lambert', asShader=True)
    mentalrayDict['mib_illum_lambert'] = '%s/render_mib_illum_lambert.png' % iconPath

    def _mib_illum_phong(self):
        cmds.shadingNode('mib_illum_phong', asShader=True)
    mentalrayDict['mib_illum_phong'] = '%s/render_mib_illum_phong.png' % iconPath

    def _mib_illum_ward(self):
        cmds.shadingNode('mib_illum_ward', asShader=True)
    mentalrayDict['mib_illum_ward'] = '%s/render_mib_illum_ward.png' % iconPath

    def _mib_illum_ward_deriv(self):
        cmds.shadingNode('mib_illum_ward_deriv', asShader=True)
    mentalrayDict['mib_illum_ward_deriv'] = '%s/render_mib_illum_ward_deriv.png' % iconPath

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

    def _mila_material(self):
        cmds.shadingNode('mila_material', asShader=True)
    mentalrayDict['mila_material'] = "render_unknown.png"

    def _misss_call_shader(self):
        cmds.shadingNode('misss_call_shader', asShader=True)
    mentalrayDict['misss_call_shader'] = "%s/render_misss_call_shader.png" % iconPath

    # SSS SHADERS
    def _misss_fast_shader(self):
        node = cmds.shadingNode('misss_fast_shader', asShader=True)
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
        'misss_fast_shader'] = ("%s"
                                "/render_misss_fast_shader.png"
                                ) % iconPath

    def _misss_fast_shader2(self):
        cmds.shadingNode('misss_fast_shader2', asShader=True)
    mentalrayDict['misss_fast_shader2'] = "render_unknown.png"

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

    def _misss_mia_skin2_surface_phen(self):
        cmds.shadingNode('misss_mia_skin2_surface_phen', asShader=True)
    mentalrayDict['misss_mia_skin2_surface_phen'] = 'render_unknown.png'

    def _misss_physical(self):
        cmds.shadingNode('misss_physical', asShader=True)
    mentalrayDict['misss_physical'] = '%s/render_misss_physical.png' % iconPath

    def _misss_set_normal(self):
        cmds.shadingNode('misss_set_normal', asShader=True)
    mentalrayDict['misss_set_normal'] = '%s/render_misss_set_normal.png' % iconPath

    def _misss_skin_specular(self):
        cmds.shadingNode('misss_skin_specular', asShader=True)
    mentalrayDict['misss_skin_specular'] = '%s/render_misss_skin_specular.png' % iconPath
    # SSS END

    def _path_material(self):
        cmds.shadingNode('path_material', asShader=True)
    mentalrayDict['path_material'] = '%s/render_path_material.png' % iconPath

    def _transmat(self):
        cmds.shadingNode('transmat', asShader=True)
    mentalrayDict['transmat'] = '%s/render_transmat.png' % iconPath

    def _mib_shadow_transparency(self):
        cmds.shadingNode('mib_shadow_transparency', asUtility=True)
    mentalrayDict['mib_shadow_transparency'] = '%s/render_mib_shadow_transparency.png' % iconPath

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
        cmds.shadingNode('parti_volume_photon', asUtility=True)
    mentalrayDict[
        'parti_volume_photon'] = ('%s'
                                  '/render_parti_volume_photon.png'
                                  ) % iconPath

    def _dgs_material_photon(self):
        cmds.shadingNode('dgs_material_photon', asUtility=True)
    mentalrayDict['dgs_material_photon'] = '%s/render_dgs_material_photon.png' % iconPath

    def _dielectric_material_photon(self):
        cmds.shadingNode('dielectric_material_photon', asUtility=True)
    mentalrayDict['dielectric_material_photon'] = '%s/render_dielectric_material_photon.png' % iconPath

    def _mib_photon_basic(self):
        cmds.shadingNode('mib_photon_basic', asUtility=True)
    mentalrayDict['mib_photon_basic'] = '%s/render_mib_photon_basic.png' % iconPath

    def _transmat_photon(self):
        cmds.shadingNode('transmat_photon', asUtility=True)
    mentalrayDict['transmat_photon'] = '%s/render_transmat_photon.png' % iconPath

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

    def _mi_bump_flakes(self):
        cmds.shadingNode('mi_bump_flakes', asTexture=True)
    mentalrayDict[
        'mi_bump_flakes'] = ('%s'
                             '/render_mi_bump_flakes.png'
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

    def _mib_bent_normal_env(self):
        cmds.shadingNode('mib_bent_normal_env', asTexture=True)
    mentalrayDict[
        'mib_bent_normal_env'] = ('%s'
                                  '/render_mib_bent_normal_env.png'
                                  ) % iconPath

    def _mib_fast_occlusion(self):
        cmds.shadingNode('mib_fast_occlusion', asTexture=True)
    mentalrayDict[
        'mib_fast_occlusion'] = ('%s'
                                 '/render_mib_fast_occlusion.png'
                                 ) % iconPath

    def _mib_bump_basis(self):
        cmds.shadingNode('mib_bump_basis', asTexture=True)
    mentalrayDict['mib_bump_basis'] = '%s/render_mib_bump_basis.png' % iconPath

    def _mib_bump_map(self):
        cmds.shadingNode('mib_bump_map', asTexture=True)
    mentalrayDict['mib_bump_map'] = '%s/render_mib_bump_map.png' % iconPath

    def _mib_bump_map2(self):
        cmds.shadingNode('mib_bump_map2', asTexture=True)
    mentalrayDict['mib_bump_map2'] = '%s/render_mib_bump_map2.png' % iconPath

    def _mib_passthrough_bump_map(self):
        cmds.shadingNode('mib_passthrough_bump_map', asTexture=True)
    mentalrayDict['mib_passthrough_bump_map'] = '%s/render_mib_passthrough_bump_map.png' % iconPath

    def _mib_texture_checkerboard(self):
        cmds.shadingNode('mib_texture_checkerboard', asTexture=True)
    mentalrayDict['mib_texture_checkerboard'] = '%s/render_mib_texture_checkerboard.png' % iconPath

    def _mib_texture_filter_lookup(self):
        cmds.shadingNode('mib_texture_filter_lookup', asTexture=True)
    mentalrayDict['mib_texture_filter_lookup'] = '%s/render_mib_texture_filter_lookup.png' % iconPath

    def _mib_texture_lookup(self):
        cmds.shadingNode('mib_texture_lookup', asTexture=True)
    mentalrayDict['mib_texture_lookup'] = '%s/render_mib_texture_lookup.png' % iconPath

    def _mib_texture_lookup2(self):
        cmds.shadingNode('mib_texture_lookup2', asTexture=True)
    mentalrayDict['mib_texture_lookup2'] = '%s/render_mib_texture_lookup2.png' % iconPath

    def _mib_texture_polkadot(self):
        cmds.shadingNode('mib_texture_polkadot', asTexture=True)
    mentalrayDict['mib_texture_polkadot'] = '%s/render_mib_texture_polkadot.png' % iconPath

    def _mib_texture_polkasphere(self):
        cmds.shadingNode('mib_texture_polkasphere', asTexture=True)
    mentalrayDict['mib_texture_polkasphere'] = '%s/render_mib_texture_polkasphere.png' % iconPath

    def _mib_texture_remap(self):
        cmds.shadingNode('mib_texture_remap', asTexture=True)
    mentalrayDict['mib_texture_remap'] = '%s/render_mib_texture_remap.png' % iconPath

    def _mib_texture_rotate(self):
        cmds.shadingNode('mib_texture_rotate', asTexture=True)
    mentalrayDict['mib_texture_rotate'] = '%s/render_mib_texture_rotate.png' % iconPath

    def _mib_texture_turbulence(self):
        cmds.shadingNode('mib_texture_turbulence', asTexture=True)
    mentalrayDict['mib_texture_turbulence'] = '%s/render_mib_texture_turbulence.png' % iconPath

    def _mib_texture_vector(self):
        cmds.shadingNode('mib_texture_vector', asTexture=True)
    mentalrayDict['mib_texture_vector'] = '%s/render_mib_texture_vector.png' % iconPath

    def _mib_texture_wave(self):
        cmds.shadingNode('mib_texture_wave', asTexture=True)
    mentalrayDict['mib_texture_wave'] = '%s/render_mib_texture_wave.png' % iconPath

    def _misss_lambert_gamma(self):
        cmds.shadingNode('misss_lambert_gamma', asTexture=True)
    mentalrayDict['misss_lambert_gamma'] = '%s/render_misss_lambert_gamma.png' % iconPath

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
        cmds.shadingNode('mia_ciesky', asShader=True)
    mentalrayDict[
        'mia_ciesky'] = '%s/render_mia_ciesky.png' % iconPath

    def _mia_envblur(self):
        cmds.shadingNode('mia_envblur', asShader=True)
    mentalrayDict[
        'mia_envblur'] = '%s/render_mia_envblur.png' % iconPath

    def _mib_lookup_cube1(self):
        cmds.shadingNode('mib_lookup_cube1', asShader=True)
    mentalrayDict[
        'mib_lookup_cube1'] = '%s/render_mib_lookup_cube1.png' % iconPath

    def _mib_lookup_cube6(self):
        cmds.shadingNode('mib_lookup_cube6', asShader=True)
    mentalrayDict[
        'mib_lookup_cube6'] = '%s/render_mib_lookup_cube6.png' % iconPath

    def _mib_lookup_cylindrical(self):
        cmds.shadingNode('mib_lookup_cylindrical', asShader=True)
    mentalrayDict[
        'mib_lookup_cylindrical'] = '%s/render_mib_lookup_cylindrical.png' % iconPath

    def _mib_lookup_spherical(self):
        cmds.shadingNode('mib_lookup_spherical', asShader=True)
    mentalrayDict[
        'mib_lookup_spherical'] = '%s/render_mib_lookup_spherical.png' % iconPath

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

    def _mib_fg_occlusion(self):
        cmds.shadingNode('mib_fg_occlusion', asUtility=True)
    mentalrayDict[
        'mib_fg_occlusion'] = '%s/render_mib_fg_occlusion.png' % iconPath

    def _mib_light_infinite(self):
        cmds.shadingNode('mib_light_infinite', asUtility=True)
    mentalrayDict[
        'mib_light_infinite'] = '%s/render_mib_light_infinite.png' % iconPath

    def _mib_light_photometric(self):
        cmds.shadingNode('mib_light_photometric', asUtility=True)
    mentalrayDict[
        'mib_light_photometric'] = '%s/render_mib_light_photometric.png' % iconPath

    def _mib_light_point(self):
        cmds.shadingNode('mib_light_point', asUtility=True)
    mentalrayDict[
        'mib_light_point'] = '%s/render_mib_light_point.png' % iconPath

    def _mib_light_spot(self):
        cmds.shadingNode('mib_light_spot', asUtility=True)
    mentalrayDict[
        'mib_light_spot'] = '%s/render_mib_light_spot.png' % iconPath

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

    def _mib_lightmap_sample(self):
        cmds.shadingNode('mib_lightmap_sample', asUtility=True)
    mentalrayDict['mib_lightmap_sample'] = '%s/render_mib_lightmap_sample.png' % iconPath

    def _mib_lightmap_write(self):
        cmds.shadingNode('mib_lightmap_write', asUtility=True)
    mentalrayDict['mib_lightmap_write'] = '%s/render_mib_lightmap_write.png' % iconPath

    def _misss_fast_lmap_maya(self):
        cmds.shadingNode('misss_fast_lmap_maya', asUtility=True)
    mentalrayDict['misss_fast_lmap_maya'] = '%s/render_misss_fast_lmap_maya.png' % iconPath

    def _misss_lightmap_phen(self):
        cmds.shadingNode('misss_lightmap_phen', asUtility=True)
    mentalrayDict['misss_lightmap_phen'] = 'render_unknown.png'

    def _misss_lightmap_write(self):
        cmds.shadingNode('misss_lightmap_write', asUtility=True)
    mentalrayDict['misss_lightmap_write'] = '%s/render_misss_lightmap_write.png' % iconPath

    def _mia_exposure_photographic(self):
        cmds.shadingNode('mia_exposure_photographic', asUtility=True)
    mentalrayDict['mia_exposure_photographic'] = '%s/render_mia_exposure_photographic.png' % iconPath

    def _mia_exposure_simple(self):
        cmds.shadingNode('mia_exposure_simple', asUtility=True)
    mentalrayDict['mia_exposure_simple'] = '%s/render_mia_exposure_simple.png' % iconPath

    def _mia_lens_bokeh(self):
        cmds.shadingNode('mia_lens_bokeh', asUtility=True)
    mentalrayDict['mia_lens_bokeh'] = '%s/render_mia_lens_bokeh.png' % iconPath

    def _mia_physicalsky(self):
        cmds.shadingNode('mia_physicalsky', asUtility=True)
    mentalrayDict['mia_physicalsky'] = '%s/render_mia_physicalsky.png' % iconPath

    def _mib_lens_clamp(self):
        cmds.shadingNode('mib_lens_clamp', asUtility=True)
    mentalrayDict['mib_lens_clamp'] = '%s/render_mib_lens_clamp.png' % iconPath

    def _mib_lens_stencil(self):
        cmds.shadingNode('mib_lens_stencil', asUtility=True)
    mentalrayDict['mib_lens_stencil'] = '%s/render_mib_lens_stencil.png' % iconPath

    def _mib_lookup_background(self):
        cmds.shadingNode('mib_lookup_background', asUtility=True)
    mentalrayDict['mib_lookup_background'] = '%s/render_mib_lookup_background.png' % iconPath

    def _oversampling_lens(self):
        cmds.shadingNode('oversampling_lens', asUtility=True)
    mentalrayDict['oversampling_lens'] = '%s/render_oversampling_lens.png' % iconPath

    def _physical_lens_dof(self):
        cmds.shadingNode('physical_lens_dof', asUtility=True)
    mentalrayDict['physical_lens_dof'] = '%s/render_physical_lens_dof.png' % iconPath

    def _abcimport(self):
        cmds.shadingNode('abcimport', asUtility=True)
    mentalrayDict['abcimport'] = 'render_unknown.png'

    def _mib_geo_add_uv_texsurf(self):
        cmds.shadingNode('mib_geo_add_uv_texsurf', asUtility=True)
    mentalrayDict['mib_geo_add_uv_texsurf'] = '%s/render_mib_geo_add_uv_texsurf.png' % iconPath

    def _mib_geo_cone(self):
        cmds.shadingNode('mib_geo_cone', asUtility=True)
    mentalrayDict['mib_geo_cone'] = '%s/render_mib_geo_cone.png' % iconPath

    def _mib_geo_cube(self):
        cmds.shadingNode('mib_geo_cube', asUtility=True)
    mentalrayDict['mib_geo_cube'] = '%s/render_mib_geo_cube.png' % iconPath

    def _mib_geo_cylinder(self):
        cmds.shadingNode('mib_geo_cylinder', asUtility=True)
    mentalrayDict['mib_geo_cylinder'] = '%s/render_mib_geo_cylinder.png' % iconPath

    def _mib_geo_instance(self):
        cmds.shadingNode('mib_geo_instance', asUtility=True)
    mentalrayDict['mib_geo_instance'] = '%s/render_mib_geo_instance.png' % iconPath

    def _mib_geo_instance_mlist(self):
        cmds.shadingNode('mib_geo_instance_mlist', asUtility=True)
    mentalrayDict['mib_geo_instance_mlist'] = '%s/render_mib_geo_instance_mlist.png' % iconPath

    def _mib_geo_sphere(self):
        cmds.shadingNode('mib_geo_sphere', asUtility=True)
    mentalrayDict['mib_geo_sphere'] = '%s/render_mib_geo_sphere.png' % iconPath

    def _mib_geo_square(self):
        cmds.shadingNode('mib_geo_square', asUtility=True)
    mentalrayDict['mib_geo_square'] = '%s/render_mib_geo_square.png' % iconPath

    def _mib_geo_torus(self):
        cmds.shadingNode('mib_geo_torus', asUtility=True)
    mentalrayDict['mib_geo_torus'] = '%s/render_mib_geo_torus.png' % iconPath

    def _contour_store_function(self):
        cmds.shadingNode('contour_store_function', asUtility=True)
    mentalrayDict['contour_store_function'] = '%s/render_contour_store_function.png' % iconPath

    def _contour_store_function_simple(self):
        cmds.shadingNode('contour_store_function_simple', asUtility=True)
    mentalrayDict['contour_store_function_simple'] = '%s/render_contour_store_function_simple.png' % iconPath

    def _contour_contrast_function_levels(self):
        cmds.shadingNode('contour_contrast_function_levels', asUtility=True)
    mentalrayDict['contour_contrast_function_levels'] = '%s/render_contour_contrast_function_levels.png' % iconPath

    def _contour_contrast_function_simple(self):
        cmds.shadingNode('contour_contrast_function_simple', asUtility=True)
    mentalrayDict['contour_contrast_function_simple'] = '%s/render_contour_contrast_function_simple.png' % iconPath

    def _contour_shader_combi(self):
        cmds.shadingNode('contour_shader_combi', asUtility=True)
    mentalrayDict['contour_shader_combi'] = '%s/render_contour_shader_combi.png' % iconPath

    def _contour_shader_curvature(self):
        cmds.shadingNode('contour_shader_curvature', asUtility=True)
    mentalrayDict['contour_shader_curvature'] = '%s/render_contour_shader_curvature.png' % iconPath

    def _contour_shader_depthfade(self):
        cmds.shadingNode('contour_shader_depthfade', asUtility=True)
    mentalrayDict['contour_shader_depthfade'] = '%s/render_contour_shader_depthfade.png' % iconPath

    def _contour_shader_factorcolor(self):
        cmds.shadingNode('contour_shader_factorcolor', asUtility=True)
    mentalrayDict['contour_shader_factorcolor'] = '%s/render_contour_shader_factorcolor.png' % iconPath

    def _contour_shader_framefade(self):
        cmds.shadingNode('contour_shader_framefade', asUtility=True)
    mentalrayDict['contour_shader_framefade'] = '%s/render_contour_shader_framefade.png' % iconPath

    def _contour_shader_layerthinner(self):
        cmds.shadingNode('contour_shader_layerthinner', asUtility=True)
    mentalrayDict['contour_shader_layerthinner'] = '%s/render_contour_shader_layerthinner.png' % iconPath

    def _contour_shader_maxcolor(self):
        cmds.shadingNode('contour_shader_maxcolor', asUtility=True)
    mentalrayDict['contour_shader_maxcolor'] = '%s/render_contour_shader_maxcolor.png' % iconPath

    def _contour_shader_silhouette(self):
        cmds.shadingNode('contour_shader_silhouette', asUtility=True)
    mentalrayDict['contour_shader_silhouette'] = '%s/render_contour_shader_silhouette.png' % iconPath

    def _contour_shader_simple(self):
        cmds.shadingNode('contour_shader_simple', asUtility=True)
    mentalrayDict['contour_shader_simple'] = '%s/render_contour_shader_simple.png' % iconPath

    def _contour_shader_widthfromcolor(self):
        cmds.shadingNode('contour_shader_widthfromcolor', asUtility=True)
    mentalrayDict['contour_shader_widthfromcolor'] = '%s/render_contour_shader_widthfromcolor.png' % iconPath

    def _contour_shader_widthfromlight(self):
        cmds.shadingNode('contour_shader_widthfromlight', asUtility=True)
    mentalrayDict['contour_shader_widthfromlight'] = '%s/render_contour_shader_widthfromlight.png' % iconPath

    def _contour_shader_widthfromlightdir(self):
        cmds.shadingNode('contour_shader_widthfromlightdir', asUtility=True)
    mentalrayDict['contour_shader_widthfromlightdir'] = '%s/render_contour_shader_widthfromlightdir.png' % iconPath

    def _contour_composite(self):
        cmds.shadingNode('contour_composite', asUtility=True)
    mentalrayDict['contour_composite'] = '%s/render_contour_composite.png' % iconPath

    def _contour_only(self):
        cmds.shadingNode('contour_only', asUtility=True)
    mentalrayDict['contour_only'] = '%s/render_contour_only.png' % iconPath

    def _contour_ps(self):
        cmds.shadingNode('contour_ps', asUtility=True)
    mentalrayDict['contour_ps'] = '%s/render_contour_ps.png' % iconPath

    def _mib_continue(self):
        cmds.shadingNode('mib_continue', asUtility=True)
    mentalrayDict['mib_continue'] = '%s/render_mib_continue.png' % iconPath

    def _mib_dielectric(self):
        cmds.shadingNode('mib_dielectric', asUtility=True)
    mentalrayDict['mib_dielectric'] = '%s/render_mib_dielectric.png' % iconPath

    def _mib_opacity(self):
        cmds.shadingNode('mib_opacity', asUtility=True)
    mentalrayDict['mib_opacity'] = '%s/render_mib_opacity.png' % iconPath

    def _mib_reflect(self):
        cmds.shadingNode('mib_reflect', asUtility=True)
    mentalrayDict['mib_reflect'] = '%s/render_mib_reflect.png' % iconPath

    def _mib_refract(self):
        cmds.shadingNode('mib_refract', asUtility=True)
    mentalrayDict['mib_refract'] = '%s/render_mib_refract.png' % iconPath

    def _mib_refraction_index(self):
        cmds.shadingNode('mib_refraction_index', asUtility=True)
    mentalrayDict['mib_refraction_index'] = '%s/render_mib_refraction_index.png' % iconPath

    def _mib_transparency(self):
        cmds.shadingNode('mib_transparency', asUtility=True)
    mentalrayDict['mib_transparency'] = '%s/render_mib_transparency.png' % iconPath

    def _mib_twosided(self):
        cmds.shadingNode('mib_twosided', asUtility=True)
    mentalrayDict['mib_twosided'] = '%s/render_mib_twosided.png' % iconPath

    def _mib_color_alpha(self):
        cmds.shadingNode('mib_color_alpha', asUtility=True)
    mentalrayDict['mib_color_alpha'] = '%s/render_mib_color_alpha.png' % iconPath

    def _mib_color_average(self):
        cmds.shadingNode('mib_color_average', asUtility=True)
    mentalrayDict['mib_color_average'] = '%s/render_mib_color_average.png' % iconPath

    def _mib_color_intensity(self):
        cmds.shadingNode('mib_color_intensity', asUtility=True)
    mentalrayDict['mib_color_intensity'] = '%s/render_mib_color_intensity.png' % iconPath

    def _mib_color_interpolate(self):
        cmds.shadingNode('mib_color_interpolate', asUtility=True)
    mentalrayDict['mib_color_interpolate'] = '%s/render_mib_color_interpolate.png' % iconPath

    def _mib_color_mix(self):
        cmds.shadingNode('mib_color_mix', asUtility=True)
    mentalrayDict['mib_color_mix'] = '%s/render_mib_color_mix.png' % iconPath

    def _mib_color_spread(self):
        cmds.shadingNode('mib_color_spread', asUtility=True)
    mentalrayDict['mib_color_spread'] = '%s/render_mib_color_spread.png' % iconPath

    def _mentalrayPhenomenon(self):
        cmds.shadingNode('mentalrayPhenomenon', asUtility=True)
    mentalrayDict['mentalrayPhenomenon'] = '%s/render_mentalrayPhenomenon.png' % iconPath

    def _mib_data_bool(self):
        cmds.shadingNode('mib_data_bool', asUtility=True)
    mentalrayDict['mib_data_bool'] = 'render_unknown.png'

    def _mib_data_bool_array(self):
        cmds.shadingNode('mib_data_bool_array', asUtility=True)
    mentalrayDict['mib_data_bool_array'] = 'render_unknown.png'

    def _mib_data_color(self):
        cmds.shadingNode('mib_data_color', asUtility=True)
    mentalrayDict['mib_data_color'] = 'render_unknown.png'

    def _mib_data_color_array(self):
        cmds.shadingNode('mib_data_color_array', asUtility=True)
    mentalrayDict['mib_data_color_array'] = 'render_unknown.png'

    def _mib_data_get_bool(self):
        cmds.shadingNode('mib_data_get_bool', asUtility=True)
    mentalrayDict['mib_data_get_bool'] = 'render_unknown.png'

    def _mib_data_get_color(self):
        cmds.shadingNode('mib_data_get_color', asUtility=True)
    mentalrayDict['mib_data_get_color'] = 'render_unknown.png'

    def _mib_data_get_int(self):
        cmds.shadingNode('mib_data_get_int', asUtility=True)
    mentalrayDict['mib_data_get_int'] = 'render_unknown.png'

    def _mib_data_get_scalar(self):
        cmds.shadingNode('mib_data_get_scalar', asUtility=True)
    mentalrayDict['mib_data_get_scalar'] = 'render_unknown.png'

    def _mib_data_get_shader(self):
        cmds.shadingNode('mib_data_get_shader', asUtility=True)
    mentalrayDict['mib_data_get_shader'] = 'render_unknown.png'

    def _mib_data_get_shader_bool(self):
        cmds.shadingNode('mib_data_get_shader_bool', asUtility=True)
    mentalrayDict['mib_data_get_shader_bool'] = 'render_unknown.png'

    def _mib_data_get_shader_color(self):
        cmds.shadingNode('mib_data_get_shader_color', asUtility=True)
    mentalrayDict['mib_data_get_shader_color'] = 'render_unknown.png'

    def _mib_data_get_shader_int(self):
        cmds.shadingNode('mib_data_get_shader_int', asUtility=True)
    mentalrayDict['mib_data_get_shader_int'] = 'render_unknown.png'

    def _mib_data_get_shader_scalar(self):
        cmds.shadingNode('mib_data_get_shader_scalar', asUtility=True)
    mentalrayDict['mib_data_get_shader_scalar'] = 'render_unknown.png'

    def _mib_data_get_shader_vector(self):
        cmds.shadingNode('mib_data_get_shader_vector', asUtility=True)
    mentalrayDict['mib_data_get_shader_vector'] = 'render_unknown.png'

    def _mib_data_get_string(self):
        cmds.shadingNode('mib_data_get_string', asUtility=True)
    mentalrayDict['mib_data_get_string'] = 'render_unknown.png'

    def _mib_data_get_texture(self):
        cmds.shadingNode('mib_data_get_texture', asUtility=True)
    mentalrayDict['mib_data_get_texture'] = 'render_unknown.png'

    def _mib_data_get_vector(self):
        cmds.shadingNode('mib_data_get_vector', asUtility=True)
    mentalrayDict['mib_data_get_vector'] = 'render_unknown.png'

    def _mib_data_int(self):
        cmds.shadingNode('mib_data_int', asUtility=True)
    mentalrayDict['mib_data_int'] = 'render_unknown.png'

    def _mib_data_int_array(self):
        cmds.shadingNode('mib_data_int_array', asUtility=True)
    mentalrayDict['mib_data_int_array'] = 'render_unknown.png'

    def _mib_data_scalar(self):
        cmds.shadingNode('mib_data_scalar', asUtility=True)
    mentalrayDict['mib_data_scalar'] = 'render_unknown.png'

    def _mib_data_scalar_array(self):
        cmds.shadingNode('mib_data_scalar_array', asUtility=True)
    mentalrayDict['mib_data_scalar_array'] = 'render_unknown.png'

    def _mib_data_shader(self):
        cmds.shadingNode('mib_data_shader', asUtility=True)
    mentalrayDict['mib_data_shader'] = 'render_unknown.png'

    def _mib_data_shader_array(self):
        cmds.shadingNode('mib_data_shader_array', asUtility=True)
    mentalrayDict['mib_data_shader_array'] = 'render_unknown.png'

    def _mib_data_string(self):
        cmds.shadingNode('mib_data_string', asUtility=True)
    mentalrayDict['mib_data_string'] = 'render_unknown.png'

    def _mib_data_string_array(self):
        cmds.shadingNode('mib_data_string_array', asUtility=True)
    mentalrayDict['mib_data_string_array'] = 'render_unknown.png'

    def _mib_data_texture(self):
        cmds.shadingNode('mib_data_texture', asUtility=True)
    mentalrayDict['mib_data_texture'] = 'render_unknown.png'

    def _mib_data_texture_array(self):
        cmds.shadingNode('mib_data_texture_array', asUtility=True)
    mentalrayDict['mib_data_texture_array'] = 'render_unknown.png'

    def _mib_data_vector(self):
        cmds.shadingNode('mib_data_vector', asUtility=True)
    mentalrayDict['mib_data_vector'] = 'render_unknown.png'

    def _mib_data_vector_array(self):
        cmds.shadingNode('mib_data_vector_array', asUtility=True)
    mentalrayDict['mib_data_vector_array'] = 'render_unknown.png'

    def _mib_ptex_lookup(self):
        cmds.shadingNode('mib_ptex_lookup', asShader=True)
    mentalrayDict['mib_ptex_lookup'] = "render_unknown.png"

    def _misss_fast_skin_phen(self):
        cmds.shadingNode('misss_fast_skin_phen', asShader=True)
    mentalrayDict['misss_fast_skin_phen'] = "render_unknown.png"

    def _misss_fast_skin_phen_d(self):
        cmds.shadingNode('misss_fast_skin_phen_d', asShader=True)
    mentalrayDict['misss_fast_skin_phen_d'] = "render_unknown.png"

    def _misss_mia_skin2_phen(self):
        cmds.shadingNode('misss_mia_skin2_phen', asShader=True)
    mentalrayDict['misss_mia_skin2_phen'] = "render_unknown.png"

    def _misss_mia_skin2_phen_d(self):
        cmds.shadingNode('misss_mia_skin2_phen_d', asShader=True)
    mentalrayDict['misss_mia_skin2_phen_d'] = "render_unknown.png"

    def _writeToColorBuffer(self):
        cmds.shadingNode('writeToColorBuffer', asShader=True)
    mentalrayDict['writeToColorBuffer'] = "render_writeToColorBuffer.png"

    def _writeToDepthBuffer(self):
        cmds.shadingNode('writeToDepthBuffer', asShader=True)
    mentalrayDict['writeToDepthBuffer'] = "render_writeToDepthBuffer.png"

    def _writeToLabelBuffer(self):
        cmds.shadingNode('writeToLabelBuffer', asShader=True)
    mentalrayDict['writeToLabelBuffer'] = "render_writeToLabelBuffer.png"

    def _writeToVectorBuffer(self):
        cmds.shadingNode('writeToVectorBuffer', asShader=True)
    mentalrayDict['writeToVectorBuffer'] = "render_writeToVectorBuffer.png"
