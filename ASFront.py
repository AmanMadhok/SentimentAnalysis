from PyQt5 import QtCore, QtGui, QtWidgets
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
recognizer=sr.Recognizer()

class Ui_ThirdWindow(object):

    def clearAll(self):
        self.textEdit.clear()
        self.textEdit_2.clear()

    def detect_sentiment(self):
        with sr.Microphone() as source:
            print('Clearing background noise...')
            recognizer.adjust_for_ambient_noise(source,duration=1)
            print('Waiting for your message...')
            recordedaudio=recognizer.listen(source)
            print('Done recording..')

        try:
            print('Printing the message..')
            text=recognizer.recognize_google(recordedaudio,language='en-US')
            a='Your message:{}'.format(text)
            print(a)
            self.textEdit.setText(str(text))

        except Exception as ex:
            print(ex)

        Sentence=[str(text)]
        analyser=SentimentIntensityAnalyzer()
        for i in Sentence:
            v=analyser.polarity_scores(i)
        print(v)
        if v['pos'] > v['neg'] and  v['pos'] > v['neu']:
            answer="Positive"

        elif v['pos'] < v['neg'] and  v['neu'] < v['neg']:
            answer="Negative"

        else:
            answer="Neutral"

        print(answer)

        self.textEdit_2.setText(answer)
    
    def setupUi(self, ThirdWindow):
        ThirdWindow.setObjectName("ThirdWindow")
        ThirdWindow.resize(860, 490)
        ThirdWindow.setStyleSheet("background-color: rgb(26, 70, 69);")

        self.centralwidget = QtWidgets.QWidget(ThirdWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 90, 151, 31))
        self.pushButton.setStyleSheet("background-color: rgb(248,188,36); color: rgb(0,0,0)")
        self.pushButton.setObjectName("pushButton")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 320, 551, 81))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 140, 121, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n" "font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 341, 41))
        self.label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255)")
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 170, 551, 81))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 290, 201, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255); \n" "font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 430, 93, 28))
        self.pushButton_2.setStyleSheet("color: rgb(0,0,0);\n" "background-color: rgb(248,188,36);")
        self.pushButton_2.setObjectName("pushButton_2")

        ThirdWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(ThirdWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 26))
        self.menubar.setObjectName("menubar")
        ThirdWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ThirdWindow)

        self.statusbar.setObjectName("statusbar")
        ThirdWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ThirdWindow)
        QtCore.QMetaObject.connectSlotsByName(ThirdWindow)

    def retranslateUi(self, ThirdWindow):
        _translate = QtCore.QCoreApplication.translate
        ThirdWindow.setWindowTitle(_translate("ThirdWindow", "ThirdWindow"))
        self.pushButton.setText(_translate("ThirdWindow", "Check Sentiment"))
        self.label_2.setText(_translate("ThirdWindow", "Your Sentence:"))
        self.label.setText(_translate("ThirdWindow", "Audio Sentiment Analysis"))
        self.label_3.setText(_translate("ThirdWindow", "Sentence overall rated as:"))
        self.pushButton_2.setText(_translate("ThirdWindow", "Clear"))
        self.pushButton.clicked.connect(self.detect_sentiment)
        self.pushButton_2.clicked.connect(self.clearAll)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ThirdWindow = QtWidgets.QMainWindow()
    ui = Ui_ThirdWindow()
    ui.setupUi(ThirdWindow)
    ThirdWindow.show()
    sys.exit(app.exec_())
