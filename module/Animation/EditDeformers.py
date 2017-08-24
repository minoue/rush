import maya.cmds as cmds
import maya.mel as mel


class Commands(object):

    commandDict = {}

    def _editPaintBlendShapeWeightsTool(self):
        cmds.ArtPaintBlendShapeWeightsTool()
    commandDict['editPaintBlendShapeWeightsTool'] = "paintBlendshape.png"   

    def _editPaintBlendShapeWeightsToolOptions(self):
        cmds.ArtPaintBlendShapeWeightsToolOptions()
    commandDict['editPaintBlendShapeWeightsToolOptions'] = "paintBlendshape.png"   

    def _paintClusterWeights(self):
        mel.eval('artAttrToolScript 4 "cluster"')
    commandDict['paintClusterWeights'] = "paintCluster.png"
