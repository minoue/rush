from pymel.all import mel as pm
from maya import OpenMayaMPx
from maya import OpenMayaUI
from maya import OpenMaya
from maya import cmds
from maya import mel
try:
    import shiboken
except ImportError:
    import shiboken2 as shiboken

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


MAYA_SCRIPT_DIR = cmds.internalVar(userScriptDir=True)


# Define mel procedure to call the previous function
mel.eval("""
global proc callLastCommand(string $function)
{
    repeatLast -ac $function -acl "blah-blah....";
}
""")


# Load json files as dicrectory.
# key is command name, and its item is icon path.
commandFile = os.path.normpath(
    os.path.join(MAYA_SCRIPT_DIR, "rushCmds.json"))
try:
    f = open(commandFile)
    CMD_DICT = json.load(f)
    f.close()
except IOError:
    CMD_DICT = {}


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


def loadStyle():
    """ Load stylesheet

    Return:
        contents(str): stylesheet info in string

    """
    qss = os.path.normpath(
        os.path.join(MAYA_SCRIPT_DIR, "rush", "style.qss"))
    f = file(qss, 'r')
    contents = f.read()
    f.close()
    return contents


def getMayaWindow():
        ptr = OpenMayaUI.MQtUtil.mainWindow()
        return shiboken.wrapInstance(long(ptr), Qt.QtWidgets.QMainWindow)


class CustomQLineEdit(Qt.QtWidgets.QLineEdit):
    """ Custom QLineEdit with custom events and signals"""

    escPressed = Qt.QtCore.Signal(str)
    tabPressed = Qt.QtCore.Signal(str)

    def __init__(self, parent=None):
        super(CustomQLineEdit, self).__init__(parent)
        self.setFocusPolicy(Qt.QtCore.Qt.StrongFocus)

    def focusOutEvent(self, event):
        # Emit signal to close the window when it gets out of focus
        self.escPressed.emit('esc')

    def keyPressEvent(self, event):
        if event.key() == Qt.QtCore.Qt.Key_Escape:
            self.escPressed.emit('esc')
        elif event.key() == Qt.QtCore.Qt.Key_Tab:
            self.tabPressed.emit('tab')
        else:
            super(CustomQLineEdit, self).keyPressEvent(event)


class Gui(rush.RushCommands, Qt.QtWidgets.QDialog):

    def closeExistingWindow(self):
        """ Close window if exists """

        for qt in Qt.QtWidgets.QApplication.topLevelWidgets():
            try:
                if qt.__class__.__name__ == self.__class__.__name__:
                    qt.close()
            except:
                pass

    def __init__(self, logger, cmdDict, parent=None):
        """

        Args:
            logger (Logger): logger
            cmdDict (dict): Dict of all commands

        """
        self.closeExistingWindow()
        super(Gui, self).__init__(parent)

        self.logger = logger
        self.cmdDict = cmdDict

        self.setAttribute(Qt.QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Rush")
        self.setWindowFlags(Qt.QtCore.Qt.Window)
        self.setWindowFlags(
            Qt.QtCore.Qt.Popup | Qt.QtCore.Qt.FramelessWindowHint)
        try:
            self.setWindowFlags(
                self.windowFlags() | Qt.QtCore.Qt.NoDropShadowWindowHint)
        except AttributeError:
            pass

        # Dpi value to set the width for window and lineedit.
        # self.dpi = self.logicalDpiX()
        self.dpi = self.physicalDpiX()

        self.setStyleSheet(loadStyle())

        # Create Data then UI
        self.createData()
        self.createUI()

        self.setFixedWidth(self.dpi * 2)

    def createUI(self):
        self.LE = CustomQLineEdit(self)
        self.LE.setFixedWidth(self.dpi * 2)
        self.layout = Qt.QtWidgets.QBoxLayout(
            Qt.QtWidgets.QBoxLayout.TopToBottom)
        self.layout.addWidget(self.LE)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # Set up QCompleter
        self.completer = Qt.QtWidgets.QCompleter(self)
        self.completer.setCompletionMode(
            Qt.QtWidgets.QCompleter.UnfilteredPopupCompletion)
        self.completer.setModel(self.filteredModel)
        self.completer.setObjectName("commandCompleter")
        # self.completer.popup().setIconSize(self.iconSize)
        self.completer.popup().setStyleSheet(loadStyle())

        # Edit line Edit behavior
        self.LE.setCompleter(self.completer)
        self.LE.textEdited.connect(self.updateData)
        self.LE.returnPressed.connect(self.execute)
        self.LE.escPressed.connect(self.close)
        self.LE.tabPressed.connect(self.tabCompletion)
        self.LE.setFocus()

    def createData(self):
        """

        Return:
            QSortFilterProxyModel: data

        """

        model = Qt.QtGui.QStandardItemModel()

        # Create a list of command names
        self.commands = [i for i in self.cmdDict]

        # Add all command names and icon paths to the the model(model)
        for num, command in enumerate(self.cmdDict):
            item = Qt.QtGui.QStandardItem(command)
            if os.path.isabs(self.cmdDict[command]) is True:
                iconPath = os.path.normpath(self.cmdDict[command])
                item.setIcon(Qt.QtGui.QIcon(iconPath))
            else:
                item.setIcon(Qt.QtGui.QIcon(":%s" % self.cmdDict[command]))
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

    def tabCompletion(self):
        text = self.LE.text().lower()
        currents = [i for i in self.commands if text in i.lower()]
        top = currents[0]
        self.LE.setText(top)

    def execute(self):
        cmd = self.LE.text()

        # Close gui first otherwise maya clashes(2017)
        self.close()

        try:
            f = getattr(self, "_%s" % cmd)
            f()
            self.logger.debug("Running command : %s" % cmd)

            # Add to repeatLast command so the comamnd can be repeatable
            # by G key
            pm.callLastCommand(
                """python(\"rush.RushCommands()._%s()\")""" % cmd)
        except AttributeError:
            pass


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
        self.mw = Gui(logger, CMD_DICT, getMayaWindow())
        self.mw.show()

        pos = Qt.QtGui.QCursor.pos()
        self.mw.move(
            pos.x() - (self.mw.width() / 2),
            pos.y() - (self.mw.height() / 2))

        self.mw.raise_()
        self.mw.activateWindow()

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
    mplugin = OpenMayaMPx.MFnPlugin(mobject, "Michitaka Inoue", "2.0.1", "Any")
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
