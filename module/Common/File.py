from maya import cmds


commandDict = {}


def newScene():
    cmds.NewScene()
commandDict['newScene'] = 'menuIconFile.png'


def newSceneOptions():
    cmds.NewSceneOptions()
commandDict['newSceneOptions'] = 'menuIconFile.png'


def openScene():
    cmds.OpenScene()
commandDict['openScene'] = 'menuIconFile.png'


def openSceneOptions():
    cmds.OpenSceneOptions()
commandDict['openSceneOptions'] = 'menuIconFile.png'


def saveScene():
    cmds.SaveScene()
commandDict['saveScene'] = 'menuIconFile.png'


def saveSceneOptions():
    cmds.SaveSceneOptions()
commandDict['saveSceneOptions'] = 'menuIconFile.png'


def saveSceneAs():
    cmds.SaveSceneAs()
commandDict['saveSceneAs'] = 'menuIconFile.png'


def saveSceneAsOptions():
    cmds.SaveSceneAsOptions()
commandDict['saveSceneAsOptions'] = 'menuIconFile.png'


def incrementAndSave():
    cmds.IncrementAndSave()
commandDict['incrementAndSave'] = 'menuIconFile.png'


def archiveScene():
    cmds.ArchiveScene()
commandDict['archiveScene'] = 'menuIconFile.png'


def archiveSceneOptions():
    cmds.ArchiveSceneOptions()
commandDict['archiveSceneOptions'] = 'menuIconFile.png'


def savePreferences():
    cmds.SavePreferences()
commandDict['savePreferences'] = 'menuIconFile.png'


def optimizeSceneOptions():
    cmds.OptimizeSceneOptions()
commandDict['optimizeSceneOptions'] = 'menuIconFile.png'


def fileImport():
    cmds.Import()
commandDict['import'] = 'menuIconFile.png'


def fileImportOptions():
    cmds.ImportOptions()
commandDict['importOptions'] = 'menuIconFile.png'


def fileExportAll():
    cmds.Export()
commandDict['export'] = 'menuIconFile.png'


def fileExportAllOptions():
    cmds.ExportOptions()
commandDict['exportOptions'] = 'menuIconFile.png'


def fileExportSelection():
    cmds.ExportSelection()
commandDict['exportSelection'] = 'menuIconFile.png'


def fileExportSelectionOptions():
    cmds.ExportSelectionOptions()
commandDict['exportSelectionOptions'] = 'menuIconFile.png'


def createReference():
    cmds.CreateReference()
commandDict['createReference'] = 'menuIconFile.png'


def createReferenceOptions():
    cmds.CreateReferenceOptions()
commandDict['createReferenceOptions'] = 'menuIconFile.png'


def referenceEditor():
    cmds.ReferenceEditor()
commandDict['referenceEditor'] = 'menuIconFile.png'
