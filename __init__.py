try:
    # Try import Qt.py from global site-package, if not import copy of Qt.py
    # in a current directory
    import Qt
except ImportError:
    from app import Qt

import app
reload(app)


def main():
    """ Show window and move it to cursor position """

    # Create and show window
    global miExec
    try:
        miExec.close()
    except:
        pass

    miExec = app.MainWindow()
    miExec.show()

    # Move the window to the cursor position.
    pos = Qt.QtGui.QCursor.pos()
    miExec.move(
        pos.x() - (miExec.width() / 2), pos.y() - (miExec.height() / 2))
    miExec.activateWindow()
    miExec.raise_()
