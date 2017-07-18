from maya import cmds


class Commands(object):
    """ class name must be 'Commands' """

    commandDict = {}

    def _loadObjPlugin(self):
        if not cmds.pluginInfo("objExport", q=True, loaded=True):
            cmds.loadPlugin("objExport")
    commandDict['loadObjPlugin'] = "sphere.png"
    # ^ Don't forget to add the command to the dictionary.
