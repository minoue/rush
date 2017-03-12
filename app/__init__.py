from preference import miExecPref
import maya.cmds as cmds
import miExec
import itertools
import glob
import json
import imp
import os
import Qt

reload(miExecPref)
reload(miExec)


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
    """ Return Maya's main window. """
    for obj in Qt.QtWidgets.QApplication.topLevelWidgets():
        if obj.objectName() == 'MayaWindow':
            return obj
    raise RuntimeError('Could not find MayaWindow instance')


class MainClass():
    """ The main class which will interit all command classes
        from all command modules.
    """
    pass


def getClassList():
    """Create a list of class objects
   """

    script_path = os.path.dirname(__file__)
    module_path = os.path.join(script_path, 'module')

    # List of module objects from miExec package
    mod_path_list = list(itertools.chain.from_iterable(
        map(getModFiles, getModDirs(module_path))))
    modObjs = map(loadModules, mod_path_list)

    # Load pref data
    prefDict = miExecPref.getPreference()

    # List of extra module path lists
    extModPathLists = map(getExtraModPath, prefDict['extra_module_path'])

    # Flatten the lists above into a single list.
    extModPathList = list(itertools.chain.from_iterable(extModPathLists))

    # Append extra module objects
    exModObjs = map(loadExtraModule, extModPathList)

    # List of all Commands class
    commandClassList = [i.Commands for i in modObjs if i is not None]

    return commandClassList


def getClassTuple():
    """ Get tuple of classes which include GUI class
        to send it to the MainClass.
    """

    # Create a list of class objects.
    cl = [miExec.UI]
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
            miExec.UI.cmdDict.update(c.commandDict)
        except:
            print "%s does not have commandDict Attribute" % c

    maya_script_dir = cmds.internalVar(userScriptDir=True)

    outFilePath = os.path.normpath(
        os.path.join(maya_script_dir, "miExecutorCommands.json"))

    with open(outFilePath, 'w') as outFile:
        json.dump(miExec.UI.cmdDict,
                  outFile,
                  indent=4,
                  separators=(',', ':'),
                  sort_keys=True)


def init():
    inheritClasses()
    mergeCommandDict()


class MainWindow(Qt.QtWidgets.QMainWindow):
    """ MainWindow"""

    def closeExistingWindow(self):
        """ Close window if exists """

        for qt in Qt.QtWidgets.QApplication.topLevelWidgets():
            try:
                if qt.__class__.__name__ == self.__class__.__name__:
                    qt.close()
            except:
                pass

    def __init__(self, parent=getMayaWindow()):
        self.closeExistingWindow()

        super(MainWindow, self).__init__(parent)

        # Load window setting
        windowDict = miExecPref.getWindowSetting()

        self.resize(windowDict['width'], windowDict['height'])
        self.setWindowTitle("miExecutor")
        self.setWindowFlags(Qt.QtCore.Qt.Tool)
        self.setWindowFlags(
            Qt.QtCore.Qt.Popup | Qt.QtCore.Qt.FramelessWindowHint)
        self.setAttribute(Qt.QtCore.Qt.WA_DeleteOnClose)

        # Transparency setting
        if windowDict['transparent'] is True:
            self.setAttribute(Qt.QtCore.Qt.WA_TranslucentBackground)

        init()

        self.centralWidget = MainClass(parent=self)
        self.centralWidget.setObjectName("miExec_frame")
        self.centralWidget.lineEdit.escPressed.connect(self.close)
        self.centralWidget.closeSignal.connect(self.close)
        self.centralWidget.lineEdit.setFocus()

        self.setCentralWidget(self.centralWidget)
