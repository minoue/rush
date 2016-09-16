from maya import cmds


class Commands(object):
    """ class name must be 'Commands' """

    commandDict = {}

    # Export
    def _exportSelection(self):
        cmds.ExportSelection()
    commandDict['exportSelection'] = "menuIconFile.png"

    def _exportSelectionOptions(self):
        cmds.ExportSelectionOptions()
    commandDict['exportSelectionOptions'] = "menuIconFile.png"

    def _exportAll(self):
        cmds.Export()
    commandDict['exportAll'] = "menuIconFile.png"

    def _exportAllOptions(self):
        cmds.ExportOptions()
    commandDict['exportAllOptions'] = "menuIconFile.png"

    def _import(self):
        cmds.Import()
    commandDict['import'] = "menuIconFile.png"

    def _importOptions(self):
        cmds.ImportOptions()
    commandDict['importOptions'] = "menuIconFile.png"
