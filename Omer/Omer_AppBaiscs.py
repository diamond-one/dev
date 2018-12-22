from libSB.libs.Qt import QtWidgets, QtCore, QtGui, QtCompat
import sys

class test(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(test, self).__init__(parent)


        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 10, 10)
        self.setMinimumHeight(700)
        self.setMaximumHeight(700)
        self.setWindowTitle('Maya Deadline Submitter')
        self.setMaximumWidth(300)
        self.setMinimumWidth(300)

        self.row_frames = QtWidgets.QWidget()

        self.lblFrames = QtWidgets.QLabel(self.row_frames)
        self.lblFrames.setGeometry(QtCore.QRect(0, 0, 46, 20))
        self.lblFrames.setText("Frames")

        self.comboFrames = QtWidgets.QComboBox(self.row_frames)
        self.comboFrames.setGeometry(QtCore.QRect(100, 0, 150, 30))
        self.comboFrames.addItems(["Interval", "Full", "matt"])
        self.comboFrames.setEditable(True)
        self.comboFrames.lineEdit().setMaxLength(45)
        self.comboFrames.lineEdit().setFixedWidth(100)

        self.layout.addWidget(self.row_frames)


        self.comboFrames.currentIndexChanged.connect(self.combo)

    def combo(self):
        print self.comboFrames.currentText()







def main():
    app = QtGui.QApplication(sys.argv)
    main = test()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()