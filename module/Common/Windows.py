from maya import mel
from maya import cmds


commandDict = {}


###################
# General Editors #
###################


def contentBrowserWindow():
    cmds.ContentBrowserWindow()


def hypergraphHierarchyWindow():
    cmds.HypergraphHierarchyWindow()


def hypergraphDGWindow():
    cmds.HypergraphDGWindow()


def assetEditorWindow():
    cmds.AssetEditor()


def spreadSheetEditorWindow():
    cmds.SpreadSheetEditor()


def componentEditorWindow():
    cmds.ComponentEditor()


def connectionEditorWindow():
    cmds.ConnectionEditor()


def channelControlEditorWindow():
    cmds.ChannelControlEditor()


def filePathEditorWindow():
    cmds.FilePathEditor()


def namespaceEditorWindow():
    cmds.NamespaceEditor()


def scriptEditorWindow():
    cmds.ScriptEditor()


def commandShellWindow():
    cmds.CommandShell()


def profilerToolWindow():
    cmds.ProfilerTool()


####################
# Modeling Editors #
####################


def paintEffectsWindow():
    cmds.PaintEffectsWindow()


def textureViewWindow():
    cmds.TextureViewWindow()


def uvEditorWindow():
    cmds.TextureViewWindow()


def creaseSetEditorWindow():
    from maya.app.general import creaseSetEditor
    creaseSetEditor.showCreaseSetEditor()


#####################
# Animation Editors #
#####################


def graphEditorWindow():
    cmds.GraphEditor()


def timeEditorWindow():
    cmds.TimeEditorWindow()


def traxEditorWindow():
    cmds.CharacterAnimationEditor()


def sequenceEditorWindow():
    cmds.SequenceEditor()


def dopeSheetEditorWindow():
    cmds.DopeSheetEditor()


def quickRigEditorWindow():
    cmds.QuickRigEditor()


def humanIKWindow():
    cmds.HIKCharacterControlsTool()


def shapeEditorWindow():
    cmds.ShapeEditor()


def poseEditorWindow():
    cmds.PoseEditor()


def expressionEditorWindow():
    cmds.ExpressionEditor()


#####################
# Rendering Editors #
#####################


def renderViewWindow():
    cmds.RenderViewWindow()


def renderGlobalWindow():
    cmds.RenderGlobalsWindow()


def hypershadeWindow():
    cmds.HypershadeWindow()


def renderSetupWindow():
    cmds.RenderSetupWindow()


def lightEditorWindow():
    from maya.app.renderSetup.views import lightEditor
    lightEditor.editor.openEditorUI()


def customStereoRigEditorWindow():
    mel.eval("""stereoCameraCBwrapper("stereoRigToolEditor","customRigEditor()")""")


def renderFlagsWindow():
    cmds.RenderFlagsWindow()


def hardwareRenderBufferWindow():
    cmds.HardwareRenderBuffer()


########################
# Relationship Editors #
########################

def animationLayerWindow():
    cmds.AnimLayerRelationshipEditor()


def cameraSetEditorWindow():
    cmds.CameraSetEditor()


def characterSetEditorWindow():
    cmds.CharacterSetEditor()


def deformerSetEditorWindow():
    cmds.DeformerSetEditor()


def layerRelationshipEditorWindow():
    cmds.LayerRelationshipEditor()


def dynamicRelationshipEditorWindow():
    cmds.DynamicRelationshipEditor()


def lightLinkingWindow_LightCentric():
    cmds.LightCentricLightLinkingEditor()


def lightLinkingWindow_ObjectCentric():
    cmds.ObjectCentricLightLinkingEditor()


def partitionEditorWindow():
    cmds.PartitionEditor()


def renderPassSetEditorWindow():
    cmds.RenderPassSetEditor()


def setEditorWindow():
    cmds.SetEditor()


def uvLinkingWindow_textureCentric():
    cmds.TextureCentricUVLinkingEditor()


def uvLinkingWindow_uvCentric():
    cmds.UVCentricUVLinkingEditor()


################################
# Settings/Preferences Editors #
################################


def preferencesWindow():
    cmds.Preferences()


def performanceSettingsWindow():
    cmds.PerformanceSettingsWindow()


def hotkeyEditorWindow():
    cmds.HotkeyPreferencesWindow()


def colorSettingsWindow():
    cmds.ColorPreferencesWindow()


def markingMenuEditorWindow():
    cmds.MarkingMenuPreferencesWindow()


def shelfEditorWindow():
    cmds.ShelfPreferencesWindow()


def panelEditorWindow():
    cmds.PanelPreferencesWindow()


def pluginManagerWindow():
    cmds.PluginManager()


