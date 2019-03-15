# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1414, 806)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_open_camera = QtWidgets.QPushButton(self.centralwidget)
        self.button_open_camera.setGeometry(QtCore.QRect(40, 30, 181, 51))
        self.button_open_camera.setObjectName("button_open_camera")
        self.button_Face_Detection = QtWidgets.QPushButton(self.centralwidget)
        self.button_Face_Detection.setGeometry(QtCore.QRect(40, 120, 181, 51))
        self.button_Face_Detection.setObjectName("button_Face_Detection")
        self.button_Face_Recognition = QtWidgets.QPushButton(self.centralwidget)
        self.button_Face_Recognition.setGeometry(QtCore.QRect(40, 200, 181, 51))
        self.button_Face_Recognition.setObjectName("button_Face_Recognition")
        self.button_Close = QtWidgets.QPushButton(self.centralwidget)
        self.button_Close.setGeometry(QtCore.QRect(590, 630, 181, 41))
        self.button_Close.setObjectName("button_Close")
        self.label_show_camera = QtWidgets.QLabel(self.centralwidget)
        self.label_show_camera.setGeometry(QtCore.QRect(340, 80, 640, 480))
        self.label_show_camera.setObjectName("label_show_camera")
        self.label_ShowPic = QtWidgets.QLabel(self.centralwidget)
        self.label_ShowPic.setGeometry(QtCore.QRect(1070, 10, 231, 231))
        self.label_ShowPic.setObjectName("label_ShowPic")
        self.button_Speech_Recognition = QtWidgets.QPushButton(self.centralwidget)
        self.button_Speech_Recognition.setGeometry(QtCore.QRect(40, 290, 181, 51))
        self.button_Speech_Recognition.setObjectName("button_Speech_Recognition")
        self.button_Chat = QtWidgets.QPushButton(self.centralwidget)
        self.button_Chat.setGeometry(QtCore.QRect(40, 390, 181, 51))
        self.button_Chat.setObjectName("button_Chat")
        self.textEdit_Information = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Information.setGeometry(QtCore.QRect(1040, 280, 291, 221))
        self.textEdit_Information.setObjectName("textEdit_Information")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(1040, 520, 296, 236))
        self.calendarWidget.setObjectName("calendarWidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(386, 10, 501, 71))
        font = QtGui.QFont()
        font.setFamily("叶根友毛笔行书2.0版")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.toolButton.setFont(font)
        self.toolButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.toolButton.setObjectName("toolButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(480, 710, 371, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1414, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionNew)
        self.menu.addAction(self.actionClose)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_open_camera.setText(_translate("MainWindow", "打开笔记本摄像头"))
        self.button_Face_Detection.setText(_translate("MainWindow", "人脸检测和表情识别"))
        self.button_Face_Recognition.setText(_translate("MainWindow", "进行人脸识别"))
        self.button_Close.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#000000;\">您真的想要退出系统吗？</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.button_Close.setText(_translate("MainWindow", "退出系统"))
        self.label_show_camera.setText(_translate("MainWindow", "label_show_camera"))
        self.label_ShowPic.setText(_translate("MainWindow", "ShowPic"))
        self.button_Speech_Recognition.setText(_translate("MainWindow", "进行语言识别"))
        self.button_Chat.setText(_translate("MainWindow", "开启聊天模式"))
        self.textEdit_Information.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">目标人物信息展示</span></p></body></html>"))
        self.toolButton.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">这是人脸识别的主界面</span></p></body></html>"))
        self.toolButton.setText(_translate("MainWindow", "人脸识别系统"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionClose.setText(_translate("MainWindow", "Close"))


