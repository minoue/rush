try:
    import Qt
except ImportError:
    from . import Qt


class CustomQLineEdit(Qt.QtWidgets.QLineEdit):
    """ Custom QLineEdit with custom events and signals"""

    escPressed = Qt.QtCore.Signal(str)
    downPressed = Qt.QtCore.Signal(str)

    def __init__(self, parent=None):
        super(CustomQLineEdit, self).__init__(parent)
        self.setFocusPolicy(Qt.QtCore.Qt.StrongFocus)

    def focusOutEvent(self, event):
        # emit signal to close the window when it gets focus out
        self.escPressed.emit('esc')

    def keyPressEvent(self, event):
        if event.key() == Qt.QtCore.Qt.Key_Escape:
            self.escPressed.emit('esc')

        elif event.key() == Qt.QtCore.Qt.Key_Down:
            self.downPressed.emit('down')
        else:
            super(CustomQLineEdit, self).keyPressEvent(event)
