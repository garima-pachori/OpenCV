import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread("saarthak.png")
#print(img.shape) #size of image
#(462 #height,623 #width,3 #number for bgr)
#imgResize=cv.resize(img,(1000,500))  #width then height
#cv.imshow("cutu",img)
#cv.imshow("Resaarthak",imgResize)
imgCropped=img[0:200,200:500]
cv.imshow("Croparthak",imgCropped)
#print(imgResize.shape)
cv.waitKey(0)

