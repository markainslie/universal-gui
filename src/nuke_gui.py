"""Template Nuke GUI
"""

from Qt import QtWidgets, QtCore

import nukescripts

from base_gui import BaseWidget


def get_nuke_main_window():
    """Get the Nuke main window.
    Returns:
        PySide2.QtWidgets.QMainWindow: 'DockMainWindow' Nuke main window.
    """
    for w in QtWidgets.QApplication.topLevelWidgets():
        if w.inherits("QMainWindow") and w.metaObject().className() == "Foundry::UI::DockMainWindow":
            return w
    raise RuntimeError("Could not find DockMainWindow instance")


class NukeWidget(BaseWidget):
    """A template widget for building Nuke tools in a floating window"""

    def __init__(self, title="Nuke Widget", parent=None, *args, **kwargs):
        super(self.__class__, self).__init__(title=title, parent=parent)

    def _hello_world(self):
        """Hello world overloaded for Nuke"""
        print("Hello Nuke World!")


class NukePanelWidget(BaseWidget):
    """A template widget for building Nuke tools in a panel.

    TODO: Overload the _cancel method so that it does something else.
    """

    def __init__(self, title="Nuke Panel Widget", parent=None, *args, **kwargs):
        super(self.__class__, self).__init__(title=title, parent=parent)

        # build the gui
        self.build_gui()

    def _hello_world(self):
        """Hello world overloaded for a Nuke panel"""
        print("Hello Nuke Panel World!")


def nuke_widget_run(title_name="Nuke Window"):
    """Construct the Nuke widget.

    Args:
        title_name (str, optional): Window name. Defaults to "Nuke Window"
    """

    # delete window if it exists (so we don't get copies)
    main_win = get_nuke_main_window()
    object_name = title_name.strip().replace(" ", "_").lower()
    for widget in main_win.children():
        if widget.objectName() == object_name:
            widget.deleteLater()

    # contruct the gui
    nuke_app = NukeWidget(title=title_name, parent=main_win)
    nuke_app.setWindowFlags(QtCore.Qt.Window)
    nuke_app.resize(500, 800)
    nuke_app.build_gui()
    nuke_app.show()


def nuke_panel_run():
    """Construct the panel

    TODO: This is overly simple. Let's make this more sophisticated in the future.
    """

    panel = nukescripts.panels.registerWidgetAsPanel("NukePanelWidget", "Nuke Panel", "NukePanelWidget", create=True)
    pane = nuke.getPaneFor("Properties.1")
    panel.addToPane(pane)


if __name__ == "__main__":
    nuke_widget_run()
