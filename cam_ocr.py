import sys
from os import path

import cv2
import numpy as np

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

import pytesseract
from PIL import Image
from pytesseract import image_to_string
from gtts import gTTS
import os

#pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your path
pytesseract.pytesseract.tesseract_cmd = r"M:\Tesseract\tesseract.exe"

#tessdata_dir_config = r'--tessdata-dir "<replace_with_your_tessdata_dir_path>"'
tessdata_dir_config = r'--tessdata-dir "M:\Tesseract\tessdata"'



class RecordVideo(QtCore.QObject):
    image_data = QtCore.pyqtSignal(np.ndarray)

    def __init__(self, camera_port=0, parent=None):
        super().__init__(parent)
        self.camera = cv2.VideoCapture(camera_port)

        self.timer = QtCore.QBasicTimer()

    def start_recording(self):
        self.timer.start(0, self)

    
    def timerEvent(self, event):
        if (event.timerId() != self.timer.timerId()):
            return

        read, data = self.camera.read()
        if read:
            self.image_data.emit(data)
    def framesave(self):
        
        #sample training data
        db_java=["JAVA", "PROGRAMMING"]
        db_daa=["Data Structures","Tree","Space Complexity"]

        read, data = self.camera.read()
        if read:
            img=Image.fromarray(data)
            img.load()
            
            text=pytesseract.image_to_string(img, config=tessdata_dir_config)
            print ('Text_Found: ',len(text),"\n",text)
            if len(text)>0:
                tts = gTTS(text=text, lang='en')
                tts.save("pcvoice.mp3")
                os.system("start pcvoice.mp3")

            #sorting data
            db=[]
            t = text.split("\t")
            for x in t:
                db.append(x)
            
            for y in db:
                if y in db_java:
                    text_file = open('saved scans/java/x.txt','w')
                    text_file.write(text)
                    text_file.close()
                    cv2.imwrite('saved notes/java/x.jpg',data)
                elif y in db_daa:
                    text_file = open('saved scans/daa/x.txt','w')
                    text_file.write(text)
                    text_file.close()
                    cv2.imwrite('saved notes/daa/x.jpg',data)
                else:
                    text_file = open('saved scans/random/x.txt','w')
                    text_file.write(text)
                    text_file.close()
                    cv2.imwrite('saved notes/random/x.jpg',data)


class FaceDetectionWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image = QtGui.QImage()
        self._red = (0, 0, 255)
        self._width = 2
        self._min_size = (30, 30)


    def image_data_slot(self, image_data):
        self.image = self.get_qimage(image_data)
        if self.image.size() != self.size():
            self.setFixedSize(self.image.size())

        self.update()
    
            
    def get_qimage(self, image: np.ndarray):
        height, width, colors = image.shape
        bytesPerLine = 3 * width
        QImage = QtGui.QImage

        image = QImage(image.data,
                       width,
                       height,
                       bytesPerLine,
                       QImage.Format_RGB888)

        image = image.rgbSwapped()
        return image

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QtGui.QImage()

from PyQt5.QtGui import QPalette, QColor

class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("AENTO")
        
        self.face_detection_widget = FaceDetectionWidget()

        # TODO: set video port
        self.record_video = RecordVideo()

        image_data_slot = self.face_detection_widget.image_data_slot
        self.record_video.image_data.connect(image_data_slot)

        #layout designing
        layout = QtWidgets.QVBoxLayout()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('red'))
        self.setPalette(palette)


        layout.addWidget(self.face_detection_widget)
        self.run_button = QtWidgets.QPushButton('Start')
        layout.addWidget(self.run_button)

        self.run_button.clicked.connect(self.record_video.start_recording)

        self.screenshot = QtWidgets.QPushButton('Snap Shot')
        layout.addWidget(self.screenshot)

        self.screenshot.clicked.connect(self.record_video.framesave)
        self.setLayout(layout)
    
    def sizeHint(self):
        return QtCore.QSize(200, 200)
    def heightForWidth(self, width):
        return width
        



def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_widget = MainWidget()
    main_window.setCentralWidget(main_widget)
    main_window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
