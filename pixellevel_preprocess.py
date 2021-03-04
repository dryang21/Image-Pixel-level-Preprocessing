import cv2
import os
import numpy as np

"""
the information about PIL and Opencv:
cv2 open file get a numpy array with shape(H,W,C)
when we need to do pytorch based transform, we need to do transpose(2,0,1)
beceuse transforms need input to be a PIL image or a tensor with shape (C,H,W)

For PIL:
with open file, we get a PILimage format file instead of an array 
when we do np.asarray(), we could get the array of the PIL image of (H,W,C)
if we want to transforms this array and use it as an tensor input for transforms, we also need to do transpose(2,0,1)
however,if we directly input PILimage into transforms ,we do not need to do transpose,because the transforms will do this automaticly
"""






input_path=r'D:\10_COVID_Gary\NI\original'
output_path=r'D:\10_COVID_Gary\NI\processed'




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