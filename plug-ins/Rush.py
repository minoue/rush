"""
Rush, tab-menu like command launcher
"""

import sys
import os

from maya import OpenMayaUI
from maya.api import OpenMaya
from maya import cmds
from maya import mel
from PySide2 import QtGui, QtWidgets, QtCore
import shiboken2
from importlib import reload

import rush
reload(rush)


__author__ = "Michi Inoue"
__version__ = "2.9.1"
PLUGIN_COMMAND = "rush2"


QSS = """
QWidget {
    background-color: rgb(42, 42, 42);
    border-style: solid;
    border-radius: 0px;
    adding: 0px;
    border-width: 0px;
    border-color: rgb(68, 68, 68);
    font-size: 14pt;
}
"""


# Define mel procedure to call the previous function
mel.eval("""
global proc callLastCommand(string $function)
{
    repeatLast -ac $function -acl "blah-blah....";
}
""")


def getMayaWindow():
    """ Get main window pointer """

    ptr = OpenMayaUI.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(ptr), QtWidgets.QMainWindow)


class History(object):
    """ Custom class to read/write command history """

    def __init__(self):

        self.history = self.read()

    @classmethod
    def read(cls) -> list:
        """ Load history

        Return:
            history(list): list of commands

        """

        mayaScriptDir = cmds.internalVar(userScriptDir=True)
        historyPath = os.path.join(mayaScriptDir, "rushHistory.txt")

        if os.path.exists(historyPath):
            try:
                historyFile = open(historyPath, 'r')
                history = historyFile.read().splitlines()
                historyFile.close()
                return history
            except IOError:
                return []
        else:
            return []

    def append(self, uuid: str):
        """ append history

        Args:
            uuid (str): uuid of a command

        Return:
            None

        """
        # If command already exists in the history, move it to the front
        if uuid in self.history:
            self.history.insert(
                0, self.history.pop(self.history.index(uuid)))
        else:
            self.history.insert(0, uuid)

        # Set maximum number of histories
        self.history = self.history[:25]

    def save(self):
        """ Write history

        """

        mayaScriptDir = cmds.internalVar(userScriptDir=True)
        historyPath = os.path.join(mayaScriptDir, "rushHistory.txt")
        try:
            historyFile = open(historyPath, 'w')
            for line in self.history:
                historyFile.write(line + "\n")
            historyFile.close()
        except IOError:
            pass

    def clear(self):
        """ Clear history

        Return:
            None

        """
        pass


