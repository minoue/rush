import maya.cmds as cmds
import maya.mel as mel


class Commands(object):

    commandDict = {}

    def _attachToMotionPath(self):
        mel.eval("""
            pathAnimation -fractionMode true -follow true -followAxis x
            -upAxis y -worldUpType "vector" -worldUpVector 0 1 0
            -inverseUp false -inverseFront false -bank false
            -startTimeU `playbackOptions -query -minTime`
            -endTimeU `playbackOptions -query -maxTime`
            """)
    commandDict['attachToMotionPath'] = "motionPath.png"

    def _attachToMotionPathOptions(self):
        cmds.AttachToPathOptions()
    commandDict['attachToMotionPath'] = "motionPath.png"

    def _flowPathObject(self):
        mel.eval("""flowObjects 5 2 2 1 0 2 2 2""")
    commandDict['flowPathObject'] = "flowPathObj.png"

    def _flowPathObjectOptions(self):
        cmds.FlowPathObjectOptions()
    commandDict['flowPathObject'] = "flowPathObj.png"
