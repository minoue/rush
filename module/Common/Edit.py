from maya import cmds
from maya import mel


commandDict = {}


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