def outlinerWindow():
    cmds.OutlinerWindow()


def nodeEditorWindow():
    cmds.NodeEditorWindow()


def playblastWindow():
    cmds.PlayblastOptions()


commandDict['contentBrowserWindow'] = "menuIconWindow.png"
commandDict['hypergraphHierarchyWindow'] = "menuIconWindow.png"
commandDict['hypergraphDGWindow'] = "menuIconWindow.png"
commandDict['assetEditorWindow'] = "menuIconWindow.png"
commandDict['spreadSheetEditorWindow'] = "menuIconWindow.png"
commandDict['componentEditorWindow'] = "menuIconWindow.png"
commandDict['connectionEditorWindow'] = "menuIconWindow.png"
commandDict['channelControlEditorWindow'] = "menuIconWindow.png"
commandDict['filePathEditorWindow'] = "menuIconWindow.png"
commandDict['namespaceEditorWindow'] = "menuIconWindow.png"
commandDict['scriptEditorWindow'] = "cmdWndIcon.png"
commandDict['commandShellWindow'] = "menuIconWindow.png"
commandDict['profilerToolWindow'] = "menuIconWindow.png"
commandDict['paintEffectsWindow'] = "menuIconWindow.png"
commandDict['_textureViewWindow'] = "textureEditor.png"
commandDict['uvEditorWindow'] = "textureEditor.png"
commandDict['creaseSetEditor'] = "menuIconWindow.png"
commandDict['graphEditorWindow'] = "menuIconWindow.png"
commandDict['timeEditorWindow'] = "getCTE.png"
commandDict['traxEditorWindow'] = "menuIconWindow.png"
commandDict['sequenceEditorWindow'] = "menuIconWindow.png"
commandDict['dopeSheetEditorWindow'] = "menuIconWindow.png"
commandDict['quickRigEditorWindow'] = "QR_QuickRigTool.png"
commandDict['humanIKWindow'] = "humanIK_CharCtrl.png"
commandDict['shapeEditorWindow'] = "blendShapeEditor.png"
commandDict['poseEditorWindow'] = "poseEditor.png"
commandDict['expressionEditorWindow'] = "menuIconWindow.png"
commandDict['renderViewWindow'] = "rvOpenWindow.png"
commandDict['renderGlobalWindow'] = "menuIconWindow.png"
commandDict['hypershadeWindow'] = "hypershadeIcon.png"
commandDict['renderSetupWindow'] = "render_setup.png"
commandDict['lightEditorWindow'] = "lightEditor.png"
commandDict['customStereoRigEditorWindow'] = "viewStereoEditor.png"
commandDict['renderFlagsWindow'] = "menuIconWindow.png"
commandDict['hardwareRenderBufferWindow'] = "menuIconWindow.png"
commandDict['animationLayerWindow'] = "menuIconWindow.png"
commandDict['cameraSetEditorWindow'] = "menuIconWindow.png"
commandDict['characterSetEditorWindow'] = "menuIconWindow.png"
commandDict['deformerSetEditorWindow'] = "menuIconWindow.png"
commandDict['layerRelationshipEditorWindow'] = "menuIconWindow.png"
commandDict['dynamicRelationshipEditorWindow'] = "menuIconWindow.png"
commandDict['lightLinkingWindow_LightCentric'] = "menuIconWindow.png"
commandDict['lightLinkingWindow_ObjectCentric'] = "menuIconWindow.png"
commandDict['partitionEditorWindow'] = "menuIconWindow.png"
commandDict['renderPassSetEditorWindow'] = "menuIconWindow.png"
commandDict['setEditorWindow'] = "menuIconWindow.png"
commandDict['uvLinkingWindow_textureCentric'] = "menuIconWindow.png"
commandDict['uvLinkingWindow_uvCentric'] = "menuIconWindow.png"
commandDict['preferencesWindow'] = "menuIconWindow.png"
commandDict['performanceSettingsWindow'] = "menuIconWindow.png"
commandDict['hotkeyEditorWindow'] = "menuIconWindow.png"
commandDict['colorSettingsWindow'] = "menuIconWindow.png"
commandDict['markingMenuEditorWindow'] = "menuIconWindow.png"
commandDict['shelfEditorWindow'] = "menuIconWindow.png"
commandDict['panelEditorWindow'] = "menuIconWindow.png"
commandDict['pluginManagerWindow'] = "menuIconWindow.png"
commandDict['outlinerWindow'] = "menuIconWindow.png"
commandDict['nodeEditorWindow'] = "menuIconWindow.png"
commandDict['playblastWindow'] = "menuIconWindow.png"
