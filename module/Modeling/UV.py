from maya import cmds
from maya import mel


commandDict = {}


def uvTextureEditor():
    cmds.TextureViewWindow()


def uVSetEditor():
    cmds.UVSetEditor()


def uvProjection_automatic():
    mel.eval("performPolyAutoProj 0")


def uvProjection_automatic_options():
    mel.eval("performPolyAutoProj 1")


def bestPlaneTexturingTool():
    mel.eval("setToolTo polyBestPlaneTexturingContext")


def uvProjection_cameraBased():
    mel.eval("polyProjection -type Planar -md p ")


def uvProjection_cameraBased_options():
    mel.eval('performPolyForceUVArgList "1" {"1", "camera", "ls -selection", "0"} "" ')


commandDict['uvTextureEditor'] = "textureEditor.png"
commandDict['uVSetEditor'] = "sphere.png"
commandDict['uvProjection_automatic'] = "polyAutoProj.png"
commandDict['uvProjection_automatic_options'] = "polyAutoProj.png"
commandDict['bestPlaneTexturingTool'] = "bestPlaneTxt.png"
commandDict['uvProjection_cameraBased'] = "polyCameraUVs.png"
commandDict['uvProjection_cameraBased_options'] = "polyCameraUVs.png"
