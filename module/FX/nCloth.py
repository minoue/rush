from maya import cmds
from maya import mel


class Commands(object):
    """ class name must be 'Commands' """

    commandDict = {}

    def _createNcloth(self):
        mel.eval("doCreateNCloth 0")
    commandDict['createNcloth'] = "nClothCreate.png"

    def _createNclothOptions(self):
        cmds.nClothCreateOptions()
    commandDict['createNclothOptions'] = "nClothCreate.png"

    def _createPassiveCollider(self):
        mel.eval("makeCollideNCloth")
    commandDict['createPassiveCollider'] = "nClothCreatePassive.png"

    def _createPassiveColliderOptions(self):
        mel.eval("nClothMakeCollideOptions")
    commandDict['createPassiveColliderOptions'] = "nClothCreatePassive.png"
