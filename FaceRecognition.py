import dlib  # 人脸处理的库 Dlib
import numpy as np  # 数据处理的库 numpy

import pandas as pd  # 数据处理的库 Pandas
import threading

#********************计算两者图片的欧式距离**********************
class return_euclidean_distance_run_thread(threading.Thread):
    def return_euclidean_distance_run(self, feature_1, feature_2):
        feature_1 = np.array(feature_1)
        feature_2 = np.array(feature_2)
        dist = np.sqrt(np.sum(np.square(feature_1 - feature_2)))
        print("e_distance: ", dist)

        if dist > 0.4:
            print("diff")
            #FaceUi.textEdit.setText("diff\n")
            return "diff"
        else:
            print("same")
            #FaceUi.textEdit.setText("same\n")
            return "same"

#***************************计算欧式距离结束***********************

#***************************人脸识别核心代码***********************
class Face_Recognition(object):
    facerec = dlib.face_recognition_model_v1("./model/dlib_face_recognition_resnet_model_v1.dat")
    # 处理存放所有人脸特征的 CSV
    path_features_known_csv = "./FaceFolder/FacialFeatures/FacialFeatures_all.csv"
    csv_rd = pd.read_csv(path_features_known_csv, header=None)
    # 用来存放所有录入人脸特征的数组
    features_known_arr = []
    # Dlib 检测器和预测器
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('./model/shape_predictor_68_face_landmarks.dat')
    def ReadFaceData(self):
        # 读取已知人脸数据
        # known faces
        for i in range(self.csv_rd.shape[0]):
            features_someone_arr = []
            for j in range(0, len(self.csv_rd.ix[i, :])):
                features_someone_arr.append(self.csv_rd.ix[i, :][j])
            #    print(features_someone_arr)
            self.features_known_arr.append(features_someone_arr)
        print("Faces in Database：", len(self.features_known_arr))
#************************人脸识别核心代码结束**********************
