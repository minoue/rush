from maya import cmds
from maya import mel


commandDict = {}


def alignUV():
    cmds.AlignUV()
commandDict['alignUV'] = "polyCameraUVs.png"


def alignUVOptions():
    cmds.AlignUVOptions()
commandDict['alignUVOptions'] = "polyCameraUVs.png"


def distributeUVs():
    cmds.DistributeUVs()
commandDict['distributeUVs'] = "polyCameraUVs.png"


def distributeUVsOptions():
    cmds.DistributeUVsOptions()
commandDict['distributeUVsOptions'] = "polyCameraUVs.png"


def flipUVs():
    cmds.FlipUVs()
commandDict['flipUVs'] = "textureEditor.png"


def flipUVsOptions():
    cmds.FlipUVsOptions()
commandDict['flipUVsOptions'] = "textureEditor.png"


def linearAlignUVs():
    cmds.linearAlignUVs()
commandDict['linearAlignUVs'] = "textureEditor.png"


def gridUV():
    cmds.GridUV()
commandDict['gridUV'] = "textureEditor.png"


def gridUVOptions():
    cmds.GridUVOptions()
commandDict['gridUVOptions'] = "textureEditor.png"


def matchUVs():
    cmds.MatchUVs()
commandDict['matchUVs'] = "textureEditor.png"


def matchUVsOptions():
    cmds.MatchUVsOptions()
commandDict['matchUVsOptions'] = "textureEditor.png"


def normalizeUVs():
    cmds.NormalizeUVs()
commandDict['normalizeUVs'] = "textureEditor.png"


def normalizeUVsOptions():
    cmds.NormalizeUVsOptions()
commandDict['normalizeUVsOptions'] = "textureEditor.png"


def rotateUVs():
    cmds.RotateUVs()
commandDict['rotateUVs'] = "textureEditor.png"


def rotateUVsOptions():
    cmds.RotateUVsOptions()
commandDict['rotateUVsOptions'] = "textureEditor.png"


def symmetrizeUV():
    cmds.SymmetrizeUV()
commandDict['symmetrizeUV'] = "textureEditor.png"


def symmetrizeUVOptions():
    cmds.SymmetrizeUVOptions()
commandDict['symmetrizeUVOptions'] = "textureEditor.png"


def unitizeUVs():
    cmds.UnitizeUVs()
commandDict['unitizeUVs'] = "textureEditor.png"


def unitizeUVsOptions():
    cmds.UnitizeUVsOptions()
commandDict['unitizeUVsOptions'] = "textureEditor.png"


def distributeShells():
    cmds.DistributeShells()
commandDict['distributeShells'] = "textureEditor.png"


def distributeShellsOptions():
    cmds.DistributeShellsOptions()
commandDict['distributeShellsOptions'] = "textureEditor.png"


def gatherShells():
    cmds.UVGatherShells()
commandDict['gatherShells'] = "textureEditor.png"


def layoutUV():
    cmds.LayoutUV()
commandDict['layoutUV'] = "textureEditor.png"


def LayoutUVOptions():
    cmds.LayoutUVOptions()
commandDict['layoutUVOptions'] = "textureEditor.png"


def layoutUVAlong():
    cmds.LayoutUVAlong()
commandDict['layoutUVAlong'] = "textureEditor.png"


def layoutUVAlongOptions():
    cmds.LayoutUVAlongOptions()
commandDict['layoutUVAlongOptions'] = "textureEditor.png"


def orientUVShells():
    cmds.UVOrientShells()
commandDict['orientUVShells'] = "textureEditor.png"


def orientUVShellsToEdges():
    mel.eval("texOrientEdge;")
commandDict['orientUVShellsToEdges'] = "textureEditor.png"


def randomizeUVShells():
    cmds.RandomizeShells()
commandDict['randomizeUVShells'] = "textureEditor.png"


def randomizeUVShellsOptions():
    cmds.RandomizeShellsOptions()
commandDict['randomizeUVShellsOptions'] = "textureEditor.png"


def snapAndStackUVs():
    mel.eval("texSnapStackShells;")
commandDict['snapAndStackUVs'] = "textureEditor.png"


def snapUVsTogether():
    cmds.UVSnapTogether()
commandDict['snapUVsTogether'] = "textureEditor.png"


def snapUVsTogetherOptions():
    cmds.UVSnapTogetherOptions()
commandDict['snapUVsTogetherOptions'] = "textureEditor.png"


def stackUVShells():
    mel.eval("texStackShells;")
commandDict['stackUVShells'] = "textureEditor.png"


def stackUVShells():
    mel.eval("texStackShells;")
commandDict['stackUVShells'] = "textureEditor.png"


def stackAndOrientUVShells():
    mel.eval("texStackShells({});UVOrientShells;")
commandDict['stackAndOrientUVShells'] = "textureEditor.png"


def stackSimilarUVShells():
    cmds.UVStackSimilarShells()
commandDict['stackSimilarUVShells'] = "textureEditor.png"


def stackSimilarUVShellsOptions():
    cmds.UVStackSimilarShellsOptions()
commandDict['stackSimilarUVShellsOptions'] = "textureEditor.png"


def unstackUVShells():
    cmds.UVUnstackShells()
commandDict['unstackUVShells'] = "textureEditor.png"


def unstackUVShellsOptions():
    cmds.UVUnstackShellsOptions()
commandDict['unstackUVShellsOptions'] = "textureEditor.png"


def mapUVBorder():
    cmds.MapUVBorder()
commandDict['mapUVBorder'] = "textureEditor.png"


def mapUVBorderOptions():
    cmds.MapUVBorderOptions()
commandDict['mapUVBorderOptions'] = "textureEditor.png"


def optimizeUVs():
    cmds.OptimzeUVs()
commandDict['optimizeUVs'] = "textureEditor.png"


def optimizeUVsOptions():
    cmds.OptimzeUVsOptions()
commandDict['optimizeUVsOptions'] = "textureEditor.png"


def straightenUVBorder():
    cmds.StraightenUVBorder()
commandDict['straightenUVBorder'] = "textureEditor.png"


def straightenUVBorderOptions():
    cmds.StraightenUVBorderOptions()
commandDict['straightenUVBorderOptions'] = "textureEditor.png"


def straightenUVShells():
    mel.eval("texStraightenShell;")
commandDict['straightenUVShells'] = "textureEditor.png"


def straightenUVs():
    cmds.UVStraighten()
commandDict['straightenUVs'] = "textureEditor.png"


def straightenUVsOptions():
    cmds.UVStraightenOptions()
commandDict['straightenUVsOptions'] = "textureEditor.png"


def unfoldUV():
    cmds.UnfoldUV()
commandDict['unfoldUV'] = "textureEditor.png"


def unfoldUVOptions():
    cmds.UnfoldUVOptions()
commandDict['unfoldUVOptions'] = "textureEditor.png"


def warpImage():
    cmds.WarpImage()
commandDict['warpImage'] = "textureEditor.png"


def warpImageOptions():
    cmds.WarpImageOptions()
commandDict['warpImageOptions'] = "textureEditor.png"
