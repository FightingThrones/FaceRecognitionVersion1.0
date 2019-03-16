# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Signin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignIn(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(444, 266)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signin_user_label = QtWidgets.QLabel(self.centralwidget)
        self.signin_user_label.setGeometry(QtCore.QRect(40, 30, 101, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.signin_user_label.setFont(font)
        self.signin_user_label.setObjectName("signin_user_label")
        self.signin_pwd_label = QtWidgets.QLabel(self.centralwidget)
        self.signin_pwd_label.setGeometry(QtCore.QRect(40, 80, 101, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.signin_pwd_label.setFont(font)
        self.signin_pwd_label.setObjectName("signin_pwd_label")
        self.signin_pwd2_label = QtWidgets.QLabel(self.centralwidget)
        self.signin_pwd2_label.setGeometry(QtCore.QRect(40, 130, 91, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.signin_pwd2_label.setFont(font)
        self.signin_pwd2_label.setObjectName("signin_pwd2_label")
        self.signin_user_line = QtWidgets.QLineEdit(self.centralwidget)
        self.signin_user_line.setGeometry(QtCore.QRect(150, 30, 250, 30))
        self.signin_user_line.setObjectName("signin_user_line")
        self.signin_pwd_line = QtWidgets.QLineEdit(self.centralwidget)
        self.signin_pwd_line.setGeometry(QtCore.QRect(150, 80, 250, 30))
        self.signin_pwd_line.setObjectName("signin_pwd_line")
        self.signin_pwd2_line = QtWidgets.QLineEdit(self.centralwidget)
        self.signin_pwd2_line.setGeometry(QtCore.QRect(150, 130, 250, 30))
        self.signin_pwd2_line.setObjectName("signin_pwd2_line")
        self.signin_button = QtWidgets.QPushButton(self.centralwidget)
        self.signin_button.setGeometry(QtCore.QRect(160, 180, 111, 28))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.signin_button.setFont(font)
        self.signin_button.setObjectName("signin_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 444, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.signin_user_label.setText(_translate("MainWindow", "用 户 名："))
        self.signin_pwd_label.setText(_translate("MainWindow", "密    码："))
        self.signin_pwd2_label.setText(_translate("MainWindow", "密    码："))
        self.signin_button.setText(_translate("MainWindow", "注  册"))

