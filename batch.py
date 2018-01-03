#coding=utf-8
import os
from hyperlpr_py3 import  pipline as  pp

import cv2

parent= "D:\MachineLearning\HyperLPR\dataset"

for filename in os.listdir(parent):
    path = os.path.join(parent,filename)
    print (path)
    if path.endswith(".jpg") or path.endswith(".png"):
        image =  cv2.imread(path)

        image,res  = pp.SimpleRecognizePlate(image)
        cv2.imshow("image",image)
        cv2.waitKey(0)