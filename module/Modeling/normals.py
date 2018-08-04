import maya.cmds as cmds


# class name must be 'Commands'
class Commands(object):

    commandDict = {}

    def _setNormalAngle(self):
        cmds.SetNormalAngle()
    commandDict['setNormalAngle'] = "polyNormalSetAngle.png"
    
    def _averageNormals(self):
        cmds.AveragePolygonNormals()
    commandDict['averageNormals'] = "polyNormalAverage.png"

    def _averageNormalsOptions(self):
        cmds.AveragePolygonNormalsOptions()
    commandDict['averageNormalsOptions'] = "polyNormalAverage.png"

    def _conformNormals(self):
        cmds.ConformPolygonNormals()
    commandDict['conformNormals'] = "polyNormalsConform.png"

    def _reverseNormals(self):
        cmds.ReversePolygonNormals()
    commandDict['reverseNormals'] = "polyNormal.png"

    def _reverseNormalsOptions(self):
        cmds.ReversePolygonNormalsOptions()
    commandDict['reverseNormals'] = "polyNormal.png"

    def _setToFaceNormals(self):
        cmds.SetToFaceNormals()
    commandDict['setToFaceNormals'] = "polyNormalSetToFace.png"

    def _setToFaceNormalsOptions(self):
        cmds.SetToFaceNormalsOptions()
    commandDict['setToFaceNormalsOptions'] = "polyNormalSetToFace.png"

    def _setVertexNormals(self):
        cmds.SetVertexNormal()
    commandDict['setVertexNormals'] = "polySetVertexNormal.png"

    def _setVertexNormalsOptions(self):
        cmds.SetVertexNormalOptions()
    commandDict['setVertexNormals'] = "polySetVertexNormal.png"

    def _softenEdgeNormals(self):
        mel.eval("SoftPolyEdgeElements 1")
    commandDict['softenEdgeNormals'] = "polySoftEdge.png"

    def _hardenEdgeNormals(self):
        mel.eval("SoftPolyEdgeElements 0")
    commandDict['hardenEdgeNormals'] = "polyHardEdge.png"

    def _lockNormals(self):
        cmds.LockNormals()
    commandDict['lockNormals'] = "polyNormalLock.png"

    def _unlockNormals(self):
        cmds.UnlockNormals()
    commandDict['unlockNormals'] = "polyNormalUnlock.png"
