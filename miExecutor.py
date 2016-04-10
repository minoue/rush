from PySide import QtGui, QtCore
from preference import miExecPref
reload(miExecPref)
from gui import frame
reload(frame)
import maya.OpenMayaUI as mui
import maya.cmds as cmds
import itertools
import shiboken
import glob
import json
import imp
import os


SCRIPT_PATH = os.path.dirname(__file__)
MODULE_PATH = os.path.join(SCRIPT_PATH, 'module')
MAYA_SCRIPT_DIR = cmds.internalVar(userScriptDir=True)


# Load pref data
prefDict = miExecPref.getPreference()


# Load window setting
windowDict = miExecPref.getWindowSetting()


def getModDirs(module_root_dir):
    mod_dirs = [module_root_dir]
    for root, dirs, files in os.walk(module_root_dir):
        for d in dirs:
            mod_dirs.append(os.path.join(root, d))
    return mod_dirs


def getModFiles(dir_path):
    return [
        i for i
        in glob.glob(os.path.join(dir_path, "*.py"))
        if os.path.basename(i) != "__init__.py"]


def loadModules(module_file_path):
    """ Return module object by given file path
    """

    name = os.path.splitext(module_file_path)[0].split("/")
    name = "/".join(name[-2:])
    try:
        mod = imp.load_source(name, module_file_path)
        return mod
    except ImportError:
        return None


def getExtraModPath(extra_dir):
    """ Return a list of python module files in abs path in given directory.
    """
    return [
        i.replace("\\", "/") for i
        in glob.glob(os.path.join(extra_dir, "*.py"))
        if os.path.basename(i) != "__init__.py"]


def loadExtraModule(module_path):
    return imp.load_source(
        os.path.basename(module_path).rsplit(".py")[0], module_path)


def getMayaWindow():
    """ Get maya main window object.
    """
    ptr = mui.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(ptr), QtGui.QMainWindow)


class MainClass():
    """ The main class which will interit all command classes
        from all command modules.
    """
    pass


def getClassList():
    """Create a list of class objects
   """

    # List of module objects from miExec package
    mod_path_list = list(itertools.chain.from_iterable(
        map(getModFiles, getModDirs(MODULE_PATH))))
    modObjs = map(loadModules, mod_path_list)

    # List of extra module path lists
    extModPathLists = map(getExtraModPath, prefDict['extra_module_path'])

    # Flatten the lists above into a single list.
    extModPathList = list(itertools.chain.from_iterable(extModPathLists))

    # Append extra module objects
    exModObjs = map(loadExtraModule, extModPathList)
    modObjs.extend(exModObjs)

    # List of all Commands class
    commandClassList = [i.Commands for i in modObjs if i is not None]

    return commandClassList


def getClassTuple():
    """ Get tuple of classes which include GUI class
        to send it to the MainClass.
    """

    # Create a list of class objects.
    cl = [frame.UI]
    for i in getClassList():
        cl.append(i)

    # Convert the list of classes to the tuple
    # The second argument of 'type' only accept a tuple
    return tuple(cl)


def inheritClasses():
    """ Re-difine MainClass to inherit all classes from other modules
    """

    CLASSES = getClassTuple()

    global MainClass
    MainClass = type('MainClass', CLASSES, dict(MainClass.__dict__))


def mergeCommandDict():
    """ Combine all command dicrectories and create json files which includes
    all command names and their icons paths.  """

    for c in getClassList():
        try:
            frame.UI.cmdDict.update(c.commandDict)
        except:
            print "%s does not have commandDict Attribute" % c

    outFilePath = os.path.normpath(
        os.path.join(MAYA_SCRIPT_DIR, "miExecutorCommands.json"))

    with open(outFilePath, 'w') as outFile:
        json.dump(frame.UI.cmdDict,
                  outFile,
                  indent=4,
                  separators=(',', ':'),
                  sort_keys=True)


def init():
    inheritClasses()
    mergeCommandDict()


def getFocusWidget():
    # Get Maya's currently focused widget

    return QtGui.qApp.focusWidget()


class MainWindow(QtGui.QMainWindow):
    """ MainWindow"""

    def __init__(self, parent=getMayaWindow()):
        super(MainWindow, self).__init__(parent)

        self.resize(windowDict['width'], windowDict['height'])
        self.setWindowTitle("miExecutor")
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setWindowFlags(QtCore.Qt.Popup | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # Transparency setting
        if windowDict['transparent'] is True:
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        centralWidget = MainClass(parent=self)
        centralWidget.setObjectName("miExec_frame")
        centralWidget.lineEdit.escPressed.connect(self.close)
        centralWidget.closeSignal.connect(self.close)
        centralWidget.lineEdit.setFocus()

        self.setCentralWidget(centralWidget)


def main():
    """ Show window and move it to cursor position """

    # Create and show window
    global miExec
    try:
        miExec.close()
    except:
        pass
    miExec = MainWindow()
    miExec.show()

    # Move the window to the cursor position.
    pos = QtGui.QCursor.pos()
    miExec.move(
        pos.x() - (miExec.width() / 2), pos.y() - (miExec.height() / 2))
    miExec.activateWindow()
    miExec.raise_()


if __name__ == "__main__":
    pass
else:
    init()