class CustomQLineEdit(QtWidgets.QLineEdit):
    """ Custom QLineEdit with custom events and signals
    Reference:
    https://ilmvfx.wordpress.com/2016/11/02/how-to-add-a-search-icon-and-clear-button-to-qlineedit/
    """

    escPressed = QtCore.Signal(str)
    tabPressed = QtCore.Signal(str)
    backtabPressed = QtCore.Signal(str)
    arrowPressed = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(CustomQLineEdit, self).__init__(parent)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        b64Data = (
            'PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tI'
            'EdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMTYuMC4wLCBTVkcgRXhwb3J0IF'
            'BsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjwhRE9DVFl'
            'QRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93'
            'd3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+Cjxzdmcge'
            'G1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaH'
            'R0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiBpZD0iQ2F'
            'wYV8xIiB4PSIwcHgiIHk9IjBweCIgd2lkdGg9IjMycHgiIGhlaWdodD0iMzJweCIg'
            'dmlld0JveD0iMCAwIDQ4NS4yMTMgNDg1LjIxMyIgc3R5bGU9ImVuYWJsZS1iYWNrZ'
            '3JvdW5kOm5ldyAwIDAgNDg1LjIxMyA0ODUuMjEzOyIgeG1sOnNwYWNlPSJwcmVzZX'
            'J2ZSI+CjxnPgoJPGc+CgkJPHBhdGggZD0iTTQ3MS44ODIsNDA3LjU2N0wzNjAuNTY'
            '3LDI5Ni4yNDNjLTE2LjU4NiwyNS43OTUtMzguNTM2LDQ3LjczNC02NC4zMzEsNjQu'
            'MzIxbDExMS4zMjQsMTExLjMyNCAgICBjMTcuNzcyLDE3Ljc2OCw0Ni41ODcsMTcuN'
            'zY4LDY0LjMyMSwwQzQ4OS42NTQsNDU0LjE0OSw0ODkuNjU0LDQyNS4zMzQsNDcxLj'
            'g4Miw0MDcuNTY3eiIgZmlsbD0iI0ZGRkZGRiIvPgoJCTxwYXRoIGQ9Ik0zNjMuOTA'
            '5LDE4MS45NTVDMzYzLjkwOSw4MS40NzMsMjgyLjQ0LDAsMTgxLjk1NiwwQzgxLjQ3'
            'NCwwLDAuMDAxLDgxLjQ3MywwLjAwMSwxODEuOTU1czgxLjQ3MywxODEuOTUxLDE4M'
            'S45NTUsMTgxLjk1MSAgICBDMjgyLjQ0LDM2My45MDYsMzYzLjkwOSwyODIuNDM3LD'
            'M2My45MDksMTgxLjk1NXogTTE4MS45NTYsMzE4LjQxNmMtNzUuMjUyLDAtMTM2LjQ'
            '2NS02MS4yMDgtMTM2LjQ2NS0xMzYuNDYgICAgYzAtNzUuMjUyLDYxLjIxMy0xMzYu'
            'NDY1LDEzNi40NjUtMTM2LjQ2NWM3NS4yNSwwLDEzNi40NjgsNjEuMjEzLDEzNi40N'
            'jgsMTM2LjQ2NSAgICBDMzE4LjQyNCwyNTcuMjA4LDI1Ny4yMDYsMzE4LjQxNiwxOD'
            'EuOTU2LDMxOC40MTZ6IiBmaWxsPSIjRkZGRkZGIi8+CgkJPHBhdGggZD0iTTc1Ljg'
            'xNywxODEuOTU1aDMwLjMyMmMwLTQxLjgwMywzNC4wMTQtNzUuODE0LDc1LjgxNi03'
            'NS44MTRWNzUuODE2QzEyMy40MzgsNzUuODE2LDc1LjgxNywxMjMuNDM3LDc1LjgxN'
            'ywxODEuOTU1eiIgZmlsbD0iI0ZGRkZGRiIvPgoJPC9nPgo8L2c+CjxnPgo8L2c+Cj'
            'xnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo'
            '8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+'
            'CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+Cjwvc3ZnPgo=')

        data = QtCore.QByteArray.fromBase64(b64Data.encode())
        tempPixmap = QtGui.QPixmap()
        tempPixmap.loadFromData(data)
        self.iconPixmap = tempPixmap.scaled(
            20,
            20,
            QtCore.Qt.IgnoreAspectRatio,
            QtCore.Qt.SmoothTransformation)

        self.setTextMargins(30, 0, 0, 0)

    def focusOutEvent(self, event):
        # Emit signal to close the window when it gets out of focus
        self.escPressed.emit('esc')

    def keyPressEvent(self, event):

        if event.key() == QtCore.Qt.Key_Escape:
            self.escPressed.emit('esc')
        elif event.key() == QtCore.Qt.Key_Tab:
            self.tabPressed.emit('tab')
        elif event.key() == QtCore.Qt.Key_Backtab:
            self.backtabPressed.emit('backtab')
        elif event.key() == QtCore.Qt.Key_Down:
            self.arrowPressed.emit('down')
        elif event.key() == QtCore.Qt.Key_Up:
            self.arrowPressed.emit('up')
        else:
            super(CustomQLineEdit, self).keyPressEvent(event)

    def paintEvent(self, event):
        super(CustomQLineEdit, self).paintEvent(event)

        painter = QtGui.QPainter(self)
        painter.setOpacity(0.75)
        height = self.iconPixmap.height()
        rightBorder = 8
        painter.drawPixmap(
            rightBorder+2, (self.height() - height) / 2, self.iconPixmap)


