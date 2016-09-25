try:
    # Try import Qt.py from global site-package, if not import copy of Qt.py
    # in a current directory
    import Qt
except ImportError:
    from . import Qt
import maya.cmds as cmds
import maya.mel as mel
import json
import os
import preference
import customWidgets
from pymel.all import mel as pa
reload(preference)
reload(customWidgets)


# Define mel procedure to call the previous function
mel.eval("""
global proc callLastCommand(string $function)
{
    repeatLast -ac $function -acl "blah-blah....";
}
""")


def loadQssFile():
    """ Load stylesheet data """

    # Load pref data
    prefDict = preference.miExecPref.getPreference()

    script_path = os.path.dirname(__file__)
    qssFilePath = os.path.join(
        script_path,
        "style",
        prefDict['style'],
        prefDict['style']) + ".qss"
    qssFile = open(qssFilePath, "r")
    qss = qssFile.read()
    qssFile.close()

    return qss


class UI(Qt.QtWidgets.QFrame):
    """ main UI class """

    # Dict to inherit all command dicrectories
    cmdDict = {}

    closeSignal = Qt.QtCore.Signal(str)

    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        self.setAttribute(Qt.QtCore.Qt.WA_DeleteOnClose)

        # Load window setting
        self.windowDict = preference.miExecPref.getWindowSetting()
        self.qss = loadQssFile()

        # These attributes will be used in MainClass as well
        self.windowWidth = self.windowDict['width']
        self.windowHeight = self.windowDict['height']
        self.windowTransparency = self.windowDict['transparent']

        self.windowSize = Qt.QtCore.QSize(
            self.windowWidth, self.windowHeight)
        self.iconSize = Qt.QtCore.QSize(
            self.windowDict['icon_size'], self.windowDict['icon_size'])

        self.setStyleSheet(self.qss)

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

        self.model = Qt.QtGui.QStandardItemModel()

        maya_script_dir = cmds.internalVar(userScriptDir=True)

        # Load json files as dicrectory.
        # key is command name, and its item is icon path.
        commandFile = os.path.normpath(
            os.path.join(maya_script_dir, "miExecutorCommands.json"))
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
            item = Qt.QtGui.QStandardItem(command)
            if os.path.isabs(jsonDict[command]) is True:
                iconPath = os.path.normpath(jsonDict[command])
                item.setIcon(Qt.QtGui.QIcon(iconPath))
            else:
                item.setIcon(Qt.QtGui.QIcon(":%s" % jsonDict[command]))
            self.model.setItem(num, 0, item)

        # Store the model(self.model) into the sortFilterProxy model
        self.filteredModel = Qt.QtCore.QSortFilterProxyModel(self)
        self.filteredModel.setFilterCaseSensitivity(
            Qt.QtCore.Qt.CaseInsensitive)
        self.filteredModel.setSourceModel(self.model)

        # History model
        self.historyList = loadHistoryList()
        self.historyModel = Qt.QtGui.QStandardItemModel()
        try:
            for num, command in enumerate(self.historyList):
                item = Qt.QtGui.QStandardItem(command)
                if os.path.isabs(jsonDict[command]) is True:
                    iconPath = os.path.normpath(jsonDict[command])
                    item.setIcon(Qt.QtGui.QIcon(iconPath))
                else:
                    item.setIcon(Qt.QtGui.QIcon(":%s" % jsonDict[command]))
                self.historyModel.setItem(num, 0, item)
        except KeyError:
            pass

    def createUI(self):
        """ Create UI """

        margin = self.windowDict['margin']
        self.lineEdit = customWidgets.CustomQLineEdit(self)
        self.lineEdit.downPressed.connect(self.showHistory)

        # Apply stylesheet
        self.lineEdit.setStyleSheet(self.qss)

        self.lineEdit.setFixedHeight(self.windowDict['height'] - margin * 2)
        vbox = Qt.QtWidgets.QVBoxLayout()
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.addWidget(self.lineEdit)
        self.setLayout(vbox)

        # Set up QCompleter
        self.completer = Qt.QtWidgets.QCompleter(self)
        self.completer.setCompletionMode(
            Qt.QtWidgets.QCompleter.UnfilteredPopupCompletion)
        self.completer.highlighted.connect(self.selectionCallback)
        self.completer.setModel(self.filteredModel)
        self.completer.setObjectName("commandCompleter")
        self.completer.popup().setIconSize(self.iconSize)

        # Setup QCompleter for history
        self.histCompleter = Qt.QtWidgets.QCompleter(self)
        self.histCompleter.setCompletionMode(
            Qt.QtWidgets.QCompleter.UnfilteredPopupCompletion)
        self.histCompleter.setModel(self.historyModel)
        self.histCompleter.setObjectName("historyCompleter")

        # Apply stylesheet
        self.completer.popup().setStyleSheet(self.qss)
        self.histCompleter.popup().setStyleSheet(self.qss)

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
        regExp = Qt.QtCore.QRegExp(
            self.lineEdit.text(),
            Qt.QtCore.Qt.CaseInsensitive,
            Qt.QtCore.QRegExp.RegExp)
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


def getHistoryFilePath():
    maya_script_dir = cmds.internalVar(userScriptDir=True)
    path = os.path.join(maya_script_dir, "miExecutorHistory.txt")
    return path


def loadHistoryList():
    """ Clear history list """

    historyFilePath = getHistoryFilePath()

    if not os.path.exists(historyFilePath):
        # Create empty text file for history
        open(historyFilePath, 'a').close()

    with open(historyFilePath, 'r') as histFile:
        histories = [i.rstrip() for i in histFile.readlines()]
        return histories


def updateHistory(command):
    """ Update and rewrite history list to file """

    historyList = loadHistoryList()
    historyFilePath = getHistoryFilePath()
    if command in historyList:
        historyList.remove(command)
    historyList.insert(0, command)
    with open(historyFilePath, 'w') as histFile:
        for i in historyList:
            histFile.write(i + "\n")
