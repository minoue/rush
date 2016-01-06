from PySide import QtGui, QtCore
from preference import pref
reload(pref)
from gui import frame
reload(frame)
import maya.OpenMayaUI as mui
import maya.cmds as cmds
import os
import json
import shiboken
import imp


SCRIPT_PATH = os.path.dirname(__file__)
MODULE_PATH = os.path.join(SCRIPT_PATH, 'module')
MAYA_SCRIPT_DIR = cmds.internalVar(userScriptDir=True)


# Load pref data
prefDict = pref.getPreference()


# Load window setting
windowDict = pref.getWindowSetting()


modulePathDict = {}

# Init modulePathDict
for root, dirs, files in os.walk(MODULE_PATH):
    for f in files:
        if f.endswith(".py"):
            if "__init__" not in f:
                fullpath = os.path.join(root, f)
                name = os.path.splitext(f)[0]
                relPath = os.path.relpath(root, SCRIPT_PATH).replace("\\", "/")
                modPath = "miExecutor." \
                          + relPath.replace("/", ".")\
                          + ".%s" % name
                modulePathDict[modPath] = fullpath


# List of all module objects
moduleObjectList = []
for i in modulePathDict:
    try:
        mod = imp.load_source(i, modulePathDict[i])
        moduleObjectList.append(mod)
    except ImportError:
        # Ignore if plugins are not loaded, eg, Mayatomr, mtoa, etc...
        continue


# Init a list of extra modules
extraModPathList = []


# Get a list of module names
for p in prefDict['extra_module_path']:
    for root, dirs, files in os.walk(p):
        for f in files:
            if f.endswith(".py"):
                if "__init__" not in f:
                    extraModPathList.append(
                        os.path.join(root, f).replace("\\", "/"))


# Load extra modules
extraModObjectList = [
    imp.load_source(
        os.path.basename(m).rsplit(".py")[0], m) for m in extraModPathList]


# Append extra module objects
moduleObjectList.extend(extraModObjectList)


# List of all Commands class
commandClassList = [i.Commands for i in moduleObjectList]


def getMayaWindow():
    ptr = mui.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(ptr), QtGui.QMainWindow)


class MainClass():
    """
    This is the main class which will interit all command classes
    from all command modules
    """

    pass

# Create a list of class objects.
CLASSLIST = [frame.UI]
for i in commandClassList:
    CLASSLIST.append(i)


# Convert the list of classes to the tuple
# The second argument of 'type' only accept a tuple
CLASSES = tuple(CLASSLIST)


def inheritClasses():
    """ Re-difine MainClass to inherit all classes from other modules """

    global MainClass
    MainClass = type('MainClass', CLASSES, dict(MainClass.__dict__))


def mergeCommandDict():
    """ Combine all command dicrectories and create json files which includes
    all command names and their icons paths.  """

    for c in commandClassList:
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


def useTab():
    """ Use Tab key as hotkey """

    mainWin = getMayaWindow()

    # Get list of QActions in main window
    mainWinActions = mainWin.actions()

    actionName = "miExec_TabKey"

    # List of QAction's object name
    actionNames = [i.objectName() for i in mainWinActions]

    # If tab action already exists in main window, use it.
    if actionName in actionNames:
        for action in mainWinActions:
            if action.objectName() == actionName:
                if prefDict['use_tab_key'] is True:
                    action.setEnabled(True)
                else:
                    action.setDisabled(True)
            else:
                pass

    # if it doesn't exist, create new tab action.
    else:
        tabAction = QtGui.QAction(mainWin)
        tabAction.setObjectName(actionName)
        tabAction.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Tab))
        tabAction.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        tabAction.triggered.connect(main)
        mainWin.addAction(tabAction)


def init():
    inheritClasses()
    mergeCommandDict()
    useTab()


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

    # Move to next widget (like Tab key) when any fields are focused.
    focusWidget = getFocusWidget()
    if 'field' in focusWidget.objectName().lower():
        focusWidget.focusNextPrevChild(True)
        return

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
