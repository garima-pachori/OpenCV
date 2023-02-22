import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread("saarthak.png")
kernel=np.ones((3,31),np.uint8)

imgGray=cv.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv.GaussianBlur(imgGray,(111,111),0)
imgCanny=cv.Canny(img,100,100)
imgCanny1=cv.Canny(img,100,500)
imgCanny2=cv.Canny(img,400,500)
imgDialation=cv.dilate(imgCanny,kernel,iterations=1) #iteration is the multiplier
imgEroded=cv.erode(imgDialation,kernel,iterations=1)
cv.imshow("Saarthak",img)
cv.imshow("Graythak",imgGray)
cv.imshow("Blurthak",imgBlur)
cv.imshow("Cannarthak",imgCanny)
cv.imshow("Cannarthak1",imgCanny1)
cv.imshow("Cannarthak2",imgCanny2)
cv.imshow("Diaarthak",imgDialation)
cv.imshow("Erothak",imgEroded)
cv.waitKey(0)