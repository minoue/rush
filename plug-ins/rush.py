from pymel.all import mel as pm
from maya import OpenMayaMPx
from maya import OpenMaya
from maya import cmds
from maya import mel
import rush
import logging
import string
import random
import json
import sys
import os
import Qt
reload(rush)


kPluginCmdName = "rush"
kVerboseFlag = "-v"
kVerboseLongFlag = "-verbose"


# Define mel procedure to call the previous function
mel.eval("""
global proc callLastCommand(string $function)
{
    repeatLast -ac $function -acl "blah-blah....";
}
""")


def setupLogger(verbose=False):
    """

    Args:
        verbose (bool): verbose mode

    Return:
        type: return value

    """
    if verbose:
        lv = logging.DEBUG
    else:
        lv = logging.CRITICAL

    tempLogName = 'Rush : ' + ''.join(
        random.SystemRandom().choice(
            string.ascii_uppercase + string.digits) for _ in range(10))

    logger = logging.getLogger(tempLogName)
    handler = logging.StreamHandler()
    logger.setLevel(lv)
    handler.setLevel(lv)
    logger.addHandler(handler)
    return logger


def getMayaWindow():
    """ Return Maya's main window
    """

    for obj in Qt.QtWidgets.QApplication.topLevelWidgets():
        if obj.objectName() == 'MayaWindow':
            return obj
    raise RuntimeError('Could not find MayaWindow instance')


class CustomQLineEdit(Qt.QtWidgets.QLineEdit):
    """ Custom QLineEdit with custom events and signals"""

    escPressed = Qt.QtCore.Signal(str)

    def __init__(self, parent=None):
        super(CustomQLineEdit, self).__init__(parent)
        self.setFocusPolicy(Qt.QtCore.Qt.StrongFocus)

    def focusOutEvent(self, event):
        # Emit signal to close the window when it gets out of focus
        self.escPressed.emit('esc')

    def keyPressEvent(self, event):
        if event.key() == Qt.QtCore.Qt.Key_Escape:
            self.escPressed.emit('esc')
        else:
            super(CustomQLineEdit, self).keyPressEvent(event)


class Gui(rush.RushCommands, Qt.QtWidgets.QFrame):

    def __init__(self, logger, parent=None):
        super(Gui, self).__init__(parent)
        self.setAttribute(Qt.QtCore.Qt.WA_DeleteOnClose)

        self.logger = logger

        # Create Data then UI
        self.createData()
        self.createUI()

    def createUI(self):
        self.LE = CustomQLineEdit(self)
        font = self.LE.font()
        font.setPointSize(14)
        self.LE.setFont(font)
        self.LE.setFixedWidth(200)
        layout = Qt.QtWidgets.QBoxLayout(
            Qt.QtWidgets.QBoxLayout.TopToBottom)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.LE)
        self.setLayout(layout)

        # Set up QCompleter
        self.completer = Qt.QtWidgets.QCompleter(self)
        self.completer.setCompletionMode(
            Qt.QtWidgets.QCompleter.UnfilteredPopupCompletion)
        self.completer.setModel(self.filteredModel)
        self.completer.setObjectName("commandCompleter")
        # self.completer.popup().setIconSize(self.iconSize)

        # Edit line Edit behavior
        self.LE.setCompleter(self.completer)
        self.LE.textEdited.connect(self.updateData)
        self.LE.returnPressed.connect(self.execute)
        self.LE.escPressed.connect(self.exitApp)
        self.LE.setFocus()

    def createData(self):
        """

        Return:
            QSortFilterProxyModel: data

        """

        model = Qt.QtGui.QStandardItemModel()

        # Load json files as dicrectory.
        # key is command name, and its item is icon path.
        mayaScriptDir = cmds.internalVar(userScriptDir=True)
        commandFile = os.path.normpath(
            os.path.join(mayaScriptDir, "rushCmds.json"))
        try:
            f = open(commandFile)
            jsonDict = json.load(f)
            f.close()
        except IOError:
            jsonDict = {}

        # Create a list of command names
        self.commands = [i for i in jsonDict]

        # Add all command names and icon paths to the the model(model)
        for num, command in enumerate(jsonDict):
            item = Qt.QtGui.QStandardItem(command)
            if os.path.isabs(jsonDict[command]) is True:
                iconPath = os.path.normpath(jsonDict[command])
                item.setIcon(Qt.QtGui.QIcon(iconPath))
            else:
                item.setIcon(Qt.QtGui.QIcon(":%s" % jsonDict[command]))
            model.setItem(num, 0, item)

        # Store the model(model) into the sortFilterProxy model
        self.filteredModel = Qt.QtCore.QSortFilterProxyModel(self)
        self.filteredModel.setFilterCaseSensitivity(
            Qt.QtCore.Qt.CaseInsensitive)
        self.filteredModel.setSourceModel(model)

    def updateData(self):
        """ Update current completion data

        Args:

        Return:

        """

        # command completer
        currentText = self.LE.text()
        if currentText == "":
            self.LE.setCompleter(self.completer)

        # Set commands to case insensitive
        regExp = Qt.QtCore.QRegExp(
            self.LE.text(),
            Qt.QtCore.Qt.CaseInsensitive,
            Qt.QtCore.QRegExp.RegExp)
        self.filteredModel.setFilterRegExp(regExp)

    def execute(self):
        cmd = self.LE.text()
        try:
            f = getattr(self, "_%s" % cmd)
            f()
            self.logger.debug("Running command : %s" % cmd)

            # Add to repeatLast command so the comamnd can be repeatable
            # by G key
            pm.callLastCommand(
                """python(\"rush.RushCommands()._%s()\")""" % cmd)
            self.exitApp()
        except AttributeError:
            pass

    def exitApp(self):
        self.close()
        self.parent().close()


