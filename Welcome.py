# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
"""
@Author：Thrones
Q  Q：1690069811
TelephoneNumber：18885672964
Email：yang18885672964@gmail.com
GitHub:
https://github.com/FightingThrones?tab=repositories


"""
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Welcome(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Ui_Welcome")
        MainWindow.resize(968, 651)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Start_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Start_pushButton.setGeometry(QtCore.QRect(140, 500, 171, 51))
        self.Start_pushButton.setObjectName("Start_pushButton")
        self.Close_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Close_pushButton.setGeometry(QtCore.QRect(390, 500, 181, 51))
        self.Close_pushButton.setObjectName("Close_pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 20, 400, 225))
        self.label.setObjectName("label")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(630, 310, 296, 236))
        self.calendarWidget.setObjectName("calendarWidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(290, 580, 321, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 260, 561, 231))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(510, 10, 431, 241))
        self.textEdit_2.setObjectName("textEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 968, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人脸识别系统"))

        self.Start_pushButton.setText(_translate("MainWindow", "开始人脸识别旅程"))
        self.Close_pushButton.setText(_translate("MainWindow", "退出系统"))
        self.label.setText(_translate("MainWindow", "Show"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:14pt; font-weight:600; color:#0000ff;\">    </span><span style=\" font-family:\'宋体\'; font-size:14pt; font-weight:600; color:#ffffff;\">人脸识别技术主要是首先通过图像采集设备采集到人脸图像，一般图像来源有静态图像以及动态视频帧，再把人脸图像用特定的特征提取算法来提取人脸特征，最终将待识别的人脸特征和已经得到的人脸特征模板来进行比对，通过计算两者之间的欧式距离、曼哈顿距离或者余弦值。根据相似程度进行校准，从而得到待识别目标人脸的身份信息。</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">软件相关信息</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">作者：杨 政 权</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Q  Q：1690069811</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">联系电话：18885672964</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">邮箱：yang18885672964@gmail.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">GitHub:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">https://github.com/FightingThrones?tab=repositories</span></p></body></html>"))

