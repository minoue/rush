import maya.cmds as cmds
import maya.mel as mel


class Commands(object):

    commandDict = {}

    # ############################# #
    # ####### General Editor ###### #
    # ############################# #

    def _componentEditor(self):
        cmds.ComponentEditor()
    commandDict['componentEditor'] = "menuIconWindow.png"

    def _spreadSheetEditor(self):
        cmds.SpreadSheetEditor()
    commandDict['spreadSheetEditor'] = "menuIconWindow.png"

    def _connectionEditor(self):
        cmds.ConnectionEditor()
    commandDict['connectionEditor'] = "menuIconWindow.png"

    def _visorWindow(self):
        cmds.VisorWindow()
    commandDict['visorWindow'] = "menuIconWindow.png"

    def _displayLayerEditor(self):
        cmds.DisplayLayerEditorWindow()
    commandDict['displayLayerEditor'] = "menuIconWindow.png"

    def _assetEditor(self):
        cmds.AssetEditor()
    commandDict['assetEditor'] = "menuIconWindow.png"

    def _namespaceEditor(self):
        cmds.NamespaceEditor()
    commandDict['namespaceEditor'] = "menuIconWindow.png"

    def _filePathEditor(self):
        cmds.FilePathEditor()
    commandDict['filePathEditor'] = "menuIconWindow.png"

    def _scriptEditor(self):
        cmds.ScriptEditor()
    commandDict['scriptEditor'] = "menuIconWindow.png"

    def _commandShell(self):
        cmds.CommandShell()
    commandDict['commandShell'] = "menuIconWindow.png"

    def _channelControlEditor(self):
        cmds.ChannelControlEditor()
    commandDict['channelControlEditor'] = "menuIconWindow.png"

    # ############################# #
    # ###### Rendering editor ##### #
    # ############################# #

    def _customStereoRigEditor(self):
        mel.eval(
            'stereoCameraCBwrapper(\
                "stereoRigToolEditor","customRigEditor()");')
    commandDict['customStereoRigEditor'] = "menuIconWindow.png"

    def _renderingFlags(self):
        cmds.RenderFlagsWindow()
    commandDict['renderingFlags'] = "menuIconWindow.png"

    def _renderViewWindow(self):
        cmds.RenderViewWindow()
    commandDict['renderViewWindow'] = "menuIconWindow.png"

    def _hyperShade(self):
        cmds.HypershadeWindow()
    commandDict['hyperShade'] = "menuIconWindow.png"

    def _mentalRayApproxEditor(self):
        cmds.MentalRayApproxEditor()
    commandDict['mentalRayApproxEditor'] = "menuIconWindow.png"

    def _mentalRayCustomTextEditor(self):
        cmds.MentalRayCustomTextEditor()
    commandDict['mentalRayCustomTextEditor'] = "menuIconWindow.png"

    def _mentalRayMapVisualizer(self):
        cmds.mrMapVisualizer()
    commandDict['mentalRayMapVisualizer'] = "menuIconWindow.png"

    def _mentalRayShaderManager(self):
        cmds.mrShaderManager()
    commandDict['mentalRayShaderManager'] = "menuIconWindow.png"

    # ############################# #
    # ###### Animation editor ##### #
    # ############################# #

    def _graphEditor(self):
        cmds.GraphEditor()
    commandDict['graphEditor'] = "menuIconWindow.png"

    def _traxEditor(self):
        cmds.CharacterAnimationEditor()
    commandDict['traxEditor'] = "menuIconWindow.png"

    def _cameraSequenceEditor(self):
        cmds.SequenceEditor()
    commandDict['cameraSequenceEditor'] = "menuIconWindow.png"

    def _dopeSheetEditor(self):
        cmds.DopeSheetEditor()
    commandDict['dopeSheetEditor'] = "menuIconWindow.png"

    def _humanIK(self):
        cmds.HIKCharacterControlsTool()
    commandDict['humanIK'] = "menuIconWindow.png"

    def _blendShapeEditor(self):
        cmds.BlendShapeEditor()
    commandDict['blendShapeEditor'] = "menuIconWindow.png"

    def _expressionEditor(self):
        cmds.ExpressionEditor()
    commandDict['expressionEditor'] = "menuIconWindow.png"

    # ############################# #
    # ###### Rendering editor ##### #
    # ############################# #
    def _setsEditor(self):
        cmds.SetEditor()
    commandDict['setsEditor'] = "menuIconWindow.png"

    def _deformerSetEditor(self):
        cmds.DeformerSetEditor()
    commandDict['deformerSetEditor'] = "menuIconWindow.png"

    def _characterSetEditor(self):
        cmds.CharacterSetEditor()
    commandDict['characterSetEditor'] = "menuIconWindow.png"

    def _partitionEditor(self):
        cmds.PartitionEditor()
    commandDict['partitionEditor'] = "menuIconWindow.png"

    def _layerRelationshipEditor(self):
        cmds.LayerRelationshipEditor()
    commandDict['layerRelationshipEditor'] = "menuIconWindow.png"

    def _renderLayerRelationshipEditor(self):
        cmds.RenderLayerRelationshipEditor()
    commandDict['renderLayerRelationshipEditor'] = "menuIconWindow.png"

    def _cameraSetEditor(self):
        cmds.CameraSetEditor()
    commandDict['cameraSetEditor'] = "menuIconWindow.png"

    def _renderPassSetEditor(self):
        cmds.RenderPassSetEditor()
    commandDict['renderPassSetEditor'] = "menuIconWindow.png"

    def _animationLayerRelationshipEditor(self):
        cmds.AnimLayerRelationshipEditor()
    commandDict['animationLayerRelationshipEditor'] = "menuIconWindow.png"

    def _dynamicRelationshipEditor(self):
        cmds.DynamicRelationshipEditor()
    commandDict['dynamicRelationshipEditor'] = "menuIconWindow.png"

    def _lightCentricLightLinkingEditor(self):
        cmds.LightCentricLightLinkingEditor()
    commandDict['lightCentricLightLinkingEditor'] = "menuIconWindow.png"

    def _objectCentricLightLinkingEditor(self):
        cmds.ObjectCentricLightLinkingEditor()
    commandDict['objectCentricLightLinkingEditor'] = "menuIconWindow.png"

    def _textureCentricUVLinkingEditor(self):
        cmds.TextureCentricUVLinkingEditor()
    commandDict['textureCentricUVLinkingEditor'] = "menuIconWindow.png"

    def _uVCentricUVLinkingEditor(self):
        cmds.UVCentricUVLinkingEditor()
    commandDict['uVCentricUVLinkingEditor'] = "menuIconWindow.png"

    def _pFXUVSetLinkingEditor(self):
        cmds.PFXUVSetLinkingEditor()
    commandDict['pFXUVSetLinkingEditor'] = "menuIconWindow.png"

    def _hairUVSetLinkingEditor(self):
        cmds.HairUVSetLinkingEditor()
    commandDict['hairUVSetLinkingEditor'] = "menuIconWindow.png"

    # ################################## #
    # ###### Setting / Preference ###### #
    # ################################## #

    def _preferencesWindow(self):
        cmds.PreferencesWindow()
    commandDict['preferencesWindow'] = "menuIconWindow.png"

    def _hotkeyEditor(self):
        cmds.HotkeyPreferencesWindow()
    commandDict['hotkeyEditor'] = "menuIconWindow.png"

    def _pluginManager(self):
        cmds.PluginManager()
    commandDict['pluginManager'] = "menuIconWindow.png"

    # OTHER
    def _blindDataEditor(self):
        cmds.BlindDataEditor()
    commandDict['blindDataEditor'] = "menuIconWindow.png"

    def _attributeEditor(self):
        cmds.AttributeEditor()
    commandDict['attributeEditor'] = "menuIconWindow.png"

    def _nodeEditorWindow(self):
        cmds.NodeEditorWindow()
    commandDict['nodeEditorWindow'] = "menuIconWindow.png"

    def _createNodeWindow(self):
        cmds.CreateNodeWindow()
    commandDict['createNodeWindow'] = "menuIconWindow.png"

    def _hyperGraphHierarchy(self):
        cmds.HypergraphHierarchyWindow()
    commandDict['hyperGraphHierarchy'] = "menuIconWindow.png"

    def _hyperGraphDG(self):
        cmds.HypergraphDGWindow()
    commandDict['hyperGraphDG'] = "menuIconWindow.png"

    def _playBlastOptions(self):
        cmds.PlayblastOptions()
    commandDict['playBlastOptions'] = "menuIconWindow.png"
