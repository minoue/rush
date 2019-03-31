from maya import cmds
from maya import mel


commandDict = {}


# Components -------------------------------

def polyBevel():
    cmds.polyBevel()


def polyBridge():
    mel.eval("performPolyBridgeEdge 0")


def polyCircularize():
    cmds.PolyCircularize()


def polyCollapse():
    cmds.PolygonCollapse()


def polyConnectComponents():
    cmds.polyConnectComponents()


def detachComponent():
    cmds.DetachComponent()


def polyExtrude():
    cmds.PolyExtrude()


def mergeComponents():
    cmds.PolyMerge()


def mergeComponentsOptions():
    cmds.PolyMergeOptions()


def mergeToCenter():
    cmds.MergeToCenter()


def transformComponents():
    cmds.MovePolygonComponent()


def transformComponentsOptions():
    cmds.MovePolygonComponentOptions()


def polyFlip():
    mel.eval("dR_performSymmetryFlip")


def polySymmetrize():
    mel.eval("dR_performSymmetrize")


# Vertex -------------------------------


def averageVertex():
    cmds.AverageVertex()


def averageVertexOptions():
    mel.eval("performPolyAverageVertex 1")


def chamferVertex():
    cmds.ChamferVertex()


def chamferVertexOptions():
    cmds.ChamferVertexOptions()


# Edge -------------------------------


def detachEdgeComponent():
    cmds.DetachEdgeComponent()


# Face -------------------------------


def extractFace():
    cmds.ExtractFace()


def extractFaceOptions():
    cmds.ExtractFaceOptions()


commandDict['polyBevel'] = 'polyBevel.png'
commandDict['polyBridge'] = 'polyBridge.png'
commandDict['polyCircularize'] = 'polyCircularize.png'
commandDict['polyCollapse'] = 'polyCollapseEdge.png'
commandDict['polyConnectComponents'] = 'polyConnectComponents.png'
commandDict['detachComponent'] = 'polySplitVertex.png'
commandDict['polyExtrude'] = 'polyExtrudeFacet.png'
commandDict['mergeComponents'] = 'polyMerge.png'
commandDict['mergeComponentsOptions'] = 'polyMerge.png'
commandDict['mergeToCenter'] = 'polyMergeToCenter.png'
commandDict['transformComponents'] = 'polyMoveVertex.png'
commandDict['transformComponentsOptions'] = 'polyMoveVertex.png'
commandDict['polyFlip'] = 'polyFlip.png'
commandDict['polySymmetrize'] = 'symmetrize.png'
commandDict['averageVertex'] = 'polyAverageVertex.png'
commandDict['averageVertexOptions'] = 'polyAverageVertex.png'
commandDict['chamferVertex'] = 'polyChamfer.png'
commandDict['chamferVertexOptions'] = 'polyChamfer.png'
commandDict['detachEdgeComponent'] = 'polyEditEdgeFlow.png'
commandDict['extractFace'] = 'polyChipOff.png'
commandDict['extractFaceOptions'] = 'polyChipOff.png'
