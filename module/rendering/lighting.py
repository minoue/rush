import maya.mel as mel


# class name must be 'Commands'
class Commands(object):

    commandDict = {}

    def _transferMapWindow(self):
        mel.eval("performSurfaceSampling 1")
    commandDict['transferMapWindow'] = "menuIconShading.png"
    # ^ Don't forget to add the command to the dictionary.
