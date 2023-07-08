import pyttsx3
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from main_ui import Ui_MainWindow
from pydub import AudioSegment


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Text to Voice")
        self.Handel_Buttons()

    def Handel_Buttons(self):
        self.pushButton_2.clicked.connect(self.speak)
        self.pushButton.clicked.connect(self.save_speach)

    def speak(self):
        text_converter = pyttsx3.init()
        rate = text_converter.getProperty('rate')
        text_converter.setProperty('rate', rate - 50)

        text = self.textEdit.toPlainText()
        print(text)
        text_converter.say(text)
        text_converter.runAndWait()

    def save_speach(self):
        text_converter = pyttsx3.init()
        rate = text_converter.getProperty('rate')
        text_converter.setProperty('rate', rate - 50)

        text = self.textEdit.toPlainText()

        audio_file = "speech.wav"
        text_converter.save_to_file(text, audio_file)
        text_converter.runAndWait()

        self.statusBar().showMessage('File Saved...')
        self.timer = QTimer()
        self.timer.timeout.connect(self.clearMessage)
        self.timer.start(5000)  # Délai de 5 secondes (5000 millisecondes)

    def clearMessage(self):
        self.statusBar().clearMessage()
        self.timer.stop()

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
