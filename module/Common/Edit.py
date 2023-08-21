from maya import cmds


commandDict = {}


def undo():
    cmds.Undo()


commandDict['undo'] = 'menuIconEdit.png'


def redo():
    cmds.Redo()


commandDict['redo'] = 'menuIconEdit.png'


def repeatLast():
    cmds.RepeatLast()


commandDict['repeatLast'] = 'menuIconEdit.png'


def recentCommandWindow():
    cmds.RecentCommandsWindow()


commandDict['recentCommandWindow'] = 'menuIconEdit.png'


def deleteHistory():
    cmds.DeleteHistory()


commandDict['deleteHistory'] = 'menuIconEdit.png'


def deleteNonDeformerHistory():
    cmds.BakeNonDefHistory()


commandDict['deleteNonDeformerHistory'] = 'menuIconEdit.png'


def deleteAllHistory():
    cmds.DeleteAllHistory()


commandDict['deleteAllHistory'] = 'menuIconEdit.png'


def deleteAllNonDeformerHistory():
    cmds.BakeAllNonDefHistory()


commandDict['deleteAllNonDeformerHistory'] = 'menuIconEdit.png'


def duplicate():
    cmds.Duplicate()


commandDict['duplicate'] = 'menuIconEdit.png'


def duplicateSpecial():
    cmds.DuplicateSpecial()


commandDict['duplicateSpecial'] = 'menuIconEdit.png'


def duplicateSpecialOptions():
    cmds.DuplicateSpecialOptions()


commandDict['duplicateSpecialOptions'] = 'menuIconEdit.png'


def duplicateWithTransform():
    cmds.DuplicateWithTransform()


commandDict['duplicateWithTransform'] = 'menuIconEdit.png'


def transferAttributeValues():
    cmds.TransferAttributeValues()


commandDict['transferAttributeValues'] = 'menuIconEdit.png'


def transferAttributeValuesOptions():
    cmds.TransferAttributeValuesOptions()


commandDict['transferAttributeValuesOptions'] = 'menuIconEdit.png'


def group():
    cmds.Group()


commandDict['group'] = 'menuIconEdit.png'


def groupOptions():
    cmds.GroupOptions()


commandDict['groupOptions'] = 'menuIconEdit.png'


def ungroup():
    cmds.Ungroup()


commandDict['ungroup'] = 'menuIconEdit.png'


def ungroupOptions():
    cmds.UngroupOptions()


commandDict['ungroupOptions'] = 'menuIconEdit.png'


def parent():
    cmds.Parent()


commandDict['parent'] = 'menuIconEdit.png'


def parentOptions():
    cmds.ParentOptions()


commandDict['parentOptions'] = 'menuIconEdit.png'


def unparent():
    cmds.Unparent()


commandDict['unparent'] = 'menuIconEdit.png'


def unparentOptions():
    cmds.UnparentOptions()


commandDict['unparentOptions'] = 'menuIconEdit.png'
