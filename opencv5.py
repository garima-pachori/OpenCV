import cv2 as cv
import numpy as np

img=cv.imread("cards.png")

width,height = 350,190 #window size of output

#these are the points that are to be put up on the frame that we want
#the window and the pic must have straight lines between two points
pts1 = np.float32([[16,227],[388,67],[140,390],[514,229]])

#destination point where we want to get those points
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])

#func to do this
matrix=cv.getPerspectiveTransform(pts1,pts2)
imgOutput=cv.warpPerspective(img,matrix,(width,height))

cv.imshow("image",img)
cv.imshow("output",imgOutput)

cv.waitKey(0)