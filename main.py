from hyperlpr_py3 import  pipline as  pp
import cv2

image = cv2.imread("D:/MachineLearning/HyperLPR/dataset/12.jpg")
image,res  = pp.SimpleRecognizePlate(image)
