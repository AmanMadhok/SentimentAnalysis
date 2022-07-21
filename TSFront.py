from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTextEdit
from textblob import TextBlob

class Ui_SecondWindow(object):

    def clearAll(self):
        self.textEdit.clear()
        self.textEdit_2.clear()

    def detect_sentiment(self):

        self.sentence=self.textEdit.toPlainText()

        pol=TextBlob(self.sentence).sentiment.polarity
        sub=TextBlob(self.sentence).sentiment.subjectivity

        if pol>0 and sub>0.3:
            self.answer="Positive"

        elif pol<0 and sub>0.3:
            self.answer="Negative"

        else:
            self.answer="Neutral"

        self.textEdit_2.setText(self.answer)

    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(860, 490)
        SecondWindow.setStyleSheet("background-color: rgb(26, 70, 69);")
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 321, 41))
        self.label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255)")
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(150, 120, 551, 81))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 90, 161, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n" "font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 230, 151, 31))
        self.pushButton.setStyleSheet("background-color: rgb(248,188,36); color: rgb(0,0,0)")
        self.pushButton.setObjectName("pushButton")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(150, 320, 551, 81))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 290, 201, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255); \n" "font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 430, 93, 28))
        self.pushButton_2.setStyleSheet("color: rgb(0,0,0);\n" "background-color: rgb(248,188,36);")
        self.pushButton_2.setObjectName("pushButton_2")

        SecondWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 26))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "SecondWindow"))
        self.label.setText(_translate("SecondWindow", "Text Sentiment Analysis"))
        self.label_2.setText(_translate("SecondWindow", "Enter your sentence:"))
        self.pushButton.setText(_translate("SecondWindow", "Check Sentiment"))
        self.label_3.setText(_translate("SecondWindow", "Sentence overall rated as:"))
        self.pushButton_2.setText(_translate("SecondWindow", "Clear"))
        self.pushButton.clicked.connect(self.detect_sentiment)
        self.pushButton_2.clicked.connect(self.clearAll)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
