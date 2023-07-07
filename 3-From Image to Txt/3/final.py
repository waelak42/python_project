# Screen Shot app 
# pyuic5 main.ui -o main_ui.py
# pyinstaller --windowed -F votre_script.py

# EXtract Code From Image 

# download Tesseract from 
# https://osdn.net/projects/sfnet_tesseract-ocr-alt/downloads/tesseract-ocr-setup-3.02.02.exe/

import os
import pytesseract
from PIL import Image
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from main3 import Ui_MainWindow
from PyQt5 import QtWidgets

class Main(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Extract Code From Image")
        self.setFixedSize(808, 237)  # Set fixed width and height
        self.Handel_Buttons()
        self.text_edit.setReadOnly(True)
        
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.select_source_file)
        self.pushButton_2.clicked.connect(self.select_destination_file)
        self.pushButton_3.clicked.connect(self.extract_text)
        self.pushButton_4.clicked.connect(self.clear)

    def select_source_file(self):
        
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select Source Image', '', 'Images (*.png *.jpg *.jpeg);;All Files (*)', options=options)
        if file_name:
            self.lineEdit.setText(os.path.basename(file_name))
            self.source_file = file_name
            
    
    def select_destination_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save Text File', '', 'Text Files (*.txt);;All Files (*)', options=options)
        if file_name:
            self.lineEdit_2.setText(os.path.basename(file_name))
            self.destination_file = file_name
            
            
    def extract_text(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
        if hasattr(self, 'source_file') and hasattr(self, 'destination_file'):
            try:
                image = Image.open(self.source_file)
                extracted_text = pytesseract.image_to_string(image)
                with open(self.destination_file, 'w', encoding='utf-8') as file:
                    file.write(extracted_text)
                
                
                
                self.text_edit.setPlainText('Text extracted successfully and saved to the specified file.')
            except Exception as e:
                self.text_edit.setPlainText(f'Error: {str(e)}')
        else:
            self.text_edit.setPlainText('Please select both source image and destination text file.')

    def clear(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.text_edit.setPlainText('')

    
    
def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if '__main__' ==__name__:
    main()