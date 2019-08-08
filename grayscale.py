import matplotlib.pyplot as plt
import cv2
import numpy as np
import os




def main():
    gray_dia_train     = "/home/zeski/Documents/PythonLessons/MachineLearning/Projects/DiabeticRetinopathy/ProjectData/Binary/Grayscale/train/Diabetic_Retinopathy"
    gray_non_dia_train = "/home/zeski/Documents/PythonLessons/MachineLearning/Projects/DiabeticRetinopathy/ProjectData/Binary/Grayscale/train/No_Diabetic_Retinopathy"

    gray_dia_test      = "/home/zeski/Documents/PythonLessons/MachineLearning/Projects/DiabeticRetinopathy/ProjectData/Binary/Grayscale/test/Diabetic_Retinopathy"
    gray_non_dia_test  = "/home/zeski/Documents/PythonLessons/MachineLearning/Projects/DiabeticRetinopathy/ProjectData/Binary/Grayscale/test/No_Diabetic_Retinopathy"


    non_gray_dia_train         = "/home/zeski/Documents/PythonLessons/MachineLearning/Projects/DiabeticRetinopathy/ProjectData/Archive/Archive/model_train/Diabetic_Retinopathy"
    non_gray_non_dia_train     = "/home/zeski/Documents/PythonLessons/MachineLearning/Projects/DiabeticRetinopathy/ProjectData/Archive/Archive/model_train/No_Diabetic_Retinopathy"

    non_gray_dia_test          ="/home/zeski/Documents/PythonLessons/MachineLearning/Projects/DiabeticRetinopathy/ProjectData/Archive/Archive/model_test/Diabetic_Retinopathy"
    non_gray_non_dia_test      = "/home/zeski/Documents/PythonLessons/MachineLearning/Projects/DiabeticRetinopathy/ProjectData/Archive/Archive/model_test/No_Diabetic_Retinopathy"


    #Train
    print("Starting Color Transformation and Moving.")

    to_gray(gray_dia_train, non_gray_dia_train)
    print("Completed Grayscale Dia Train")
    to_gray(gray_non_dia_train, non_gray_non_dia_train)
    print("Completed Grayscale Non Dia Train")
    #Test


    to_gray(gray_dia_test, non_gray_dia_test)
    print("Completed Grayscale Dia Test")
    to_gray(gray_non_dia_test, non_gray_non_dia_test)
    print("Completed Grayscale Non Dia Test")


def to_gray(gray_dest, base_dir):

    import cv2
    import matplotlib.pyplot as plt

    os.chdir(base_dir)
    input_shape = (256,256,3)
    for i in os.listdir():

        os.chdir(base_dir)
        img = cv2.imread(i)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, input_shape[:2])
        img =  cv2.addWeighted(img, 4, cv2.GaussianBlur(img, (0,0), 256/10), -4, 128)
        os.chdir(gray_dest)

        plt.imshow(img, cmap = "gray")
        plt.savefig(i)
        #plt.show()

def color_gauss(gauss_dest,  base_dir, sigmaX = 10):
    import cv2
    import matplotlib.pyplot as plt
    os.chdir(base_dir)

    input_shape = (256,256,3)
    for i in os.listdir()
        os.chdir(base_dir)
        image = cv2.imread(i)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, input_shape[:2])
        image=cv2.addWeighted( image,4, cv2.GaussianBlur( image , (0,0) , sigmaX) ,-4 ,128)
        os.chdir(gauss_dest)

        plt.imshow(image)
        plt.savefig(i)

main()
