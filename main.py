from tkinter import *
import numpy as np
import tkinter.filedialog as fdialog
import tkinter.colorchooser as cchooser
import cv2

def main():
    # Load image in grayscale type
    img = cv2.imread(fdialog.askopenfilename(title="Choose your image file",filetypes = (("jpeg files","*.jpg"),("All files", "*"))),0)
    img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) #resize
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) #chagne grayscale to bgr (rgb order in opencv)
    #user pick color
    color = getColor()

    #adjust color in each color channel
    img[:, :, 0] = np.multiply(img[:,:,0],color[0][2]/255)
    img[:, :, 1] = np.multiply(img[:,:,1],color[0][1]/255)
    img[:, :, 2] = np.multiply(img[:,:,2],color[0][0]/255)

    print("b ",img[:, :, 0])
    print("g ",img[:, :, 1])
    print("r ",img[:, :, 2])

    # for w in range(img.shape[1]):
    #     for h in range(img.shape[0]):
    #         if img[h,w,0] > 200:
    #             img[h,w,0] = color[0][2]
    #
    #         if img[h,w,1] > 200:
    #             img[h,w,1] = color[0][1]
    #
    #         if img[h,w,2] > 200:
    #             img[h,w,2] = color[0][0]

    bgr = cv2.split(img)
    # print(bgr)
    cv2.imwrite("b.jpg", bgr[0])
    cv2.imwrite("g.jpg", bgr[1])
    cv2.imwrite("r.jpg", bgr[2])
    showImg(img)

def showImg(img):
    cv2.imshow("Result", img)
    cv2.waitKey(0)

def getColor():
    color = cchooser.askcolor()
    print (color)
    return color

if __name__ == "__main__":
    main()
