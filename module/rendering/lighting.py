# import maya.cmds as cmds
import maya.mel as mel


# class name must be 'Commands'
class Commands(object):

    # Name of dictionary must be this module name + 'Dict'
    lightingDict = {}

    def __init__(self):
        pass

    def _transferMapWindow(self):
        print "Hello World"
        mel.eval("performSurfaceSampling 1")
    lightingDict['transferMapWindow'] = "menuIconShading.png"
    # ^ Don't forget to add the command to the dictionary.
