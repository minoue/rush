from PyQt4 import QtCore, QtGui
from pymel.all import mel as pa
import maya.OpenMayaUI as mui
import maya.cmds as cmds
import maya.mel as mel
import os
import sys
import json
from pref import miExecutorCommands
reload(miExecutorCommands)
try:
    import sip
except ImportError:
    import PyQt4.sip as sip


# MEL PROCEDUAL TO CALL LAST FUNCTION
mel.eval("""
global proc callLastCommand(string $function)
{
    repeatLast -ac $function -acl "blah-blah....";
}
""")


def getMayaWindow():
    ptr = mui.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)


class MiExecutor(QtGui.QWidget, miExecutorCommands.Commands):

    def __init__(self, parent=getMayaWindow()):
        super(MiExecutor, self).__init__()
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setWindowTitle("miExecutor")
        self.setWindowFlags(QtCore.Qt.Popup | QtCore.Qt.FramelessWindowHint)
        self.setFixedSize(200, 20)

        osType = sys.platform
        if osType == "darwin":
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        elif osType == "linux2":
            # Composite Window needs be enabled
            # in linux to use window transparent
            pass
        elif osType == "win32":
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        else:
            pass

        # Attribute to check if item on the popup list is selected
        self._selected = None

        # 0: when return pressed without
        #    selecting an item on the completion list
        # 1: when an item on the completion list is selected by arrow keys
        self.executeType = 0

        self.createData()
        self.createUI()

    def createData(self):
        self.model = QtGui.QStandardItemModel()

        commandFile = os.path.normpath(
            os.path.join(os.path.dirname(__file__), "pref/commands.json"))
        jsonDict = json.load(open(commandFile))
        self.commands = [i for i in jsonDict]

        for i, command in enumerate(jsonDict):
            item = QtGui.QStandardItem(command)
            if os.path.isabs(jsonDict[command]) is True:
                item.setIcon(QtGui.QIcon("%s" % jsonDict[command]))
            else:
                item.setIcon(QtGui.QIcon(":%s" % jsonDict[command]))
            self.model.setItem(i, 0, item)

        self.filteredModel = QtGui.QSortFilterProxyModel(self)
        self.filteredModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.filteredModel.setSourceModel(self.model)

    def createUI(self):
        self.lineEdit = QtGui.QLineEdit(self)

        vbox = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom, self)
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

        # Edit line Edit behavior
        self.lineEdit.setCompleter(self.completer)
        self.lineEdit.textEdited.connect(self.updateData)
        self.lineEdit.returnPressed.connect(self.initialExecution)
        self.lineEdit.textChanged.connect(self.getCurrentCompletion)
        self.lineEdit.setFocus()

    def updateData(self):
        regExp = QtCore.QRegExp(self.lineEdit.text(),
                                QtCore.Qt.CaseInsensitive,
                                QtCore.QRegExp.RegExp)
        self.filteredModel.setFilterRegExp(regExp)

    def selectionCallback(self, selected):
        self._selected = selected
        self.executeType = 1
        return self._selected

    def getCurrentCompletion(self, *args):
        self.curCompPrefix = self.completer.completionPrefix().toLower()
        self.curCompList = [i for i
                            in self.commands
                            if self.curCompPrefix in i.lower()]
        try:
            self.currentCompletion = self.curCompList[0]
        except IndexError:
            self.currentCompletion = None

        currentCompletion = self.completer.currentCompletion()
        if str(currentCompletion) == "":
            pass
        else:
            self.currentCompletion = currentCompletion

        return self.currentCompletion

    def initialExecution(self):
        try:
            self.secondaryExecution()
        except RuntimeError:
            cmds.warning("Command not found. No object created.")
            self.close()
            return

        if self.lastCommand is not None:
            className = self.__class__.__name__
            pa.callLastCommand(
                """python(\"miExecutor_PyQt4.%s()._%s()\")""" % (
                    className, self.lastCommand))
        else:
            cmds.warning("Command not found. No object created.")

    def secondaryExecution(self):
        if self.executeType == 0:
            if self.currentCompletion is None:
                self.close()
                self.lastCommand = None
                return self.lastCommand
            else:
                commandString = "self._%s()" % self.currentCompletion
                exec commandString
                self.close()
                self.lastCommand = self.currentCompletion
                return self.lastCommand
        elif self.executeType == 1:
            commandString = "self._%s()" % self._selected
            exec commandString
            self.close()
            self.lastCommand = self._selected
            return self.lastCommand
        else:
            pass

    def main(self):
        global executorWin
        try:
            executorWin.close()
        except NameError:
            pass
        executorWin = MiExecutor()
        executorWin.show()

        pos = QtGui.QCursor.pos()
        executorWin.move(
            pos.x() - (self.width() / 2), pos.y() - (self.height() / 2))
        executorWin.activateWindow()
        executorWin.raise_()
