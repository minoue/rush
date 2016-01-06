from PySide import QtGui, QtCore


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
