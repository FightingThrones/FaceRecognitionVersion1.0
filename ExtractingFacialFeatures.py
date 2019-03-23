"""
# 目的：    从人脸图像文件中提取人脸特征存入 CSV文件中
# @Author: Thrones
# GitHub:  https://github.com/FightingThrones?tab=repositories
"""

# return_128d_features()          获取某张图像的 128D 特征
# write_into_csv()                获取某个路径下所有图像的特征，并写入 CSV
# compute_the_mean()              从 CSV　中读取　128D 特征，并计算特征均值

import cv2
import os
import dlib
from skimage import io
import csv
import numpy as np
import pandas as pd

# 要读取人脸图像文件的路径
path_photos_from_camera = "./FaceFolder/FaceDataSet/"
# 储存人脸特征 csv文件的路径
path_csv_from_photos = "./FaceFolder/FacialFeatures/"

# Dlib 正向人脸检测器
detector = dlib.get_frontal_face_detector()

# Dlib 人脸预测器
predictor = dlib.shape_predictor("./model/shape_predictor_5_face_landmarks.dat")

# Dlib 人脸识别模型
# Face recognition model, the object maps human faces into 128D vectors
facerec = dlib.face_recognition_model_v1("./model/dlib_face_recognition_resnet_model_v1.dat")


# 返回单张图像的 128D 特征
def return_128d_features(path_img):
    #读取上一个文件保存的图片
    img = io.imread(path_img)
    #进行灰度变换
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #取得检测到的人数
    faces = detector(img_gray, 1)

    print("检测到人脸的图像：", path_img, "\n")

    #检测到有人脸再去计算特征
    if len(faces) != 0:
        shape = predictor(img_gray, faces[0])
        face_descriptor = facerec.compute_face_descriptor(img_gray, shape)
    else:
        face_descriptor = 0
        print("no face")

    # print(face_descriptor)
    return face_descriptor

def write_into_csv(path_faces_personX, path_csv_from_photos):
    photos_list = os.listdir(path_faces_personX)
    with open(path_csv_from_photos, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if photos_list:
            for i in range(len(photos_list)):
                # 调用return_128d_features()得到128d特征
                print("正在读的人脸图像：", path_faces_personX + "/" + photos_list[i])
                features_128d = return_128d_features(path_faces_personX + "/" + photos_list[i])
                #  print(features_128d)
                # 遇到没有检测出人脸的图片跳过
                if features_128d == 0:
                    i += 1
                else:
                    writer.writerow(features_128d)
        else:
            print("Warning: Empty photos in "+path_faces_personX+'/')
            writer.writerow("")


# 读取某人所有的人脸图像的数据，写入 person_X.csv
faces = os.listdir(path_photos_from_camera)
for person in faces:
    print("##### " + person + " #####")
    print(path_csv_from_photos + person + ".csv")
    write_into_csv(path_photos_from_camera + person, path_csv_from_photos + person + ".csv")
print('\n')


# 从 CSV 中读取数据，计算 128D 特征的均值
def compute_the_mean(path_csv_from_photos):
    column_names = []

    # 128D 特征
    for feature_num in range(128):
        column_names.append("features_" + str(feature_num + 1))

    # 利用 pandas 读取 csv
    rd = pd.read_csv(path_csv_from_photos, names=column_names)

    if rd.size != 0:
        # 存放 128D 特征的均值
        feature_mean_list = []

        for feature_num in range(128):
            tmp_arr = rd["features_" + str(feature_num + 1)]
            tmp_arr = np.array(tmp_arr)
            # 计算某一个特征的均值
            tmp_mean = np.mean(tmp_arr)
            feature_mean_list.append(tmp_mean)
    else:
        feature_mean_list = []
    return feature_mean_list

# 存放所有特征均值的 CSV 的路径
path_csv_from_photos_feature_all = "./FaceFolder/FacialFeatures/FacialFeatures_all.csv"

# 存放人脸特征的 CSV 的路径
path_csv_from_photos = "FaceFolder/FacialFeatures/"

with open(path_csv_from_photos_feature_all, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    csv_rd = os.listdir(path_csv_from_photos)
    print("##### 得到的特征均值 / The generated average values of features stored in: #####")
    for i in range(len(csv_rd)):
        feature_mean_list = compute_the_mean(path_csv_from_photos + csv_rd[i])
        print(path_csv_from_photos + csv_rd[i])
        writer.writerow(feature_mean_list)
