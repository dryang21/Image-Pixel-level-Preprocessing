import cv2
import os
import numpy as np

input_path=r'D:\10_COVID_Gary\data\reversal_all'
output_path=r'D:\10_COVID_Gary\data\CLAHE_all'




def reversal(input_path,output_path):
    input_files = os.listdir(input_path)
    for file in input_files:
        file_path=os.path.join(input_path,file)
        save_path=os.path.join(output_path,file)
        img=cv2.imread(file_path)
        reversal=255-img
        cv2.imwrite(save_path,reversal)

        del img
        del reversal


def CLAHE(input_path,output_path):
    input_files = os.listdir(input_path)
    for file in input_files:
        file_path = os.path.join(input_path, file)
        save_path = os.path.join(output_path, file)
        img = cv2.imread(file_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Contrast Limited Adaptive Histogram Equalization
        # cliplimit control the contrast of the result, the bigger limit, the higher contrast
        # cliplimit=2.0 is suitable for our CXR task
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        clahed_img=clahe.apply(gray)
        cv2.imwrite(save_path, clahed_img)
        del img
        del gray
        del clahe


def histogram_equalization(input_path,output_path):
    input_files = os.listdir(input_path)
    for file in input_files:
        file_path = os.path.join(input_path, file)
        save_path = os.path.join(output_path, file)
        img = cv2.imread(file_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        equ=cv2.equalizeHist(gray)
        cv2.imwrite(save_path, equ)
        del img
        del gray
        del que





if __name__ == "__main__":
    CLAHE(input_path,output_path)