import maya.cmds as cmds
import maya.mel as mel


# class name must be 'Commands'
class Commands(object):

    commandDict = {}

    def _applyColor(self):
        mel.eval("polyColorPerVertex -r 0.5 -g 0.5 -b 0.5 -a 1 -cdo;")
    commandDict['applyColor'] = "polyApplyColor.png"

    def _paintVertexColorTool(self):
        cmds.PaintVertexColorTool()
    commandDict['paintVertexColorTool'] = "paintVertexColour.png"

    def _createEmptyColorSet(self):
        mel.eval("colorSetEditCmdNew new none 1 RGB 0")
    commandDict['createEmptyColorSet'] = "polyColorSetCreateEmpty.png"

    def _deleteCurrentColorSet(self):
        mel.eval("colorSetEditCmd delete none")
    commandDict['deleteCurrentColorSet'] = "polyColorSetDelete.png"

    def _renameCurrentColorSet(self):
        mel.eval("colorSetEditCmd rename none")
    commandDict['renameCurrentColorSet'] = "polyColorSetRename.png"

    def _modifyCurrentColorSet(self):
        mel.eval("colorSetEditCmd modify none")
    commandDict['modifyCurrentColorSet'] = "polyColorSetModify.png"

    def _colorSetEditor(self):
        mel.eval("colorSetEditor")
    commandDict['colorSetEditor'] = "polyColorSetEditor.png"
