import os
import platform
import subprocess

from maya import cmds
from maya import OpenMayaUI

MAYA_VER = int(cmds.about(v=True))

if MAYA_VER > 2024:
    from PySide6 import QtGui, QtWidgets, QtCore
    import shiboken6 as shiboken
else:
    from PySide2 import QtGui, QtWidgets, QtCore
    import shiboken2 as shiboken

import rush

from importlib import reload
reload(rush)


def getMayaWindow():
    """ Get main window pointer """

    ptr = OpenMayaUI.MQtUtil.mainWindow()
    return shiboken.wrapInstance(int(ptr), QtWidgets.QMainWindow)


commandDict = {}


def reloadRush():
    try:
        cmds.unloadPlugin("Rush.py")
        cmds.loadPlugin("Rush.py")
    except Exception:
        print("Failed to reload plugin")


commandDict['reloadRush'] = "sphere.png"


def openRushModules():
    a = rush.MODULES

    w = ModuleList(a, getMayaWindow())
    w.show()


commandDict['openRushModules'] = "sphere.png"


class ModuleList(QtWidgets.QWidget):
    def __init__(self, modules, parent=None):
        super(ModuleList, self).__init__(parent)

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("RushModules")
        self.setWindowFlags(QtCore.Qt.Window)
        self.resize(600, 300)

        listWidget = QtWidgets.QListWidget()
        for m in modules:
            listWidget.addItem(m)
        listWidget.itemDoubleClicked.connect(self.open)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(listWidget)

        self.setLayout(layout)

    def open(self, *args):
        item = args[0]
        path = item.text()

        if platform.system() == 'Darwin':       # macOS
            subprocess.call(('open', path))
        elif platform.system() == 'Windows':    # Windows
            os.startfile(path)
        else:                                   # linux variants
            subprocess.call(('xdg-open', path))
