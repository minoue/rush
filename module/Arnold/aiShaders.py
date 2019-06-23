from __future__ import print_function
from maya import cmds


commandDict = {}


def aiStandardSurface():
	cmds.shadingNode("aiStandardSurface", asShader=True)


commandDict['aiStandardSurface'] = "AreaLightShelf.png"
