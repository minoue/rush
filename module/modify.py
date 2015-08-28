import maya.cmds as cmds


class Commands(object):

    #Name of dictionary must be this module name + 'Dict'
    modifyDict = {}

    def __init__(self):
        pass

    def _freezeAll(self):
        cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False)
    modifyDict['freezeAll'] = "menuIconModify.png"

    def _freezeOnlyTranslation(self):
        cmds.makeIdentity(apply=True, t=True, r=False, s=False, n=False)
    modifyDict['freezeOnlyTranslation'] = "menuIconModify.png"

    def _freezeOnlyRotation(self):
        cmds.makeIdentity(apply=True, t=False, r=True, s=False, n=False)
    modifyDict['freezeOnlyRotation'] = "menuIconModify.png"

    def _freezeOnlyScale(self):
        cmds.makeIdentity(apply=True, t=False, r=False, s=True, n=False)
    modifyDict['freezeOnlyScale'] = "menuIconModify.png"