class CustomQTableView(QtWidgets.QTableView):
    """ Custom QTableView """

    tabPressed = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(CustomQTableView, self).__init__(parent)

        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setShowGrid(False)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # header
        self.verticalHeader().hide()
        self.horizontalHeader().hide()
        self.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Fixed)
        self.horizontalHeader().setStretchLastSection(True)

        # scrollbar
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.verticalScrollBar().hide()
        self.horizontalScrollBar().hide()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Tab:
            self.tabPressed.emit('tab')
        else:
            super(CustomQTableView, self).keyPressEvent(event)


class Database():

    def __init__(self):
        self.command_dict = {**rush.cmdDict, **rush.TmpCls.commandDict}

        self.filteredModel = self.createCompletionData()
        self.historyModel = self.createHistoryData()

    def createCompletionData(self) -> QtCore.QSortFilterProxyModel:
        model = QtGui.QStandardItemModel()

        # Add all command names and icon paths to the the model(model)
        for uuid in self.command_dict:
            # 1st column
            dataDict = self.command_dict[uuid]
            label = dataDict["label"]
            icon = dataDict["icon"]
            item = QtGui.QStandardItem(label)
            if os.path.isabs(icon) is True:
                iconPath = os.path.normpath(icon)
                item.setIcon(QtGui.QIcon(iconPath))
            else:
                if icon == "":
                    item.setIcon(QtGui.QIcon(":commandButton.png"))
                else:
                    item.setIcon(QtGui.QIcon(":%s" % icon))

            item.setData(uuid, 4)

            # 2nd column
            module = QtGui.QStandardItem(dataDict['module'])
            module.setTextAlignment(
                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            font = module.font()
            font.setItalic(True)
            font.setPointSize(11)
            module.setFont(font)
            item.setEditable(False)
            module.setEditable(False)

            # set item
            model.appendRow([item, module])

        # Store the model(model) into the sortFilterProxy model
        filteredModel = QtCore.QSortFilterProxyModel()
        filteredModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        filteredModel.setSourceModel(model)

        return filteredModel

    def createHistoryData(self) -> QtCore.QSortFilterProxyModel:
        """ Create data for history list """

        # History model
        historyList = History.read()
        historyModel = QtGui.QStandardItemModel()

        for uuid in historyList:

            label = self.command_dict[uuid]["label"]

            # Capitalize the first letter of the command
            displayName = label[:1].capitalize() + label[1:]

            item = QtGui.QStandardItem(displayName)
            icon = self.command_dict[uuid]['icon']

            if os.path.isabs(icon) is True:
                iconPath = os.path.normpath(icon)
                item.setIcon(QtGui.QIcon(iconPath))
            else:
                item.setIcon(
                    QtGui.QIcon(":%s" % icon))

            item.setData(uuid, 4)

            module = QtGui.QStandardItem("History")
            module.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            font = module.font()
            font.setItalic(True)
            font.setPointSize(11)
            module.setFont(font)
            item.setEditable(False)
            module.setEditable(False)
            historyModel.appendRow([item, module])

        # Store the model(model) into the sortFilterProxy model
        historyFilteredModel = QtCore.QSortFilterProxyModel()
        historyFilteredModel.setFilterCaseSensitivity(
            QtCore.Qt.CaseInsensitive)
        historyFilteredModel.setSourceModel(historyModel)

        return historyFilteredModel


# Create data only once when plugin is activated
DATA = Database()


class Gui(rush.TmpCls, QtWidgets.QWidget):
    """ Gui class """

    def __init__(self, parent=None):
        super(Gui, self).__init__(parent)

        self.history = History()

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Rush")
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowFlags(QtCore.Qt.Popup | QtCore.Qt.FramelessWindowHint)

        self.completeMode = None

        # Dpi value to set the width for window and lineedit.
        self.dpi = self.physicalDpiX()

        self.setStyleSheet(QSS)
        margin = 5
        self.setContentsMargins(margin, margin, margin, margin)

        # Create Data then UI
        # Those data are created only once when the plugin is activated.
        self.cmdDict = DATA.command_dict
        self.filteredModel = DATA.filteredModel

        # History dynamically changes so run everytime window is created.
        self.historyModel = DATA.createHistoryData()

        # self.createHistoryData()
        self.createUI()

        self.toolWidth = self.dpi * 6
        self.toolHeight = 70
        self.setFixedWidth(self.toolWidth)

        self.currentRow = 0

    def createUI(self):
        """ docstring """

        self.cmdsLE = CustomQLineEdit(self)
        self.cmdsLE.setPlaceholderText("Search")
        self.cmdsLE.setFixedHeight(30)

        self.cmdsView = CustomQTableView()
        self.cmdsView.setVisible(False)
        self.cmdsView.setModel(self.filteredModel)
        self.cmdsView.horizontalHeader().resizeSection(0, 400)
        self.cmdsViewSelModel = self.cmdsView.selectionModel()
        self.cmdsViewSelModel.selectionChanged.connect(self.viewSelectionChanged)

        self.historyView = CustomQTableView()
        self.historyView.setVisible(False)
        self.historyView.setModel(self.historyModel)
        self.historyView.horizontalHeader().resizeSection(0, 400)

        # Layout
        self.layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.TopToBottom)
        self.layout.addWidget(self.cmdsLE)
        self.layout.addWidget(self.cmdsView)
        self.layout.addWidget(self.historyView)
        self.layout.setSpacing(5)
        self.setLayout(self.layout)

        self.cmdsLE.textEdited.connect(self.showCompleter)
        self.cmdsLE.returnPressed.connect(self.execute)
        self.cmdsLE.escPressed.connect(self.close)
        self.cmdsLE.tabPressed.connect(self.complete)
        self.cmdsLE.backtabPressed.connect(self.complete)
        self.cmdsLE.arrowPressed.connect(self.arrowPressed)
        self.cmdsLE.setFocus()

        self.showHistory()

    def viewSelectionChanged(self, item: QtCore.QItemSelection):

        indexes = item.indexes()
        if len(indexes) == 2:
            index = indexes[0]
            data = self.filteredModel.itemData(index)
            command_uuid = data[4]
            command_label = self.cmdDict[command_uuid]["label"]
            # command_exec = self.cmdDict[command_uuid]["command"]
            self.cmdsLE.setText(command_label)

    def showCompleter(self, *args):
        """ Show commands

        """
        self.updateData()

        if self.cmdsLE.text() == "":
            self.completeMode = None
        else:
            self.completeMode = "normal"

    def complete(self, *args):
        """ docstring """

        tabType = args[0]

        if self.completeMode == "normal":
            if tabType == "tab":
                self.tabComplete(self.cmdsView, self.filteredModel)
            else:
                self.shiftTabComplete(self.cmdsView, self.filteredModel)
        elif self.completeMode == "history":
            if tabType == "tab":
                self.tabComplete(self.historyView, self.historyModel)
            else:
                self.shiftTabComplete(
                    self.historyView, self.historyModel)
        else:
            pass

    def arrowPressed(self, direction: str):
        # type: (str) -> None
        """ key press event when arrow key pressed

        Args:
            direction (str): "down" or "up"

        """

        if direction == "down":
            self.downPressed()
        if direction == "up":
            self.upPressed()
        else:
            pass

    def showHistory(self):
        self.cmdsView.setVisible(False)
        self.historyView.setVisible(True)
        self.historyView.setFixedHeight(390)
        self.setFixedHeight(390)
        self.completeMode = "history"

    def downPressed(self):
        """ Down arrow key pressed event """

        if self.completeMode is None:
            # Show history view
            self.showHistory()
        elif self.completeMode == "normal":
            self.tabComplete(self.cmdsView, self.filteredModel)
        elif self.completeMode == "history":
            self.tabComplete(self.historyView, self.historyModel)
        else:
            pass

        if self.cmdsLE.text() != "":
            return

    def upPressed(self):
        """ Up arrow key pressed event """

        if self.completeMode == "normal":
            self.shiftTabComplete(self.cmdsView, self.filteredModel)
        elif self.completeMode == "history":
            self.shiftTabComplete(self.historyView, self.historyModel)
        else:
            pass

        if self.cmdsLE.text() != "":
            return

    def createHistoryData(self):
        """ Create data for history list """

        # History model
        self.historyList = self.history.read()
        self.historyModel = QtGui.QStandardItemModel()

        for uuid in self.historyList:

            command = self.cmdDict[uuid]["label"]

            # Capitalize the first letter of the command
            displayName = command[:1].capitalize() + command[1:]

            # If a command dosen't exist in the history list,
            # for some reason(eg. command renamed), do nothing.
            if displayName not in self.cmdDict:
                continue

            item = QtGui.QStandardItem(displayName)
            if os.path.isabs(self.cmdDict[displayName]['icon']) is True:
                iconPath = os.path.normpath(self.cmdDict[displayName]['icon'])
                item.setIcon(QtGui.QIcon(iconPath))
            else:
                item.setIcon(
                    QtGui.QIcon(":%s" % self.cmdDict[displayName]['icon']))
            module = QtGui.QStandardItem("History")
            module.setTextAlignment(
                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            font = module.font()
            font.setItalic(True)
            font.setPointSize(11)
            module.setFont(font)
            item.setEditable(False)
            module.setEditable(False)
            self.historyModel.appendRow([item, module])

        # Store the model(model) into the sortFilterProxy model
        self.historyFilteredModel = QtCore.QSortFilterProxyModel(self)
        self.historyFilteredModel.setFilterCaseSensitivity(
            QtCore.Qt.CaseInsensitive)
        self.historyFilteredModel.setSourceModel(self.historyModel)

    def updateData(self):
        """ Update current completion data

        """

        text = self.cmdsLE.text()

        if text == "":
            self.cmdsView.setVisible(False)
            self.historyView.setVisible(False)
            self.setFixedHeight(55)
        else:
            self.historyView.setVisible(False)
            self.cmdsView.setVisible(True)
            self.setFixedHeight(300)

        if " " in text:
            # If multiple words separated by whitespace
            words = text.rstrip()  # Remove whitespace at the end
            wordList = words.split(" ")
            text = "^"
            for word in wordList:
                text += "(?=.*{})".format(word)

        # Set commands to case insensitive
        regExp = QtCore.QRegExp(
            text, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)

        self.filteredModel.setFilterRegExp(regExp)

        numRows = self.cmdsView.model().rowCount()
        if numRows == 0:
            self.cmdsView.setVisible(False)

        # Resize window based on number rows
        if numRows < 8:
            height = 36 * numRows + 55 + 4
            self.setFixedHeight(height)

    def tabComplete(self,
                    view: QtWidgets.QTableView,
                    model: QtCore.QSortFilterProxyModel):
        """ Complete commands by tab key
        Args:
            currentView (QTableView): view

        """

        selection = view.selectionModel()
        numRows = model.rowCount()

        if selection.hasSelection() is False:
            view.selectRow(0)
            index = model.index(0, 0)
        else:
            currentIndex = selection.currentIndex()
            currentRow = currentIndex.row()

            if currentRow == (numRows - 1):
                nextRow = 0
            else:
                nextRow = currentRow + 1

            view.clearSelection()
            view.selectRow(nextRow)

            index = model.index(nextRow, 0)
            selection.select(index, QtCore.QItemSelectionModel.Select)

        data = model.itemData(index)
        name = data[0]
        self.cmdsLE.setText(name)
        self.cmdsLE.setFocus()

    def shiftTabComplete(self,
                         view: QtWidgets.QTableView,
                         model: QtCore.QSortFilterProxyModel):
        """ shift tab completion

        Args:
            view (QTableView): view
            model (QSortFilterProxyModel): model

        Return:
            None

        """

        if self.cmdsLE.text() == "":
            return

        selection = view.selectionModel()
        numRows = model.rowCount()

        if selection.hasSelection() is False:
            lastIndex = numRows - 1
            view.selectRow(lastIndex)
            index = model.index(lastIndex, 0)
        else:
            currentIndex = selection.currentIndex()
            currentRow = currentIndex.row()

            if currentRow == 0:
                nextRow = numRows - 1
            else:
                nextRow = currentRow - 1

            view.clearSelection()
            view.selectRow(nextRow)

            index = model.index(nextRow, 0)
            selection.select(index, QtCore.QItemSelectionModel.Select)

        data = model.itemData(index)
        name = data[0]
        self.cmdsLE.setText(name)
        self.cmdsLE.setFocus()

    def execute(self):
        """ execute commands """

        if not self.cmdsLE.text():
            return

        index = None
        # Get command uuid from the selection
        if self.completeMode == "history":
            sel = self.historyView.selectionModel().selectedRows()
            index = sel[0]
            data = self.historyModel.itemData(index)
        else:
            sel = self.cmdsViewSelModel.selectedRows()
            index = sel[0]
            data = self.filteredModel.itemData(index)

        command_id = data[4]

        # get command string
        cmd = self.cmdDict[command_id]["command"]

        # Close gui first otherwise maya clashes(2017)
        self.close()

        sourceType = self.cmdDict[command_id]["sourceType"]
        if sourceType == "mel":
            mel.eval(cmd)
            mel.eval("""callLastCommand("%s")""" % cmd)
        else:
            try:
                func = getattr(self, "%s" % cmd)
                func()
                print("Rush command executed : %s" % cmd)

                # Add to repeatLast command so the comamnd can be repeatable
                # by G key
                cs = """python(\\"from rush import TmpCls; TmpCls.%s()\\")""" % cmd
                mel.eval("""callLastCommand("%s")""" % cs)
            except AttributeError:
                pass

        # Add command to history data
        self.history.append(command_id)
        self.history.save()


class Rush(OpenMaya.MPxCommand):
    """ Main plugin class """

    def doIt(self, *args):

        mainWindow = Gui(getMayaWindow())
        mainWindow.show()

        pos = QtGui.QCursor.pos()
        mainWindow.move(
            pos.x() - (mainWindow.width() / 2),
            pos.y() - (mainWindow.toolHeight / 2))

        mainWindow.raise_()
        mainWindow.activateWindow()

    @classmethod
    def isUndoable(cls):
        return False

    @staticmethod
    def cmdCreator():
        return Rush()


def syntaxCreator():
    """ Syntax creator

    Return:
        syntax (OpenMaya.MSyntax): return value

    """
    syntax = OpenMaya.MSyntax()
    syntax.addArg(OpenMaya.MSyntax.kString)
    return syntax


def maya_useNewAPI():
    """
    The presence of this function tells Maya that the plugin produces, and
    expects to be passed, objects created using the Maya Python API 2.0.
    """
    pass


def initializePlugin(mobject: OpenMaya.MObject):
    """ Initialize the script plug-in

    Args:
        mobject (OpenMaya.MObject):

    """
    mplugin = OpenMaya.MFnPlugin(
        mobject, "Michitaka Inoue", __version__, "Any")
    try:
        mplugin.registerCommand(PLUGIN_COMMAND, Rush.cmdCreator, syntaxCreator)
    except Exception:
        sys.stderr.write("Failed to register command: %s\n" % PLUGIN_COMMAND)
        raise


def uninitializePlugin(mobject: OpenMaya.MObject):
    """ Uninitialize the script plug-in

    Args:
        mobject (OpenMaya.MObject):

    """
    mplugin = OpenMaya.MFnPlugin(mobject)
    try:
        mplugin.deregisterCommand(PLUGIN_COMMAND)
    except Exception:
        sys.stderr.write("Failed to unregister command: %s\n" % PLUGIN_COMMAND)
        raise
