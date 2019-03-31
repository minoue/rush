from maya import mel


commandDict = {}


def transferMapWindow():
    mel.eval("performSurfaceSampling 1")


commandDict['transferMapWindow'] = "menuIconShading.png"
