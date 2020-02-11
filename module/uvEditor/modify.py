from maya import cmds
from maya import mel


commandDict = {}


def alignUV():
    cmds.AlignUV()
commandDict['alignUV'] = "polyCameraUVs.png"


def alignUVOptions():
    cmds.AlignUVOptions()
commandDict['alignUVOptions'] = "polyCameraUVs.png"
