# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Testspeed.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TestSpeed(object):
    def setupUi(self, TestSpeed):
        TestSpeed.setObjectName("TestSpeed")
        TestSpeed.resize(400, 300)
        self.label = QtWidgets.QLabel(TestSpeed)
        self.label.setGeometry(QtCore.QRect(140, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(TestSpeed)
        self.scrollArea.setGeometry(QtCore.QRect(10, 30, 381, 261))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 259))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 381, 261))
        self.textEdit.setObjectName("textEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(TestSpeed)
        QtCore.QMetaObject.connectSlotsByName(TestSpeed)

    def retranslateUi(self, TestSpeed):
        _translate = QtCore.QCoreApplication.translate
        TestSpeed.setWindowTitle(_translate("TestSpeed", "Form"))
        self.label.setText(_translate("TestSpeed", "<html><head/><body><p><span style=\" color:#ff0202;\">Test Speed</span></p></body></html>"))
