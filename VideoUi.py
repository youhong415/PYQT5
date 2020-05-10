# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VideoUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(802, 520)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 600, 480))
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(660, 10, 121, 491))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.H_Slider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.H_Slider.setMaximum(255)
        self.H_Slider.setOrientation(QtCore.Qt.Vertical)
        self.H_Slider.setObjectName("H_Slider")
        self.gridLayout_2.addWidget(self.H_Slider, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.S_Slider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.S_Slider.setMaximum(255)
        self.S_Slider.setOrientation(QtCore.Qt.Vertical)
        self.S_Slider.setObjectName("S_Slider")
        self.gridLayout_2.addWidget(self.S_Slider, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.V_Slider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.V_Slider.setMaximum(255)
        self.V_Slider.setOrientation(QtCore.Qt.Vertical)
        self.V_Slider.setObjectName("V_Slider")
        self.gridLayout_2.addWidget(self.V_Slider, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.H_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.H_Label.setObjectName("H_Label")
        self.gridLayout_2.addWidget(self.H_Label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.S_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.S_Label.setObjectName("S_Label")
        self.gridLayout_2.addWidget(self.S_Label, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.V_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.V_Label.setObjectName("V_Label")
        self.gridLayout_2.addWidget(self.V_Label, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.H_Label.setText(_translate("Form", "0"))
        self.S_Label.setText(_translate("Form", "0"))
        self.V_Label.setText(_translate("Form", "0"))



