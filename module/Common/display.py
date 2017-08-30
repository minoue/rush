import maya.cmds as cmds
import maya.mel as mel


# class name must be 'Commands'
class Commands(object):

    commandDict = {}

    def _showAllHeadsup(self):
        toggle = 1
        mel.eval("setSelectDetailsVisibility(%s);" % toggle)
        mel.eval("setObjectDetailsVisibility(%s);" % toggle)
        mel.eval("setParticleCountVisibility(%s);" % toggle)
        mel.eval("setPolyCountVisibility(%s);" % toggle)
        mel.eval("setAnimationDetailsVisibility(%s);" % toggle)
        mel.eval("setHikDetailsVisibility(%s);" % toggle)
        mel.eval("setFrameRateVisibility(%s);" % toggle)
        mel.eval("setCurrentFrameVisibility(%s);" % toggle)
        mel.eval("setSceneTimecodeVisibility(%s);" % toggle)
        mel.eval("setCurrentContainerVisibility(%s);" % toggle)
        mel.eval("setViewportRendererVisibility(%s);" % toggle)
        mel.eval("setCameraNamesVisibility(%s);" % toggle)
        mel.eval("setFocalLengthVisibility(%s);" % toggle)
        mel.eval("setViewAxisVisibility(%s);" % toggle)
        if toggle == 1:
            cmds.viewManip(v=1)
        else:
            cmds.viewManip(v=0)
        cmds.ToggleOriginAxis()
    commandDict['showAllHeadsup'] = 'menuIconDisplay.png'

    def _hideAllHeadsup(self):
        toggle = 0
        mel.eval("setSelectDetailsVisibility(%s);" % toggle)
        mel.eval("setObjectDetailsVisibility(%s);" % toggle)
        mel.eval("setParticleCountVisibility(%s);" % toggle)
        mel.eval("setPolyCountVisibility(%s);" % toggle)
        mel.eval("setAnimationDetailsVisibility(%s);" % toggle)
        mel.eval("setHikDetailsVisibility(%s);" % toggle)
        mel.eval("setFrameRateVisibility(%s);" % toggle)
        mel.eval("setCurrentFrameVisibility(%s);" % toggle)
        mel.eval("setSceneTimecodeVisibility(%s);" % toggle)
        mel.eval("setCurrentContainerVisibility(%s);" % toggle)
        mel.eval("setViewportRendererVisibility(%s);" % toggle)
        mel.eval("setCameraNamesVisibility(%s);" % toggle)
        mel.eval("setFocalLengthVisibility(%s);" % toggle)
        mel.eval("setViewAxisVisibility(%s);" % toggle)
        if toggle == 1:
            cmds.viewManip(v=1)
        else:
            cmds.viewManip(v=0)
        cmds.ToggleOriginAxis()
    commandDict['hideAllHeadsup'] = 'menuIconDisplay.png'

    def _toggleComponentID_vertex(self):
        cmds.ToggleVertIDs()
    commandDict['toggleComponentID_vertex'] = 'menuIconDisplay.png'

    def _toggleComponentID_edge(self):
        cmds.ToggleEdgeIDs()
    commandDict['toggleComponentID_edge'] = 'menuIconDisplay.png'

    def _toggleComponentID_face(self):
        cmds.ToggleFaceIDs()
    commandDict['toggleComponentID_face'] = 'menuIconDisplay.png'

    def _toggleBorderEdges(self):
        cmds.ToggleBorderEdges()
    commandDict['toggleBorderEdges'] = 'menuIconDisplay.png'

    def _toggleCreaseEdges(self):
        cmds.ToggleCreaseEdges()
    commandDict['toggleCreaseEdges'] = 'menuIconDisplay.png'

    def _toggleTextureBorderEdges(self):
        cmds.ToggleTextureBorderEdges()
    commandDict['toggleTextureBorderEdges'] = 'menuIconDisplay.png'
