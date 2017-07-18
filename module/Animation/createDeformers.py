import maya.cmds as cmds
import maya.mel as mel


class Commands(object):

    commandDict = {}

    def _createBlendShape(self):
        cmds.CreateBlendShape()
    commandDict['createBlendShape'] = "blendShape.png"

    def _createBlendShapeOptions(self):
        cmds.CreateBlendShapeOptions()
    commandDict['createBlendShapeOptions'] = "blendShape.png"

    def _createLattice(self):
        cmds.CreateLattice()
    commandDict['createLattice'] = "lattice.png"

    def _createLatticeOptions(self):
        cmds.CreateLatticeOptions()
    commandDict['createLatticeOptions'] = "lattice.png"

    def _createWrap(self):
        cmds.CreateWrap()
    commandDict['createWrap'] = "wrap.png"

    def _createWrapOptions(self):
        cmds.CreateWrapOptions()
    commandDict['createWrapOptions'] = "wrap.png"

    def _createShrinkWrap(self):
        cmds.CreateShrinkWrap()
    commandDict['createShrinkWrap'] = "shrinkwrap.png"

    def _createShrinkWrapOptions(self):
        cmds.CreateShrinkWrapOptions()
    commandDict['createShrinkWrapOptions'] = "shrinkwrap.png"

    def _createCluster(self):
        cmds.CreateCluster()
    commandDict['createCluster'] = "cluster.png"

    def _createClusterOptions(self):
        cmds.CreateClusterOptions()
    commandDict['createClusterOptions'] = "cluster.png"

    def _bend(self):
        cmds.Bend()
    commandDict['bend'] = "bendNLD.png"

    def _bendOptions(self):
        cmds.BendOptions()
    commandDict['bendOptions'] = "bendNLD.png"

    def _flare(self):
        cmds.Flare()
    commandDict['flare'] = "flareNLD.png"

    def _flareOptions(self):
        cmds.FlareOptions()
    commandDict['flareOptions'] = "flareNLD.png"

    def _sine(self):
        cmds.Sine()
    commandDict['sine'] = "sineNLD.png"

    def _sineOptions(self):
        cmds.SineOptions()
    commandDict['sineOptions'] = "sineNLD.png"

    def _squash(self):
        cmds.Squash()
    commandDict['squash'] = "squashNLD.png"

    def _squashOptions(self):
        cmds.SquashOptions()
    commandDict['squashOptions'] = "squashNLD.png"

    def _twist(self):
        cmds.Twist()
    commandDict['twist'] = "twistNLD.png"

    def _twistOptions(self):
        cmds.TwistOptions()
    commandDict['twistOptions'] = "twistNLD.png"

    def _wave(self):
        cmds.Wave()
    commandDict['wave'] = "waveNLD.png"

    def _waveOptions(self):
        cmds.WaveOptions()
    commandDict['waveOptions'] = "waveNLD.png"   
