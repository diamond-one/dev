from PySide.QtCore import *
from PySide.QtGui import *
import sys
import datetime

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)





app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()