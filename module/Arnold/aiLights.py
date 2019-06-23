from __future__ import print_function
from maya import cmds
import mtoa


commandDict = {}


def aiAreaLight():
	mtoa.utils.createLocator("aiAreaLight", asLight=True)


commandDict['aiAreaLight'] = "AreaLightShelf.png"


def aiSkyDomeLight():
    mtoa.utils.createLocator("aiSkyDomeLight", asLight=True)


commandDict['aiSkyDomeLight'] = "SkydomeLightShelf.png"


def aiMeshLight():
	mtoa.utils.createMeshLight()


commandDict['aiMeshLight'] = "MeshLightShelf.png"


def aiPhotometricLight():
	mtoa.utils.createLocator("aiPhotometricLight", asLight=True)


commandDict['aiPhotometricLight'] = "PhotometricLightShelf.png"


def aiLightPortal():
	mtoa.ui.arnoldmenu.doCreateLightPortal()


commandDict['aiLightPortal'] = "LightPortalShelf.png"


def aiPhysicalSky():
	mtoa.ui.arnoldmenu.doCreatePhysicalSky()


commandDict['aiPhysicalSky'] = "PhysicalSkyShelf.png"
