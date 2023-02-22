import cv2 as cv
import numpy as np

def getContours(img):
    #saving all the shapes based on their contours in an array
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

    #traversing contour array to make all shapes visible differntly
    for cnt in contours:
        #drawing contours as blue line over the original drawing

        area=cv.contourArea(cnt)
        print(area)
        #specifies the area so as to detect image otherwise bg noise and images will also
        #be thought up as an image only




        if area>500:
            cv.drawContours(imgContour,cnt,-1,(255.0,0),3)
            #cnt is the variable
            # -1 is the index as we want to print all the contours
            # 255 is blue of bgr
            # 3 is the thickness

            peri=cv.arcLength(cnt,True)
            #print(peri)
            approx=cv.approxPolyDP(cnt,0.02*peri,True)
            print(approx)


path = "shapes.png"
img = cv.imread(path)
imgContour = img.copy() #copy of original image
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv.Canny(imgBlur,50,50)
getContours(imgCanny)

cv.imshow("ImageCanny",imgCanny)
cv.imshow("ImageContour",imgContour)

cv.waitKey(0)