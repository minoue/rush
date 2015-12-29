from PySide import QtGui, QtCore
import maya.cmds as cmds
import maya.mel as mel
from pymel.all import mel as pa
import maya.OpenMayaUI as mui
import os
import json
import shiboken
import imp


MAYA_SCRIPT_DIR = cmds.internalVar(userScriptDir=True)
MIEXEC_HISTORY_FILE = os.path.join(MAYA_SCRIPT_DIR, "miExecutorHistory.txt")
SCRIPT_PATH = os.path.dirname(__file__)
MODULE_PATH = os.path.join(SCRIPT_PATH, 'module')


# Define mel procedure to call the previous function
mel.eval("""
global proc callLastCommand(string $function)
{
    repeatLast -ac $function -acl "blah-blah....";
}
""")


# Load pref data
prefFile = open(os.path.join(SCRIPT_PATH, "pref.json"), 'r')
prefDict = json.load(prefFile)
prefFile.close()


# Load stylesheet data
qssFilePath = os.path.join(
    SCRIPT_PATH,
    "style",
    prefDict['style'],
    prefDict['style']) + ".qss"
qssFile = open(qssFilePath, "r")
qss = qssFile.read()
qssFile.close()


# Load window setting
windowFilePath = os.path.join(
    SCRIPT_PATH,
    "style",
    prefDict['style'],
    "window.json")
windowFile = open(windowFilePath, 'r')
windowDict = json.load(windowFile)
windowFile.close()


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


# Reload all modules
for m in moduleObjectList:
    reload(m)


# Append extra module objects
moduleObjectList.extend(extraModObjectList)


# List of all Commands class
commandClassList = [i.Commands for i in moduleObjectList]


def getMayaWindow():
    ptr = mui.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(ptr), QtGui.QMainWindow)


class CustomQLineEdit(QtGui.QLineEdit):
    """ Custom QLineEdit with custom events and signals"""

    escPressed = QtCore.Signal(str)
    downPressed = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(CustomQLineEdit, self).__init__(parent)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def focusOutEvent(self, event):
        # emit signal to close the window when it gets focus out
        self.escPressed.emit('esc')

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.escPressed.emit('esc')

        elif event.key() == QtCore.Qt.Key_Down:
            self.downPressed.emit('down')
        else:
            super(CustomQLineEdit, self).keyPressEvent(event)


