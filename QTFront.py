from PyQt5 import QtCore, QtGui, QtWidgets
from TSFront import Ui_SecondWindow
from ASFront import Ui_ThirdWindow

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 490)
        MainWindow.setStyleSheet("background-color: rgb(26, 70, 69);")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 380, 151, 28))
        self.pushButton.setStyleSheet("background-color: rgb(248,188,36); color: rgb(0,0,0);")
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 380, 151, 28))
        self.pushButton_2.setStyleSheet("background-color: rgb(248,188,36); color: rgb(0,0,0);")
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 380, 151, 28))
        self.pushButton_3.setStyleSheet("background-color: rgb(248,188,36); color: rgb(0,0,0);")
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 30, 341, 51))
        self.label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\"; color: rgb(255, 255, 255)")
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 110, 361, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 220, 151, 131))
        self.label_4.setStyleSheet("background-image: url(:/newPrefix2/Mic (1).png);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix2/Mic (1).png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 220, 151, 131))
        self.label_3.setStyleSheet("background-image: url(:/newPrefix1/Text.png);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix1/Text.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(640, 220, 151, 131))
        self.label_5.setStyleSheet("background-image: url(:/newPrefix3/Webcam.png);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix3/Webcam.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Text"))
        self.pushButton_2.setText(_translate("MainWindow", "Audio"))
        self.pushButton_3.setText(_translate("MainWindow", "Video"))
        self.label.setText(_translate("MainWindow", "SENTIMENT ANALYSIS"))
        self.label_2.setText(_translate("MainWindow", "Choose any one of the following to perform sentiment analysis"))
        self.pushButton.clicked.connect(self.openText)
        self.pushButton_2.clicked.connect(self.openAudio)
        self.pushButton_3.clicked.connect(self.openVideo)

    def openText(self):
        self.window=QtWidgets.QMainWindow()
        self.ui= Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAudio(self):
        self.window2=QtWidgets.QMainWindow()
        self.ui2= Ui_ThirdWindow()
        self.ui2.setupUi(self.window2)
        self.window2.show()

    def openVideo(self):
        exec(open('detect_emotion_video.py').read(), globals())

import audiophotonew
import textphotonew
import videophotonew

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
