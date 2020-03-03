from maya import cmds
from maya import mel


commandDict = {}


def displayFaceNormals():
    cmds.ToggleFaceNormals()
commandDict['displayFaceNormals'] = "paintFXtoCurve.png"


def displayVertexNormals():
    cmds.ToggleVertexNormalDisplay()
commandDict['displayVertexNormals'] = "paintFXtoCurve.png"


def displayTangents():
    cmds.ToggleTangentDisplay()
commandDict['displayTangents'] = "paintFXtoCurve.png"


def changeNormalSize():
    cmds.ChangeNormalSize()
commandDict['changeNormalSize'] = "paintFXtoCurve.png"


# ----------------


def displayBorderEdges():
    cmds.ToggleBorderEdges()
commandDict['displayBorderEdges'] = "paintFXtoCurve.png"


def displayCreaseEdges():
    cmds.ToggleCreaseEdges()
commandDict['displayCreaseEdges'] = "paintFXtoCurve.png"


def displayTextureBorderEdges():
    cmds.ToggleTextureBorderEdges()
commandDict['displayTextureBorderEdges'] = "paintFXtoCurve.png"


def changeEdgeWidth():
    cmds.ChangeEdgeWidth()
commandDict['changeEdgeWidth'] = "paintFXtoCurve.png"


# ----------------
