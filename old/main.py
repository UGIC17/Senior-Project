from tkinter import *
import tkinter
import PIL.Image as Image
import PIL.ImageTk as ImageTk
import numpy as np
import tkinter.filedialog as fdialog
import tkinter.colorchooser as cchooser
import cv2


updatePanel = None
resultPanel = None
path = ""
def main():
    global updatePanel, resultPanel

    # Load image in grayscale type

    if len(path) > 2:

        img = cv2.imread(path,0)
        img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) #resize
        oriImage = img
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) #chagne grayscale to bgr (rgb order in opencv)
        result = changeColor(img)
        result = result[:, :, ::-1]
        oriImage = Image.fromarray(oriImage)
        oriImage = ImageTk.PhotoImage(oriImage)

        result = Image.fromarray(result)
        result = ImageTk.PhotoImage(result)
        ## create result panel

        updatePanel.config(image=oriImage)
        resultPanel.config(image=result)
        updatePanel.image = oriImage
        resultPanel.image = result

    #showImg(img)

def getPath():
    global path
    path = fdialog.askopenfilename(title="Choose your image file",filetypes=(("jpeg files", "*.jpg"), ("All files", "*")))


def showImg(img):
    cv2.imshow("Result", img)
    cv2.waitKey(0)

def getColor():
    color = cchooser.askcolor()
    print (color)
    return color

def changeColor(img):
    # user pick color
    color = getColor()
    #adjust color in each color channel
    img[:, :, 0] = np.multiply(img[:,:,0],color[0][2]/255)
    img[:, :, 1] = np.multiply(img[:,:,1],color[0][1]/255)
    img[:, :, 2] = np.multiply(img[:,:,2],color[0][0]/255)
    writeImage(img)
    print("b ",img[:, :, 0])
    print("g ",img[:, :, 1])
    print("r ",img[:, :, 2])
    return img

def writeImage(img):
    bgr = cv2.split(img)
    # print(bgr)
    cv2.imwrite("res.jpg", img)
    cv2.imwrite("b.jpg", bgr[0])
    cv2.imwrite("g.jpg", bgr[1])
    cv2.imwrite("r.jpg", bgr[2])

#if __name__ == "__main__":
#    main()

window = Tk()
b = Button(window,text="Open File",command = getPath)
b.pack(side="top", padx="10", pady="10")
s = Button(window,text="Process",command = main)
s.pack(side="bottom", padx="10", pady="10")

bg = cv2.imread("background.jpg")
bg = Image.fromarray(bg)
bg = ImageTk.PhotoImage(bg)
updatePanel = tkinter.Label(window, image=bg)
updatePanel.image = bg
updatePanel.pack(side="left", fill="both", expand="yes", padx="10", pady="10")
resultPanel = tkinter.Label(window, image=bg)
resultPanel.image = bg
resultPanel.pack(side="right", fill="both", expand="yes", padx="10", pady="10")

window.mainloop()
