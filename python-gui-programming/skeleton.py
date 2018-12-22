from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)






app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
