import maya.cmds as cmds
import maya.mel as mel


# class name must be 'Commands'
class Commands(object):

    # Name of dictionary must be this module name + 'Dict'
    modelingDict = {}

    def __init__(self):
        pass

    def _smoothPolygonOptions(self):
        cmds.SmoothPolygonOptions()
    modelingDict['smoothPolygonOptions'] = "polySphere.png"
    # ^ Don't forget to add the command to the dictionary.

    def _setNormalAngle(self):
        cmds.SetNormalAngle()
    modelingDict['setNormalAngle'] = "polyNormalSetAngle.png"

    def _polygonSelectionConstraints(self):
        cmds.PolygonSelectionConstraints()
    modelingDict['polygonSelectionConstraints'] = "polySelectUsingConstraints.png"

    def _transferAttributes(self):
        mel.eval("performTransferAttributes 1")
    modelingDict['transferAttributes'] = "polyTransferAttributes.png"

    def _polyCleanup(self):
        mel.eval("performPolyCleanup 1")
    modelingDict['polyCleanup'] = "polyCleanup.png"

    def _polyQuadrangulate(self):
        cmds.QuadrangulateOptions()
    modelingDict['polyQuadrangulate'] = "polyQuad.png"

    def _freezeOnlyTranslation(self):
        cmds.makeIdentity(apply=True, t=True, r=False, s=False, n=False)
    modelingDict['freezeOnlyTranslation'] = "menuIconModify.png"

    def _freezeOnlyRotation(self):
        cmds.makeIdentity(apply=True, t=False, r=True, s=False, n=False)
    modelingDict['freezeOnlyRotation'] = "menuIconModify.png"

    def _freezeOnlyScale(self):
        cmds.makeIdentity(apply=True, t=False, r=False, s=True, n=False)
    modelingDict['freezeOnlyScale'] = "menuIconModify.png"

    def _detachEdgeComponent(self):
        cmds.DetachEdgeComponent()
    modelingDict['detachEdgeComponent'] = 'polyEditEdgeFlow.png'

    def _polyBevel(self):
        cmds.polyBevel()
    modelingDict['polyBevel'] = 'polyBevel.png'

    def _polyBooleanUnion(self):
        cmds.PolygonBooleanUnion()
    modelingDict['polyBooleanUnion'] = 'polyBooleansUnion.png'

    def _polyBooleanUnionOptions(self):
        cmds.PolygonBooleanUnionOptions()
    modelingDict['polyBooleanUnionOptions'] = 'polyBooleansUnion.png'

    def _polyBooleanDifference(self):
        cmds.PolygonBooleanDifference()
    modelingDict['polyBooleanDifference'] = 'polyBooleansDifference.png'

    def _polyBooleanDifferenceOptions(self):
        cmds.PolygonBooleanDifferenceOptions()
    modelingDict['polyBooleanDifferenceOptions'] = 'polyBooleansDifference.png'

    def _polyBooleanIntersection(self):
        cmds.PolygonBooleanIntersection()
    modelingDict['polyBooleanIntersection'] = 'polyBooleansIntersection.png'

    def _polyBooleanIntersectionOptions(self):
        cmds.PolygonBooleanIntersectionOptions()
    modelingDict['polyBooleanIntersectionOptions'] = 'polyBooleansIntersection.png'
