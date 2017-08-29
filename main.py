from tkinter import *
import numpy as np
import tkinter.filedialog as fdialog
import tkinter.colorchooser as cchooser
import cv2

def main():
    img = cv2.imread(fdialog.askopenfilename(title="Choose your image file",filetypes = (("jpeg files","*.jpg"),("All files", "*"))),1)
    img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
    print (img.shape)
    cv2.imshow("Image",img)
    #rgbimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    color = getColor()
    img[:, :, 0] = color[0][2]
    img[:, :, 1] = color[0][1]
    #img[:, :, 2] = color[0][0]

    print(img[:,:,0], img[:,:,1], img[:,:,2])

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
