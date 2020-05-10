# -*- coding: utf-8 -*-
"""
Created on Sat May  9 08:35:25 2020

@author: bbjac
"""


import sys
import os
import time
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QListView, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import pyqtSlot

from MainUi import Ui_MainWindow


path = os.getcwd()




class Main_Ui(QMainWindow, Ui_MainWindow):
    
    FILE_PATH = ''
    
    
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        
        # 建立ui介面
        self.setupUi(self)
        
        # 觸發Event
        self.Src_Slt_Btn.clicked.connect(self.Src_Slt_Btn_Event)
        self.Save_Btn.clicked.connect(self.Save_Btn_Event)
    
    
    
    
    def Set_File_Path(self,file_path=''):self.FILE_PATH = file_path
    def Get_File_Path(self):return self.FILE_PATH
    
    
    # 來源目錄的按鈕事件觸發的函式
    def Src_Slt_Btn_Event(self):
        file_path,filters = QFileDialog.getOpenFileName(self,"choose directory",path)
        self.Set_File_Path(file_path)
        with open(file_path,'r',encoding='utf-8') as fd:
            self.textEdit.setText(fd.read())
            self.Src_Path_Txt.setText(file_path)

    # 儲存檔案
    def Save_Btn_Event(self):
        
        fd = open(self.Get_File_Path(),'w',encoding='utf-8')
        try:
            fd.write(str(self.textEdit.toPlainText()))
        except Exception  as e:
            self.Save_Status.setText(str(e))
        else:
            self.Save_Status.setText('Save Done')
        finally:
            fd.close()
if __name__ == "__main__":
    
    # 第一行必備，系統呼叫
    app = QApplication(sys.argv)

    # 指定 Mark Class 會先執行__init__
    window = Main_Ui()

    # 將GUI介面顯示出來
    window.show()

    # 關閉系統
    sys.exit(app.exec_())
    
    