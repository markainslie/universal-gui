"""Template Houdini GUI
"""

from Qt import QtWidgets, QtCore

from base_gui import BaseWidget


class HoudiniWidget(BaseWidget):
    """A template widget for building Houdini tools."""

    def __init__(self, title="Houdini Widget", parent=None):
        super(HoudiniWidget, self).__init__(title=title, parent=parent)

    def _hello_world(self):
        """Hello world overloaded for Houdini"""
        print("Hello Houdini World!")


def houdini_run(title_name="Houdini Widget"):
    """Build the Houdini widget.

    Args:
        title_name (str, optional): Window name. Defaults to "Houdini Widget".
    """

    import hou

    # get the main houdini window
    main_win = hou.qt.mainWindow()

    # delete window if it exists (so we don't get copies)
    object_name = title_name.strip().replace(" ", "_").lower()
    for widget in main_win.children():
        if widget.objectName() == object_name:
            widget.deleteLater()

    # construct the gui
    houdini_app = HoudiniWidget(title=title_name, parent=main_win)
    houdini_app.setWindowFlags(QtCore.Qt.Window)
    houdini_app.resize(500, 800)
    houdini_app.build_gui()
    houdini_app.show()


if __name__ == "hou.session":
    houdini_run()
