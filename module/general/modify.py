import maya.cmds as cmds


class Commands(object):

    commandDict = {}

    def _freezeAll(self):
        cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False)
    commandDict['freezeAll'] = "menuIconModify.png"

    def _freezeOnlyTranslation(self):
        cmds.makeIdentity(apply=True, t=True, r=False, s=False, n=False)
    commandDict['freezeOnlyTranslation'] = "menuIconModify.png"

    def _freezeOnlyRotation(self):
        cmds.makeIdentity(apply=True, t=False, r=True, s=False, n=False)
    commandDict['freezeOnlyRotation'] = "menuIconModify.png"

    def _freezeOnlyScale(self):
        cmds.makeIdentity(apply=True, t=False, r=False, s=True, n=False)
    commandDict['freezeOnlyScale'] = "menuIconModify.png"
