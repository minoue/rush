from maya import cmds
from maya import mel


commandDict = {}


# Normals

def averagePolygonNormals():
    cmds.AveragePolygonNormals()


commandDict['averagePolygonNormals'] = 'polyNormalAverage.png'


def averagePolygonNormalsOptions():
    cmds.AveragePolygonNormalsOptions()


commandDict['averagePolygonNormalsOptions'] = 'polyNormalAverage.png'


def conformPolygonNormals():
    cmds.ConformPolygonNormals()


commandDict['conformPolygonNormals'] = 'polyNormalsConform.png'


def reversePolygonNormals():
    cmds.ReversePolygonNormals()


commandDict['reversePolygonNormals'] = 'polyNormal.png'


def reversePolygonNormalsOptions():
    cmds.ReversePolygonNormalsOptions()


commandDict['reversePolygonNormalsOptions'] = 'polyNormal.png'


def setToFaceNormals():
    cmds.SetToFaceNormals()


commandDict['setToFaceNormals'] = 'polyNormalSetToFace.png'


def setToFaceNormalsOptions():
    cmds.SetToFaceNormalsOptions()


commandDict['setToFaceNormalsOptions'] = 'polyNormalSetToFace.png'


def setVertexNormals():
    cmds.SetVertexNormal()


commandDict['setVertexNormals'] = 'polySetVertexNormal.png'


def setVertexNormalsOptions():
    cmds.SetVertexNormalOptions()


commandDict['setVertexNormalsOptions'] = 'polySetVertexNormal.png'


def hardenPolygonEdges():
    cmds.PolygonHardenEdge()


commandDict['hardenPolygonEdges'] = 'polyHardEdge.png'


def softenPolygonEdges():
    cmds.PolygonSoftenEdge()


commandDict['softenPolygonEdges'] = 'polySoftEdge.png'


def unlockNormals():
    cmds.UnlockNormals()


commandDict['unlockNormals'] = 'polyNormalUnlock.png'


def lockNormals():
    cmds.LockNormals()


commandDict['lockNormals'] = 'polyNormalLock.png'


# Color Sets

def colorSetEditor():
    mel.eval("colorSetEditor;")


commandDict['colorSetEditor'] = 'polyColorSetEditor.png'
