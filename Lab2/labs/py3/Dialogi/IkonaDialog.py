import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ikona(QDialog):
  def __init__(self, parent = None):
    super(Ikona, self).__init__(parent)
    layout = QVBoxLayout(self)
    layout.addStretch(1)
    # OK and Cancel buttons
    buttons = QDialogButtonBox(
        QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
        Qt.Horizontal, self)
    buttons.accepted.connect(self.accept)
    buttons.rejected.connect(self.reject)
    layout.addWidget(buttons)
