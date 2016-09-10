import maya.cmds as cmds
import maya.mel as mel
import json
import os
import preference
import customWidgets
from Qt import QtWidgets, QtCore, QtGui
from pymel.all import mel as pa
reload(preference)
reload(customWidgets)


MAYA_SCRIPT_DIR = cmds.internalVar(userScriptDir=True)
MIEXEC_HISTORY_FILE = os.path.join(MAYA_SCRIPT_DIR, "miExecutorHistory.txt")
SCRIPT_PATH = os.path.dirname(__file__)


# Load pref data
prefDict = preference.miExecPref.getPreference()


# Load window setting
windowDict = preference.miExecPref.getWindowSetting()


# Load stylesheet data
qssFilePath = os.path.join(
    SCRIPT_PATH,
    "style",
    prefDict['style'],
    prefDict['style']) + ".qss"
qssFile = open(qssFilePath, "r")
qss = qssFile.read()
qssFile.close()


# Define mel procedure to call the previous function
mel.eval("""
global proc callLastCommand(string $function)
{
    repeatLast -ac $function -acl "blah-blah....";
}
""")


class UI(QtWidgets.QFrame):
    """ main UI class """

    # Dict to inherit all command dicrectories
    cmdDict = {}

    closeSignal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # These attributes will be used in MainClass as well
        self.windowWidth = windowDict['width']
        self.windowHeight = windowDict['height']
        self.windowTransparency = windowDict['transparent']

        self.windowSize = QtCore.QSize(
            self.windowWidth, self.windowHeight)
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
        self.filteredModel = QtCore.QSortFilterProxyModel(self)
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
        self.lineEdit = customWidgets.CustomQLineEdit()
        self.lineEdit.downPressed.connect(self.showHistory)
        # Apply stylesheet
        self.lineEdit.setStyleSheet(qss)

        self.lineEdit.setFixedHeight(windowDict['height'] - margin * 2)
        vbox = QtWidgets.QVBoxLayout()
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.addWidget(self.lineEdit)
        self.setLayout(vbox)

        # Set up QCompleter
        self.completer = QtWidgets.QCompleter(self)
        self.completer.setCompletionMode(
            QtWidgets.QCompleter.UnfilteredPopupCompletion)
        self.completer.highlighted.connect(self.selectionCallback)
        self.completer.setModel(self.filteredModel)
        self.completer.setObjectName("commandCompleter")
        self.completer.popup().setIconSize(self.iconSize)

        # Apply stylesheet
        self.completer.popup().setStyleSheet(qss)

        # Setup QCompleter for history
        self.histCompleter = QtWidgets.QCompleter(self)
        self.histCompleter.setCompletionMode(
            QtWidgets.QCompleter.UnfilteredPopupCompletion)
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
                """python(\"miExecutor.app.%s()._%s()\")""" % (
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
