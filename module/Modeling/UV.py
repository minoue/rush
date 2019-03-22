from maya import cmds
from maya import mel


# class name must be 'Commands'
class Commands(object):

    commandDict = {}

    def _uvTextureEditor(self):
        cmds.TextureViewWindow()
    commandDict['uvTextureEditor'] = "textureEditor.png"

    def _uVSetEditor(self):
        cmds.UVSetEditor()
    commandDict['uVSetEditor'] = "sphere.png"

    def _uvProjection_automatic(self):
        mel.eval("performPolyAutoProj 0")
    commandDict['uvProjection_automatic'] = "polyAutoProj.png"

    def _uvProjection_automatic_options(self):
        mel.eval("performPolyAutoProj 1")
    commandDict['uvProjection_automatic_options'] = "polyAutoProj.png"

    def _bestPlaneTexturingTool(self):
        mel.eval("setToolTo polyBestPlaneTexturingContext")
    commandDict['bestPlaneTexturingTool'] = "bestPlaneTxt.png"

    def _uvProjection_cameraBased(self):
        mel.eval("polyProjection -type Planar -md p ")
    commandDict['uvProjection_cameraBased'] = "polyCameraUVs.png"

    def _uvProjection_cameraBased_options(self):
        mel.eval('performPolyForceUVArgList "1" {"1", "camera", "ls -selection", "0"} "" ')
    commandDict['uvProjection_cameraBased_options'] = "polyCameraUVs.png"
