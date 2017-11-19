import cv2
import numpy as np
import matplotlib.pyplot as plt
def auto_canny(image, sigma=0.3):
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged




color1Array = []
color2Array = []
i = 1
for i in range(1,4):
    oriImage = cv2.imread('base/'+str(i)+'.jpg',0)
    color1 = cv2.imread('color1/'+str(i)+'.jpg',0)
    color1 = cv2.resize(color1,(oriImage.shape[1],oriImage.shape[0]))
    color2 = cv2.imread('color2/'+str(i)+'.jpg',0)
    color2 = cv2.resize(color2,(oriImage.shape[1],oriImage.shape[0]))

    notColor1 = cv2.bitwise_and(color1,oriImage)
    notColor2 = cv2.bitwise_and(color2,oriImage)


    edgeOrigin = auto_canny(oriImage)
    edgeColor1 = auto_canny(notColor1)
    edgeColor2 = auto_canny(notColor2)


    #cv2.imshow('color1',edgeColor1)
    #cv2.imshow('color2',edgeColor2)

    result1 = edgeColor1-edgeOrigin
    result2 = edgeColor2-edgeOrigin

    color1Array.append(cv2.sumElems(result1)[0])
    color2Array.append(cv2.sumElems(result2)[0])

    print(color1Array)
    print(color2Array)

    #cv2.imshow('Ori',edgeOrigin)
    #cv2.imshow('From Color1', result1)
    #cv2.imshow('From Color2', result2)
x = [1,2,3]
#bw2 = cv2.threshold(im4,128,255, cv2.THRESH_BINARY)[1]
plt.plot(x,color1Array, 'rs',x,color2Array,'bs')
plt.show()

cv2.waitKey()


