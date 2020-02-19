from maya import cmds
from maya import mel


commandDict = {}


def openAlembic():
    cmds.AlembicOpen()
commandDict['openAlembic'] = 'commandButton.png'

def referenceAlembic():
    mel.eval("""projectViewer AlembicReference;""")
commandDict['referenceAlembic'] = 'commandButton.png'

def referenceAlembicOptions():
    cmds.CreateReferenceOptions()
commandDict['referenceAlembicOptions'] = 'commandButton.png'

def importAlembic():
    cmds.AlembicImport()
commandDict['importAlembic'] = 'commandButton.png'

def importAlembicOptions():
    cmds.AlembicImportOptions()
commandDict['importAlembicOptions'] = 'commandButton.png'

def replaceAlembic():
    cmds.AlembicReplace()
commandDict['replaceAlembic'] = 'commandButton.png'

def exportAllToAlembic():
    cmds.AlembicExportAll()
commandDict['exportAllToAlembic'] = 'commandButton.png'

def exportAllToAlembicOptions():
    cmds.AlembicExportAllOptions()
commandDict['exportAllToAlembicOptions'] = 'commandButton.png'

def exportSelectionToAlembic():
    cmds.AlembicExportSelection()
commandDict['exportSelectionToAlembic'] = 'commandButton.png'

def exportSelectionToAlembicOptions():
    cmds.AlembicExportSelectionOptions()
commandDict['exportSelectionToAlembicOptions'] = 'commandButton.png'