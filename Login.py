# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 312)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(310, 40, 71, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.user_label.setFont(font)
        self.user_label.setMouseTracking(True)
        self.user_label.setObjectName("user_label")
        self.pwd_line = QtWidgets.QLineEdit(self.centralwidget)
        self.pwd_line.setGeometry(QtCore.QRect(380, 130, 200, 30))
        self.pwd_line.setObjectName("pwd_line")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(320, 200, 91, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.signin_button = QtWidgets.QPushButton(self.centralwidget)
        self.signin_button.setGeometry(QtCore.QRect(480, 200, 91, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.signin_button.setFont(font)
        self.signin_button.setObjectName("signin_button")
        self.Logo_label = QtWidgets.QLabel(self.centralwidget)
        self.Logo_label.setGeometry(QtCore.QRect(10, 40, 301, 203))
        self.Logo_label.setObjectName("Logo_label")
        self.user_line = QtWidgets.QLineEdit(self.centralwidget)
        self.user_line.setGeometry(QtCore.QRect(380, 40, 200, 30))
        self.user_line.setObjectName("user_line")
        self.pwd_label = QtWidgets.QLabel(self.centralwidget)
        self.pwd_label.setGeometry(QtCore.QRect(310, 130, 71, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.pwd_label.setFont(font)
        self.pwd_label.setObjectName("pwd_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 26))
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
        self.user_label.setText(_translate("MainWindow", "账  号："))
        self.login_button.setText(_translate("MainWindow", "登  录"))
        self.signin_button.setText(_translate("MainWindow", "注  册"))
        self.Logo_label.setText(_translate("MainWindow", "ShowLogo"))
        self.pwd_label.setText(_translate("MainWindow", "密  码："))

