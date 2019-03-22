from maya import mel
from maya import cmds


class Commands(object):
    """ class name must be 'Commands' """

    commandDict = {}

    ###################
    # General Editors #
    ###################

    def _contentBrowserWindow(self):
        cmds.ContentBrowserWindow()
    commandDict['contentBrowserWindow'] = "menuIconWindow.png"

    def _hypergraphHierarchyWindow(self):
        cmds.HypergraphHierarchyWindow()
    commandDict['hypergraphHierarchyWindow'] = "menuIconWindow.png"

    def _hypergraphDGWindow(self):
        cmds.HypergraphDGWindow()
    commandDict['hypergraphDGWindow'] = "menuIconWindow.png"

    def _assetEditorWindow(self):
        cmds.AssetEditor()
    commandDict['assetEditorWindow'] = "menuIconWindow.png"

    def _spreadSheetEditorWindow(self):
        cmds.SpreadSheetEditor()
    commandDict['spreadSheetEditorWindow'] = "menuIconWindow.png"

    def _componentEditorWindow(self):
        cmds.ComponentEditor()
    commandDict['componentEditorWindow'] = "menuIconWindow.png"

    def _connectionEditorWindow(self):
        cmds.ConnectionEditor()
    commandDict['connectionEditorWindow'] = "menuIconWindow.png"

    def _channelControlEditorWindow(self):
        cmds.ChannelControlEditor()
    commandDict['channelControlEditorWindow'] = "menuIconWindow.png"

    def _filePathEditorWindow(self):
        cmds.FilePathEditor()
    commandDict['filePathEditorWindow'] = "menuIconWindow.png"

    def _namespaceEditorWindow(self):
        cmds.NamespaceEditor()
    commandDict['namespaceEditorWindow'] = "menuIconWindow.png"

    def _scriptEditorWindow(self):
        cmds.ScriptEditor()
    commandDict['scriptEditorWindow'] = "cmdWndIcon.png"

    def _commandShellWindow(self):
        cmds.CommandShell()
    commandDict['commandShellWindow'] = "menuIconWindow.png"

    def _profilerToolWindow(self):
        cmds.ProfilerTool()
    commandDict['profilerToolWindow'] = "menuIconWindow.png"

    ####################
    # Modeling Editors #
    ####################

    def _paintEffectsWindow(self):
        cmds.PaintEffectsWindow()
    commandDict['paintEffectsWindow'] = "menuIconWindow.png"

    def _textureViewWindow(self):
        cmds.TextureViewWindow()
    commandDict['_textureViewWindow'] = "textureEditor.png"

    def _uvEditorWindow(self):
        cmds.TextureViewWindow()
    commandDict['uvEditorWindow'] = "textureEditor.png"

    def _creaseSetEditorWindow(self):
        from maya.app.general import creaseSetEditor
        creaseSetEditor.showCreaseSetEditor()
    commandDict['creaseSetEditor'] = "menuIconWindow.png"

    #####################
    # Animation Editors #
    #####################

    def _graphEditorWindow(self):
        cmds.GraphEditor()
    commandDict['graphEditorWindow'] = "menuIconWindow.png"

    def _timeEditorWindow(self):
        cmds.TimeEditorWindow()
    commandDict['timeEditorWindow'] = "getCTE.png"

    def _traxEditorWindow(self):
        cmds.CharacterAnimationEditor()
    commandDict['traxEditorWindow'] = "menuIconWindow.png"

    def _sequenceEditorWindow(self):
        cmds.SequenceEditor()
    commandDict['sequenceEditorWindow'] = "menuIconWindow.png"

    def _dopeSheetEditorWindow(self):
        cmds.DopeSheetEditor()
    commandDict['dopeSheetEditorWindow'] = "menuIconWindow.png"

    def _quickRigEditorWindow(self):
        cmds.QuickRigEditor()
    commandDict['quickRigEditorWindow'] = "QR_QuickRigTool.png"

    def _humanIKWindow(self):
        cmds.HIKCharacterControlsTool()
    commandDict['humanIKWindow'] = "humanIK_CharCtrl.png"

    def _shapeEditorWindow(self):
        cmds.ShapeEditor()
    commandDict['shapeEditorWindow'] = "blendShapeEditor.png"

    def _poseEditorWindow(self):
        cmds.PoseEditor()
    commandDict['poseEditorWindow'] = "poseEditor.png"

    def _expressionEditorWindow(self):
        cmds.ExpressionEditor()
    commandDict['expressionEditorWindow'] = "menuIconWindow.png"

    #####################
    # Rendering Editors #
    #####################

    def _renderViewWindow(self):
        cmds.RenderViewWindow()
    commandDict['renderViewWindow'] = "rvOpenWindow.png"

    def _renderGlobalWindow(self):
        cmds.RenderGlobalsWindow()
    commandDict['renderGlobalWindow'] = "menuIconWindow.png"

    def _hypershadeWindow(self):
        cmds.HypershadeWindow()
    commandDict['hypershadeWindow'] = "hypershadeIcon.png"

    def _renderSetupWindow(self):
        cmds.RenderSetupWindow()
    commandDict['renderSetupWindow'] = "render_setup.png"

    def _lightEditorWindow(self):
        from maya.app.renderSetup.views import lightEditor
        lightEditor.editor.openEditorUI()
    commandDict['lightEditorWindow'] = "lightEditor.png"

    def _customStereoRigEditorWindow(self):
        mel.eval("""stereoCameraCBwrapper("stereoRigToolEditor","customRigEditor()")""")
    commandDict['customStereoRigEditorWindow'] = "viewStereoEditor.png"

    def _renderFlagsWindow(self):
        cmds.RenderFlagsWindow()
    commandDict['renderFlagsWindow'] = "menuIconWindow.png"

    def _hardwareRenderBufferWindow(self):
        cmds.HardwareRenderBuffer()
    commandDict['hardwareRenderBufferWindow'] = "menuIconWindow.png"

    ########################
    # Relationship Editors #
    ########################

    def _animationLayerWindow(self):
        cmds.AnimLayerRelationshipEditor()
    commandDict['animationLayerWindow'] = "menuIconWindow.png"

    def _cameraSetEditorWindow(self):
        cmds.CameraSetEditor()
    commandDict['cameraSetEditorWindow'] = "menuIconWindow.png"

    def _characterSetEditorWindow(self):
        cmds.CharacterSetEditor()
    commandDict['characterSetEditorWindow'] = "menuIconWindow.png"

    def _deformerSetEditorWindow(self):
        cmds.DeformerSetEditor()
    commandDict['deformerSetEditorWindow'] = "menuIconWindow.png"

    def _layerRelationshipEditorWindow(self):
        cmds.LayerRelationshipEditor()
    commandDict['layerRelationshipEditorWindow'] = "menuIconWindow.png"

    def _dynamicRelationshipEditorWindow(self):
        cmds.DynamicRelationshipEditor()
    commandDict['dynamicRelationshipEditorWindow'] = "menuIconWindow.png"

    def _lightLinkingWindow_LightCentric(self):
        cmds.LightCentricLightLinkingEditor()
    commandDict['lightLinkingWindow_LightCentric'] = "menuIconWindow.png"

    def _lightLinkingWindow_ObjectCentric(self):
        cmds.ObjectCentricLightLinkingEditor()
    commandDict['lightLinkingWindow_ObjectCentric'] = "menuIconWindow.png"

    def _partitionEditorWindow(self):
        cmds.PartitionEditor()
    commandDict['partitionEditorWindow'] = "menuIconWindow.png"

    def _renderPassSetEditorWindow(self):
        cmds.RenderPassSetEditor()
    commandDict['renderPassSetEditorWindow'] = "menuIconWindow.png"

    def _setEditorWindow(self):
        cmds.SetEditor()
    commandDict['setEditorWindow'] = "menuIconWindow.png"

    def _uvLinkingWindow_textureCentric(self):
        cmds.TextureCentricUVLinkingEditor()
    commandDict['uvLinkingWindow_textureCentric'] = "menuIconWindow.png"

    def _uvLinkingWindow_uvCentric(self):
        cmds.UVCentricUVLinkingEditor()
    commandDict['uvLinkingWindow_uvCentric'] = "menuIconWindow.png"

    ################################
    # Settings/Preferences Editors #
    ################################

    def _preferencesWindow(self):
        cmds.Preferences()
    commandDict['preferencesWindow'] = "menuIconWindow.png"

    def _performanceSettingsWindow(self):
        cmds.PerformanceSettingsWindow()
    commandDict['performanceSettingsWindow'] = "menuIconWindow.png"

    def _hotkeyEditorWindow(self):
        cmds.HotkeyPreferencesWindow()
    commandDict['hotkeyEditorWindow'] = "menuIconWindow.png"

    def _colorSettingsWindow(self):
        cmds.ColorPreferencesWindow()
    commandDict['colorSettingsWindow'] = "menuIconWindow.png"

    def _markingMenuEditorWindow(self):
        cmds.MarkingMenuPreferencesWindow()
    commandDict['markingMenuEditorWindow'] = "menuIconWindow.png"

    def _shelfEditorWindow(self):
        cmds.ShelfPreferencesWindow()
    commandDict['shelfEditorWindow'] = "menuIconWindow.png"

    def _panelEditorWindow(self):
        cmds.PanelPreferencesWindow()
    commandDict['panelEditorWindow'] = "menuIconWindow.png"

    def _pluginManagerWindow(self):
        cmds.PluginManager()
    commandDict['pluginManagerWindow'] = "menuIconWindow.png"

    def _outlinerWindow(self):
        cmds.OutlinerWindow()
    commandDict['outlinerWindow'] = "menuIconWindow.png"

    def _nodeEditorWindow(self):
        cmds.NodeEditorWindow()
    commandDict['nodeEditorWindow'] = "menuIconWindow.png"

    def _playblastWindow(self):
        cmds.PlayblastOptions()
    commandDict['playblastWindow'] = "menuIconWindow.png"
