"""Template dockable Maya GUI
"""

from Qt import QtCore, QtWidgets

import maya.cmds as cmds
from maya import OpenMayaUI
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

from base_gui import BaseWidget


def get_maya_win():
    """Get the main Maya QMainWindow"""
    # imoport the right shiboken
    if cmds.about(v=True) == "2025":
        from shiboken6 import wrapInstance
    else:
        from shiboken2 import wrapInstance

    # return the main window
    win_ptr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(int(win_ptr), QtWidgets.QMainWindow)


class MayaWidget(MayaQWidgetDockableMixin, BaseWidget):
    """A template widget for building dockable Maya tools."""

    def __init__(self, title="Dockable Maya Widget", parent=None):
        super(MayaWidget, self).__init__(title=title, parent=parent)

    def _hello_world(self):
        """Hello world overloaded for Maya"""
        print("Hello Dockable Maya World!")


def maya_widget_run(title_name="Dockable Maya Widget", dockable=True):
    """Construct the Maya widget. It supports both dockable and standard window behaviour.
    It's a little hacky because using the dockable=False boolean the show method doesn't seem to work.

    Args:
        title_name (str, optional): Windows name. Defaults to "Dockable Maya Widget".
        dockable (bool, optional): Makes the widget dockable. Defaults to True.
    """

    # delete window if it exists (so we don't get copies)
    window_name = title_name.strip().replace(" ", "_").lower()
    if cmds.window(window_name, ex=True):
        cmds.deleteUI(window_name)

    # delete the old workspace if it exists so it remains unique
    workspace_name = "{}WorkspaceControl".format(window_name)
    if cmds.workspaceControl(workspace_name, q=True, exists=True):
        cmds.workspaceControl(workspace_name, e=True, close=True)
        cmds.deleteUI(workspace_name, control=True)

    # now we can construct the gui
    maya_widget = MayaWidget(title=title_name)
    maya_widget.build_gui()

    # we have to do it this was because dockable=False doesn't seem to work as intended
    if dockable:
        maya_widget.show(dockable=True)
    else:
        maya_widget.show()


if __name__ == "__main__":
    maya_widget_run(title_name="Dockable Maya Widget", dockable=True)
