from maya import cmds


commandDict = {}


# Primitives
def polyCube():
    cmds.polyCube()


def polySphere():
    cmds.polySphere()


def polyCylinder():
    cmds.polyCylinder()


def polyPlane():
    cmds.polyPlane()


def polyCone():
    cmds.polyCone()


def polyTorus():
    cmds.polyTorus()


def polyPrism():
    cmds.polyPrism()


def polyPyramid():
    cmds.polyPyramid()


def polyPipe():
    cmds.polyPipe()


def polyHelix():
    cmds.polyHelix()


def polyDisk():
    cmds.CreatePolygonDisc()


commandDict['polyDisk'] = "polyDisk.png"


def polyPlatonic():
    cmds.CreatePolygonPlatonic()


commandDict['polyPlatonic'] = "polyPlatonicSolid.png"


def polyGear():
    cmds.CreatePolygonGear()


commandDict['polyGear'] = "polyGear.png"


def polySoccerBall():
    cmds.CreatePolygonSoccerBall()


commandDict['polySoccerBall'] = "polySoccerBall.png"


def nurbsSphere():
    cmds.sphere()


commandDict['nurbsSphere'] = "sphere.png"


def nurbsCube():
    cmds.nurbsCube()


commandDict['nurbsCube'] = "cube.png"


def nurbsCylinder():
    cmds.cylinder()


commandDict['nurbsCylinder'] = "cylinder.png"


def nurbsCone():
    cmds.cone()


commandDict['nurbsCone'] = "cone.png"


def nurbsPlane():
    cmds.nurbsPlane()


commandDict['nurbsPlane'] = "plane.png"


def nurbsTorus():
    cmds.torus()


commandDict['nurbsTorus'] = "torus.png"


def nurbsCircle():
    cmds.circle()


commandDict['nurbsCircle'] = "circle.png"


def nurbsSquare():
    cmds.nurbsSquare()


commandDict['nurbsSquare'] = "square.png"


def type():
    cmds.CreatePolygonType()


commandDict['type'] = "polyType.png"


def bifrostGraph():
    cmds.CreateNewBifrostGraph()


commandDict['bifrostGraph'] = "menuIconEdit.png"


# Lights
def ambientLight():
    cmds.shadingNode('ambientLight', asLight=True)


def areaLight():
    cmds.shadingNode('areaLight', asLight=True)


def directionalLight():
    cmds.shadingNode('directionalLight', asLight=True)


def pointLight():
    cmds.shadingNode('pointLight', asLight=True)


def spotLight():
    cmds.shadingNode('spotLight', asLight=True)


def volumeLight():
    cmds.shadingNode('volumeLight', asLight=True)


# Cameras
def camera():
    cmds.camera()


# Locator
def locator():
    cmds.CreateLocator()


# Measure Tools
def distanceTool():
    cmds.DistanceTool()


def parameterTool():
    cmds.ParameterTool()


def arcLengthTool():
    cmds.ArcLengthTool()


# Sets
def createSet():
    cmds.CreateSet()


commandDict['createSet'] = "menuIconEdit.png"


def createSetOptions():
    cmds.CreateSetOptions()


commandDict['createSetOptions'] = "menuIconEdit.png"


def createPartition():
    cmds.CreatePartition()


commandDict['createPartition'] = "menuIconEdit.png"


def createPartitionOptions():
    cmds.CreatePartitionOptions()


commandDict['createPartitionOptions'] = "menuIconEdit.png"


def createQuickSelectSet():
    cmds.CreateQuickSelectSet()


commandDict['createQuickSelectSet'] = "menuIconEdit.png"


commandDict['polyCube'] = "polyCube.png"
commandDict['polySphere'] = "polySphere.png"
commandDict['polyCylinder'] = "polyCylinder.png"
commandDict['polyPlane'] = "polyPlane.png"
commandDict['polyCone'] = "polyCone.png"
commandDict['polyTorus'] = "polyTorus.png"
commandDict['polyPrism'] = "polyPrism.png"
commandDict['polyPyramid'] = "polyPyramid.png"
commandDict['polyPipe'] = "polyPipe.png"
commandDict['polyHelix'] = "polyHelix.png"
commandDict['ambientLight'] = "render_ambientLight.png"
commandDict['areaLight'] = "render_areaLight.png"
commandDict['directionalLight'] = "render_directionalLight.png"
commandDict['pointLight'] = "render_pointLight.png"
commandDict['spotLight'] = "render_spotLight.png"
commandDict['volumeLight'] = "render_volumeLight.png"
commandDict['camera'] = "Camera.png"
commandDict['locator'] = "render_locator.png"
commandDict['distanceTool'] = "distanceDim.png"
commandDict['parameterTool'] = "paramDim.png"
commandDict['arcLengthTool'] = "arcLengthDim.png"