class MainWindow(Qt.QtWidgets.QMainWindow):

    def closeExistingWindow(self):
        """ Close window if exists """

        for qt in Qt.QtWidgets.QApplication.topLevelWidgets():
            try:
                if qt.__class__.__name__ == self.__class__.__name__:
                    qt.close()
            except:
                pass

    def __init__(self, logger, parent=getMayaWindow()):
        self.closeExistingWindow()
        super(MainWindow, self).__init__(parent)

        self.logger = logger
        self.setWindowTitle("test")
        self.setWindowFlags(Qt.QtCore.Qt.Tool)
        self.setAttribute(Qt.QtCore.Qt.WA_DeleteOnClose)
        self.setWindowFlags(
            Qt.QtCore.Qt.Popup | Qt.QtCore.Qt.FramelessWindowHint)
        self.setFixedHeight(25)

        self.cw = Gui(logger, self)
        self.setCentralWidget(self.cw)


class Rush(OpenMayaMPx.MPxCommand):

    def __init__(self):
        super(Rush, self).__init__()

        self.verbose = False
        self.cmdArg = "Initial arg"

    def doIt(self, args):

        # Parse the arguments.
        argData = OpenMaya.MArgDatabase(self.syntax(), args)
        try:
            self.cmdArg = argData.commandArgumentString(0)
        except RuntimeError:
            pass
        if argData.isFlagSet(kVerboseFlag):
            self.verbose = argData.flagArgumentBool(kVerboseFlag, 0)

        logger = setupLogger(self.verbose)
        self.mainWindow = MainWindow(logger)
        self.mainWindow.show()

        # Move the window to the cursor position.
        pos = Qt.QtGui.QCursor.pos()
        self.mainWindow.move(
            pos.x() - (self.mainWindow.width() / 2),
            pos.y() - (self.mainWindow.height() / 2))

        self.mainWindow.raise_()
        self.mainWindow.activateWindow()

    def undoIt(self):
        pass

    def redoIt(self):
        pass

    def isUndoable(self):
        return False


# Creator
def cmdCreator():
    # Create the command
    """

    Return:
        pointer to the command

    """
    ptr = OpenMayaMPx.asMPxPtr(Rush())
    return ptr


def syntaxCreator():
    """ Syntax creator

    Return:
        syntax (OpenMaya.MSyntax): return value

    """
    syntax = OpenMaya.MSyntax()
    syntax.addArg(OpenMaya.MSyntax.kString)
    syntax.addFlag(kVerboseFlag, kVerboseLongFlag, OpenMaya.MSyntax.kBoolean)
    return syntax


def initializePlugin(mobject):
    """ Initialize the script plug-in

    Args:
        mobject (OpenMaya.MObject):

    """
    mplugin = OpenMayaMPx.MFnPlugin(mobject, "Michitaka Inoue", "1.0", "Any")
    try:
        mplugin.registerCommand(kPluginCmdName, cmdCreator, syntaxCreator)
    except:
        sys.stderr.write("Failed to register command: %s\n" % kPluginCmdName)
        raise


def uninitializePlugin(mobject):
    """ Uninitialize the script plug-in

    Args:
        mobject (OpenMaya.MObject):

    """
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterCommand(kPluginCmdName)
    except:
        sys.stderr.write("Failed to unregister command: %s\n" % kPluginCmdName)
        raise
