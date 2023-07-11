##################################################
################ Convert Video to MP3 ##############
##################################################

import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys
import moviepy.editor as mp
from main_ui import Ui_Form

from PyQt5 import QtWidgets



class Main(QMainWindow,Ui_Form ):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Convert Video to Mp3")
        self.Handel_Buttons()
        self.source = ''
        self.destination = ''

    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.select_source_file)
        self.pushButton_2.clicked.connect(self.select_destination_file)
        self.pushButton_3.clicked.connect(self.convert)
        self.pushButton_4.clicked.connect(self.clear)

    def select_source_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, 'Select Source Image', '', 'Images (*.flv *.mp4 *.mpeg);;All Files (*)', options=options)
        if file_name:
            self.lineEdit.setText(os.path.basename(file_name))
            self.source = file_name

    def select_destination_file(self):
        options = QFileDialog.Options()
        file_name1, _ = QFileDialog.getSaveFileName(
            self, 'Save File mp3', '', 'Mp3 Files (*.mp3);;All Files (*)', options=options)
        if file_name1:
            self.lineEdit_2.setText(os.path.basename(file_name1))
            self.destination = file_name1

    def convert(self):
        self.label_3.setText("Converting...")
        QApplication.processEvents()  # Mettre à jour l'interface graphique

        # Démarrer la conversion dans un thread séparé
        self.thread = ConvertThread(self.source, self.destination)
        self.thread.conversionFinished.connect(self.on_conversion_finished)
        self.thread.start()

    def on_conversion_finished(self):
        self.label_3.setText("Done")

    def clear(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.label_3.setText('')

class ConvertThread(QThread):
    conversionFinished = pyqtSignal()

    def __init__(self, source, destination, parent=None):
        super(ConvertThread, self).__init__(parent)
        self.source = source
        self.destination = destination

    def run(self):
        clip = mp.VideoFileClip(self.source)
        clip.audio.write_audiofile(self.destination)
        self.conversionFinished.emit()

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
