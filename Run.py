"""
测试版本:
加上UI界面，摄像头采集的图像实时显示到UI界面中
而不是之前以弹窗形式显示
@author：Thrones
邮箱：yang18885672964@gmail.com
GitHub:  https://github.com/FightingThrones?tab=repositories
"""

import dlib
import cv2
import numpy as np
import threading
import _thread
from PyQt5.QtWidgets import*
from PyQt5 import QtCore
from Welcome import Ui_Welcome
from MainWindow import Ui_MainWindow
import qdarkstyle
from PyQt5.QtGui import *
import sys
class WelcomeUi(QMainWindow,Ui_Welcome):
    def __init__(self):
        super(WelcomeUi,self).__init__()
        self.setupUi(self)
        self.textEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Start_pushButton.setIcon(QIcon("./Resource/Cam.jpg"))
        self.Close_pushButton.setIcon(QIcon("./Resource/exit.ico"))
        self.Close_pushButton.clicked.connect(self.close)

class FaceUi(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(FaceUi,self).__init__()
        #定时器，用户控制显示视频的帧率
        self.timer_camera=QtCore.QTimer()

        #打开笔记本摄像头
        self.cap=cv2.VideoCapture()
        self.CAM_NUM=0

        self.setupUi(self)
        self.detector = dlib.get_frontal_face_detector()
        # dlib的68点模型，使用作者训练好的特征预测器
        self.predictor = dlib.shape_predictor("model/shape_predictor_68_face_landmarks.dat")

        self.slot_init()
        self.button_open_camera.setIcon(QIcon("./Resource/Cam.jpg"))
        self.button_Face_Detection.setIcon(QIcon("./Resource/Cam.jpg"))
        self.button_Face_Recognition.setIcon(QIcon("./Resource/Cam.jpg"))
        self.button_Speech_Recognition.setIcon(QIcon("./Resource/Video.jpg"))
        self.button_Chat.setIcon(QIcon("./Resource/Chat.jpg"))
        self.button_Close.setIcon(QIcon("./Resource/exit.ico"))



    #初始化各类事件响应函数
    def slot_init(self):
        self.button_open_camera.clicked.connect(self.button_open_camera_click)
        self.timer_camera.timeout.connect(self.show_camera)
        self.button_Face_Detection.clicked.connect(self.learning_face)
        self.button_Close.clicked.connect(self.close)

    def button_open_camera_click(self):
        # 如果定时器未启动
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            # 笔记本摄像头打开失败，提示用户检查
            if flag == False:
                msg = QMessageBox.warning(self, u"Warning", u"请检查笔记本摄像头是否完好!",
                                                    buttons=QMessageBox.Ok,
                                                    defaultButton=QMessageBox.Ok)
            else:
                self.timer_camera.start(30)
                self.button_open_camera.setText(u'关闭笔记本摄像头')
        else:
            self.timer_camera.stop()
            self.cap.release()
            self.label_show_camera.clear()
            self.button_open_camera.setText(u'打开笔记本摄像头')

    def show_camera(self):
        # 从视频流中读取数据
        flag, self.image = self.cap.read()
        # 将读到的帧的大小重新设置为640*480
        show = cv2.resize(self.image, (640, 480))
        # 将视频色彩转换为RGB颜色
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        # 将读取到的视频数据转换成QImage形式
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        # 在Label里显示QImage
        self.label_show_camera.setPixmap(QPixmap.fromImage(showImage))

        # 关闭系统处理函数
    def closeEvent(self, event):
        ok = QPushButton()
        cacel = QPushButton()

        msg = QMessageBox(QMessageBox.Warning, u"关闭", u"是否关闭！")

        msg.addButton(ok,QMessageBox.ActionRole)
        msg.addButton(cacel,QMessageBox.RejectRole)
        ok.setText(u'确定')
        cacel.setText(u'取消')
        if msg.exec_() == QMessageBox.RejectRole:
            event.ignore()
        else:
            if self.cap.isOpened():
                self.cap.release()
            if self.timer_camera.isActive():
                self.timer_camera.stop()
            event.accept()

    def learning_face(self):
        # 建cv2摄像头对象，这里使用电脑自带摄像头，如果接了外部摄像头，则自动切换到外部摄像头
        self.cap = cv2.VideoCapture(0)
        # 设置视频参数，propId设置的视频参数，value设置的参数值
        self.cap.set(3, 480)
        # 截图screenshoot的计数器
        self.cnt = 0

        # cap.isOpened（） 返回true/false 检查初始化是否成功
        while (self.cap.isOpened()):

            # cap.read()
            # 返回两个值：
            #    一个布尔值true/false，用来判断读取视频是否成功/是否到视频末尾
            #    图像对象，图像的三维矩阵
            flag, self.im_rd = self.cap.read()
            # 每帧数据延时5ms，延时为0读取的是静态帧
            self.k = cv2.waitKey(5)
            # 取灰度
            self.img_gray = cv2.cvtColor(self.im_rd, cv2.COLOR_RGB2GRAY)

            # 使用人脸检测器检测每一帧图像中的人脸。并返回人脸数rects
            faces = self.detector(self.img_gray, 0)

            # 待会要显示在屏幕上的字体
            font = cv2.FONT_HERSHEY_SIMPLEX

            # 如果检测到人脸
            if (len(faces) != 0):

                # enumerate方法同时返回数据对象的索引和数据，k为索引，d为faces中的对象
                for k, d in enumerate(faces):
                    # 眉毛直线拟合数据缓冲
                    line_brow_x = []
                    line_brow_y = []
                    # 用红色矩形框出人脸
                    cv2.rectangle(self.im_rd, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255))
                    # 计算人脸框边长
                    self.face_width = d.right() - d.left()

                    # 使用预测器得到68点数据的坐标
                    shape = self.predictor(self.im_rd, d)
                    # 圆圈显示每个特征点
                    for i in range(68):
                        cv2.circle(self.im_rd, (shape.part(i).x, shape.part(i).y), 2, (0, 255, 0), -1, 8)
                        # cv2.putText(im_rd, str(i), (shape.part(i).x, shape.part(i).y), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        #            (255, 255, 255))

                    # 分析任意n点的位置关系来作为表情识别的依据
                    mouth_width = (shape.part(54).x - shape.part(48).x) / self.face_width  # 嘴巴咧开程度
                    mouth_higth = (shape.part(66).y - shape.part(62).y) / self.face_width  # 嘴巴张开程度
                    # print("嘴巴宽度与识别框宽度之比：",mouth_width_arv)
                    # print("嘴巴高度与识别框高度之比：",mouth_higth_arv)

                    # 通过两个眉毛上的10个特征点，分析挑眉程度和皱眉程度
                    brow_sum = 0  # 高度之和
                    frown_sum = 0  # 两边眉毛距离之和
                    for j in range(17, 21):
                        brow_sum += (shape.part(j).y - d.top()) + (shape.part(j + 5).y - d.top())
                        frown_sum += shape.part(j + 5).x - shape.part(j).x
                        line_brow_x.append(shape.part(j).x)
                        line_brow_y.append(shape.part(j).y)

                    # self.brow_k, self.brow_d = self.fit_slr(line_brow_x, line_brow_y)  # 计算眉毛的倾斜程度
                    tempx = np.array(line_brow_x)
                    tempy = np.array(line_brow_y)
                    z1 = np.polyfit(tempx, tempy, 1)  # 拟合成一次直线
                    self.brow_k = -round(z1[0], 3)  # 拟合出曲线的斜率和实际眉毛的倾斜方向是相反的

                    brow_hight = (brow_sum / 10) / self.face_width  # 眉毛高度占比
                    brow_width = (frown_sum / 5) / self.face_width  # 眉毛距离占比
                    # print("眉毛高度与识别框高度之比：",round(brow_arv/self.face_width,3))
                    # print("眉毛间距与识别框高度之比：",round(frown_arv/self.face_width,3))

                    # 眼睛睁开程度
                    eye_sum = (shape.part(41).y - shape.part(37).y + shape.part(40).y - shape.part(38).y +
                               shape.part(47).y - shape.part(43).y + shape.part(46).y - shape.part(44).y)
                    eye_hight = (eye_sum / 4) / self.face_width
                    # print("眼睛睁开距离与识别框高度之比：",round(eye_open/self.face_width,3))

                    # 分情况讨论
                    # 张嘴，可能是开心或者惊讶
                    if round(mouth_higth >= 0.08):
                        if eye_hight >= 0.056:
                            cv2.putText(self.im_rd, "amazing", (d.left(), d.bottom() + 20), cv2.FONT_HERSHEY_SIMPLEX,
                                        0.8,
                                        (0, 0, 255), 2, 4)
                        else:
                            cv2.putText(self.im_rd, "happy", (d.left(), d.bottom() + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                                        (0, 0, 255), 2, 4)

                    # 没有张嘴，可能是正常和生气
                    else:
                        if self.brow_k <= 0.07:
                            cv2.putText(self.im_rd, "angry", (d.left(), d.bottom() + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                                        (0, 0, 255), 2, 4)
                        else:
                            cv2.putText(self.im_rd, "nature", (d.left(), d.bottom() + 20), cv2.FONT_HERSHEY_SIMPLEX,
                                        0.8,
                                        (0, 0, 255), 2, 4)

                # 标出人脸数
                cv2.putText(self.im_rd, "Faces: " + str(len(faces)), (20, 50), font, 1, (0, 0, 255), 1, cv2.LINE_AA)
            else:
                # 没有检测到人脸
                cv2.putText(self.im_rd, "No Face", (20, 50), font, 1, (0, 0, 255), 1, cv2.LINE_AA)

            # # 将读到的帧的大小重新设置为640*480
            show = cv2.resize(self.im_rd, (640, 480))
            # 将视频色彩转换为RGB颜色
            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
            # 将读取到的视频数据转换成QImage形式
            showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            # 在Label里显示QImage
            self.label_show_camera.setPixmap(QPixmap.fromImage(showImage))

        # 释放摄像头
        # self.cap.release()
        # 删除建立的窗口
        # cv2.destroyAllWindows()
        # t = threading.Thread(target=self.face_thread, name='Face_Thread')
        # t.start()
        # t.join()

    def OPEN(self):
        self.show()
        WelcomeUi.close()

if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    WelcomeUi=WelcomeUi()
    WelcomeUi.setWindowIcon(QIcon("./Resource/Icon.png"))
    movie=QMovie("./Resource/Cool.gif")
    WelcomeUi.label.setMovie(movie)
    movie.start()
    FaceUi=FaceUi()
    FaceUi.setWindowIcon(QIcon("./Resource/Icon.png"))
    WelcomeUi.show()
    WelcomeUi.Start_pushButton.clicked.connect(FaceUi.OPEN)
    sys.exit(app.exec_())