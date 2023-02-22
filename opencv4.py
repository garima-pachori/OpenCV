import cv2 as cv
import numpy as np

#resizing and shapes specifies width and then height
#but the porder of posisioning for others is (height,width)

#making a box by using 512 pixels(black color by default)
#unit8 specifies 256 specifications of color will be there in BGR shades
img=np.zeros((512,512,3),np.uint8)
#512*512 is the specification of the image size to be displayed
print(img)

#for printing specific part out of rhe image
img[200:300,100:300]=255,0,0
#BGR=B=255,G=0,R=0 so blue color will be displayed wholly
#256 each BGR is given


cv.line(img,(0,0),(300,300),(0,255,0),3)
#(0,0) is the starting point, (300,300) is the ending point
#(0,255,0) is the color specification in BGR


cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
#when you dont know the specifications of it, and you want it on whole screen
#0 and 1 is the index here of the output of .shape
#3 is the thickness


cv.rectangle(img,(0,0),(250,350),(0,0,255),cv.FILLED)
#(0,0) and (250,350) specifies the diagonal of the box
#FILLED is used for filling the rectangle


cv.circle(img,(450,50),30,(255,255,0),5)
#(450,50) is the centre , 30 is the radius, (255,255,0) is RGB color
#5 is the thickness
cv.circle(img,(450,50),30,(255,255,0),cv.FILLED)
#thickness is not to be mentioned when we are filling it inside


cv.putText(img,"OPENCV",(300,200),cv.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)
#(300,200) is the starting point of the text
#1 is the font size
#BGR color format
#3 is the thickness

cv.imshow("image",img)

cv.waitKey(0)