class UI(QtGui.QFrame):
    """ main UI class """

    # Dict to inherit all command dicrectories
    cmdDict = {}

    closeSignal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.windowSize = QtCore.QSize(
            windowDict['width'], windowDict['height'])
        self.iconSize = QtCore.QSize(
            windowDict['icon_size'], windowDict['icon_size'])

        self.setStyleSheet(qss)

        # Attribute to check if item on the popup list is selected
        self._selected = None

        # 0: When return pressed without selecting any items
        #    on the completion list
        # 1: when any items on the completion list is selected by arrow keys
        # Default is 1
        self.executeType = 0

        # Create Data then UI
        self.createData()
        self.createUI()

    def createData(self):
        """ Create item models for completers """

        self.model = QtGui.QStandardItemModel()

        # Load json files as dicrectory.
        # key is command name, and its item is icon path.
        commandFile = os.path.normpath(
            os.path.join(MAYA_SCRIPT_DIR, "miExecutorCommands.json"))
        try:
            f = open(commandFile)
            jsonDict = json.load(f)
            f.close()
        except IOError:
            jsonDict = {}

        # Create a list of command names
        self.commands = [i for i in jsonDict]

        # Add all command names and icon paths to the the model(self.model)
        for num, command in enumerate(jsonDict):
            item = QtGui.QStandardItem(command)
            if os.path.isabs(jsonDict[command]) is True:
                iconPath = os.path.normpath(jsonDict[command])
                item.setIcon(QtGui.QIcon(iconPath))
            else:
                item.setIcon(QtGui.QIcon(":%s" % jsonDict[command]))
            self.model.setItem(num, 0, item)

        # Store the model(self.model) into the sortFilterProxy model
        self.filteredModel = QtGui.QSortFilterProxyModel(self)
        self.filteredModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.filteredModel.setSourceModel(self.model)

        # History model
        self.historyList = loadHistory()
        self.historyModel = QtGui.QStandardItemModel()
        try:
            for num, command in enumerate(self.historyList):
                item = QtGui.QStandardItem(command)
                if os.path.isabs(jsonDict[command]) is True:
                    iconPath = os.path.normpath(jsonDict[command])
                    item.setIcon(QtGui.QIcon(iconPath))
                else:
                    item.setIcon(QtGui.QIcon(":%s" % jsonDict[command]))
                self.historyModel.setItem(num, 0, item)
        except KeyError:
            pass

    def createUI(self):
        """ Create UI """

        margin = windowDict['margin']
        self.lineEdit = CustomQLineEdit()
        self.lineEdit.downPressed.connect(self.showHistory)

        # Apply stylesheet
        self.lineEdit.setStyleSheet(qss)

        self.lineEdit.setFixedHeight(windowDict['height'] - margin * 2)
        vbox = QtGui.QVBoxLayout()
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.addWidget(self.lineEdit)
        self.setLayout(vbox)

        # Set up QCompleter
        self.completer = QtGui.QCompleter(self)
        self.completer.setCompletionMode(
            QtGui.QCompleter.UnfilteredPopupCompletion)
        self.completer.highlighted.connect(self.selectionCallback)
        self.completer.setModel(self.filteredModel)
        self.completer.setObjectName("commandCompleter")
        self.completer.popup().setIconSize(self.iconSize)

        # Apply stylesheet
        self.completer.popup().setStyleSheet(qss)

        # Setup QCompleter for history
        self.histCompleter = QtGui.QCompleter()
        self.histCompleter.setCompletionMode(
            QtGui.QCompleter.UnfilteredPopupCompletion)
        self.histCompleter.setModel(self.historyModel)
        self.histCompleter.setObjectName("historyCompleter")

        # Edit line Edit behavior
        self.lineEdit.setCompleter(self.completer)
        self.lineEdit.textEdited.connect(self.updateData)
        self.lineEdit.textChanged.connect(self.getCurrentCompletion)
        self.lineEdit.returnPressed.connect(self.initialExecution)
        self.lineEdit.setFocus()

    def showHistory(self, *args):
        """ Show previously executed commands """

        self.lineEdit.setCompleter(self.histCompleter)
        self.histCompleter.complete()

    def updateData(self):
        """ Update current completion data """

        # If text is empty, change history completer back to
        # command completer
        currentText = self.lineEdit.text()
        if currentText == "":
            self.lineEdit.setCompleter(self.completer)

        # Set commands to case insensitive
        regExp = QtCore.QRegExp(self.lineEdit.text(),
                                QtCore.Qt.CaseInsensitive,
                                QtCore.QRegExp.RegExp)
        self.filteredModel.setFilterRegExp(regExp)

    def selectionCallback(self, selected):
        """ Return highlighted command """

        self._selected = selected
        self.executeType = 1
        return self._selected

    def getCurrentCompletion(self, *args):
        """ Get a command to be completed """

        compType = self.lineEdit.completer().objectName()
        if compType == "commandCompleter":
            self.curCompPrefix = self.completer.completionPrefix().lower()
            self.curCompList = [i for i
                                in self.commands
                                if self.curCompPrefix in i.lower()]
            try:
                self.currentCompletion = self.curCompList[0]
            except IndexError:
                self.currentCompletion = None

            currentCompletion = self.completer.currentCompletion()

            # If currentCompletion by QCompleter is empty, use the top item
            # in the self.curComList instead.
            if str(currentCompletion) == "":
                pass
            else:
                self.currentCompletion = currentCompletion

        elif compType == "historyCompleter":
            self.currentCompletion = self.lineEdit.text()

        else:
            pass

        return self.currentCompletion

    def initialExecution(self):
        """ Execute actuall command and register it to last command """

        try:
            # Run command
            self.secondaryExecution()
        except RuntimeError:
            cmds.warning("Command not found. No object created.")
            self.close()
            return

        # Send the last command to the mel procedure defined
        # at the begging of the script
        if self.lastCommand is not None:
            className = self.__class__.__name__
            pa.callLastCommand(
                """python(\"miExecutor.%s()._%s()\")""" % (
                    className, self.lastCommand))
        else:
            cmds.warning("Command not found. No object created.")

    def secondaryExecution(self):
        """ Execute command """

        # When return pressed without selecting any items
        # on the completion list
        if self.executeType == 0:
            if self.currentCompletion is None:
                self.close()
                self.lastCommand = None
            else:
                commandString = "self._%s()" % self.currentCompletion
                exec commandString
                self.close()
                self.lastCommand = self.currentCompletion
        # when any items on the completion list is selected by arrow keys
        elif self.executeType == 1:
            commandString = "self._%s()" % self._selected
            exec commandString
            self.close()
            self.lastCommand = self._selected
        else:
            pass

        updateHistory(self.lastCommand)

        self.closeSignal.emit('foobar')

        return self.lastCommand


class MainClass():
    """
    This is the main class which will interit all command classes
    from all command modules
    """

    pass


# Create a list of class objects.
CLASSLIST = [UI]
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
            UI.cmdDict.update(c.commandDict)
        except:
            print "%s does not have commandDict Attribute" % c

    outFilePath = os.path.normpath(
        os.path.join(MAYA_SCRIPT_DIR, "miExecutorCommands.json"))

    with open(outFilePath, 'w') as outFile:
        json.dump(UI.cmdDict,
                  outFile,
                  indent=4,
                  separators=(',', ':'),
                  sort_keys=True)


def loadHistory():
    """ Clear history list """

    if not os.path.exists(MIEXEC_HISTORY_FILE):
        # Create empty text file for history
        open(MIEXEC_HISTORY_FILE, 'a').close()

    with open(MIEXEC_HISTORY_FILE, 'r') as histFile:
        histories = [i.rstrip() for i in histFile.readlines()]
        return histories


def updateHistory(command):
    """ Update and rewrite history list to file """

    historyList = loadHistory()
    if command in historyList:
        historyList.remove(command)
    historyList.insert(0, command)
    with open(MIEXEC_HISTORY_FILE, 'w') as histFile:
        for i in historyList:
            histFile.write(i + "\n")


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
