from maya import cmds


class Commands(object):
    """ class name must be 'Commands' """

    commandDict = {}

    # Primitives
    def _polyCube(self):
        cmds.polyCube()
    commandDict['polyCube'] = "polyCube.png"

    def _polySphere(self):
        cmds.polySphere()
    commandDict['polySphere'] = "polySphere.png"

    def _polyCylinder(self):
        cmds.polyCylinder()
    commandDict['polyCylinder'] = "polyCylinder.png"

    def _polyPlane(self):
        cmds.polyPlane()
    commandDict['polyPlane'] = "polyPlane.png"

    def _polyCone(self):
        cmds.polyCone()
    commandDict['polyCone'] = "polyCone.png"

    def _polyTorus(self):
        cmds.polyTorus()
    commandDict['polyTorus'] = "polyTorus.png"

    def _polyPrism(self):
        cmds.polyPrism()
    commandDict['polyPrism'] = "polyPrism.png"

    def _polyPyramid(self):
        cmds.polyPyramid()
    commandDict['polyPyramid'] = "polyPyramid.png"

    def _polyPipe(self):
        cmds.polyPipe()
    commandDict['polyPipe'] = "polyPipe.png"

    def _polyHelix(self):
        cmds.polyHelix()
    commandDict['polyHelix'] = "polyHelix.png"

    # Lights
    def _ambientLight(self):
        cmds.shadingNode('ambientLight', asLight=True)
    commandDict['ambientLight'] = "render_ambientLight.png"

    def _areaLight(self):
        cmds.shadingNode('areaLight', asLight=True)
    commandDict['areaLight'] = "render_areaLight.png"

    def _directionalLight(self):
        cmds.shadingNode('directionalLight', asLight=True)
    commandDict['directionalLight'] = "render_directionalLight.png"

    def _pointLight(self):
        cmds.shadingNode('pointLight', asLight=True)
    commandDict['pointLight'] = "render_pointLight.png"

    def _spotLight(self):
        cmds.shadingNode('spotLight', asLight=True)
    commandDict['spotLight'] = "render_spotLight.png"

    def _volumeLight(self):
        cmds.shadingNode('volumeLight', asLight=True)
    commandDict['volumeLight'] = "render_volumeLight.png"

    # Cameras
    def _camera(self):
        cmds.camera()
    commandDict['camera'] = "Camera.png"

    # Locator
    def _locator(self):
        cmds.spaceLocator(p=[0, 0, 0])
    commandDict['locator'] = "render_locator.png"

    # Measure Tools
    def _distanceTool(self):
        cmds.DistanceTool()
    commandDict['distanceTool'] = "distanceDim.png"

    def _parameterTool(self):
        cmds.ParameterTool()
    commandDict['parameterTool'] = "paramDim.png"

    def _arcLengthTool(self):
        cmds.ArcLengthTool()
    commandDict['arcLengthTool'] = "arcLengthDim.png"
