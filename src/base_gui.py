"""Template Base GUI
"""

import sys
import re

from Qt import QtWidgets, QtCore


class BaseWidget(QtWidgets.QWidget):
    """Template Base Widget"""

    def __init__(self, title="Base Widget", parent=None, *args, **kwargs):
        super(BaseWidget, self).__init__(parent=parent)

        # set the window title
        self.title = title
        self.setWindowTitle(self.title)

        # name the object so we can find it later
        object_name = self.title.strip().replace(" ", "_").lower()
        self.setObjectName(object_name)

        # set attributes and flags
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.setWindowFlags(QtCore.Qt.Window)

    def build_gui(self):
        """Build the gui"""

        # define the main layout
        hbox = QtWidgets.QHBoxLayout()
        self.setLayout(hbox)

        # vertical layout
        vbox = QtWidgets.QVBoxLayout()

        # make controls
        btn1 = QtWidgets.QPushButton('Print "Hello World!"')
        btn2 = QtWidgets.QPushButton("Input Dialog")
        btn3 = QtWidgets.QPushButton("Cancel")

        # set size policies
        btn1.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        btn2.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        btn3.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        # add to layouts
        hbox.addWidget(btn1)
        hbox.addLayout(vbox)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        # slots and signals
        btn1.clicked.connect(self._hello_world)
        btn2.clicked.connect(self._input_dialog)
        btn3.clicked.connect(self._close_me)

    def _hello_world(self):
        print("Hello World!")

    def _validate_input(self):
        """Constrain the input dialog text to camelCase"""

        # get the input from the dialog and constrain it
        input_string = self.input_dialog.textValue().replace(" ", "")
        if input_string:
            input_string = re.sub("[^a-zA-Z]+", "", input_string)
            input_string = input_string[0].lower() + input_string[1:]

        # write the constrained input back to the dialog
        self.input_dialog.setTextValue(input_string)

    def _input_dialog(self, title="title", message="message"):
        """Create an input dialog"""

        self.input_dialog = QtWidgets.QInputDialog()

        # set the title and label message
        self.input_dialog.setWindowTitle(title)
        self.input_dialog.setLabelText(message)

        # validate the input to camelCase
        self.input_dialog.textValueChanged.connect(self._validate_input)

        # run the input dialog
        self.input_dialog.exec_()

        # collect the input value
        self.input_value = self.input_dialog.textValue()
        print(self.input_value)

    def _close_me(self):
        self.close()


def run_standalone():
    """Build the GUI from command line"""
    app = QtWidgets.QApplication(sys.argv)
    win = BaseWidget()
    win.build_gui()
    win.resize(500, 300)
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run_standalone()
