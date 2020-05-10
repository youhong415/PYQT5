# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:26:47 2020

@author: bbjac
"""

from VideoUi import Ui_Form

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap

import numpy as np
import sys
import cv2


class Thread(QThread):
    
    changePixmap = pyqtSignal(QImage)
    Text = '123'
    
    @pyqtSlot(int)
    def setInt(self,value):
        #print(value)
        self.Text = str(value)
    
    
    def run(self):
        
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                cv2.putText(rgbImage, self.Text, (25,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 255), 1, cv2.LINE_AA)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)


class VideoUi(QMainWindow, Ui_Form):
    
    changeText = pyqtSignal(int)
    
    
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))
    
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_Form.__init__(self)
        # 建立ui介面
        self.setupUi(self)
        self.H_Slider.valueChanged.connect(self.H_Slide_Event)
        
    
    def H_Slide_Event(self):
        value = self.H_Slider.value()
        self.H_Label.setText(str(value))
        self.changeText.emit(value)
        

if __name__ == "__main__":
    
    # 第一行必備，系統呼叫
    app = QApplication(sys.argv)
    
    
    videoui = VideoUi()
    thread = Thread()
    
    # 建立 videoui --> thread 的qyptsignal及slot
    videoui.changeText.connect(thread.setInt)
    
    # 建立 thread --> videoui 的qyptsignal及slot
    thread.changePixmap.connect(videoui.setImage)
    thread.start()
    
    # 將GUI介面顯示出來
    videoui.show()

    # 關閉系統
    sys.exit(app.exec_())
    
    
    