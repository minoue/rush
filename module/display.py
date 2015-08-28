import maya.cmds as cmds


# class name must be 'Commands'
class Commands(object):

    #Name of dictionary must be this module name + 'Dict'
    displayDict = {}

    def __init__(self):
        pass

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
    displayDict['showAllHeadsup'] = 'menuIconDisplay.png'

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
    displayDict['hideAllHeadsup'] = 'menuIconDisplay.png'

    def _toggleVertexIDs(self):
        cmds.ToggleVertIDs()
    displayDict['toggleVertexIDs'] = 'menuIconDisplay.png'

    def _toggleEdgeIDs(self):
        cmds.ToggleEdgeIDs()
    displayDict['toggleEdgeIDs'] = 'menuIconDisplay.png'

    def _toggleFaceIDs(self):
        cmds.ToggleFaceIDs()
    displayDict['toggleFaceIDs'] = 'menuIconDisplay.png'

    def _toggleCompIDs(self):
        cmds.ToggleCompIDs()
    displayDict['toggleCompIDs'] = 'menuIconDisplay.png'

