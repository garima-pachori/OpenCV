import cv2 as cv
import numpy as np


def empty(a):
    pass


def stackImages(scale, imgArray):
  rows = len(imgArray)
  cols = len(imgArray[0])
  rowsAvailable = isinstance(imgArray[0], list)
  width = imgArray[0][0].shape[1]
  height = imgArray[0][0].shape[0]
  if rowsAvailable:
    for x in range(0, rows):
      for y in range(0, cols):
        if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
          imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
        else:
          imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale,
                                     scale)
        if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv.cvtColor(imgArray[x][y], cv.COLOR_GRAY2BGR)
    imageBlank = np.zeros((height, width, 3), np.uint8)
    hor = [imageBlank] * rows
    hor_con = [imageBlank] * rows
    for x in range(0, rows):
      hor[x] = np.hstack(imgArray[x])
    ver = np.vstack(hor)
  else:
    for x in range(0, rows):
      if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
        imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
      else:
        imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
      if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
    hor = np.hstack(imgArray)
    ver = hor
  return ver

path="cards.png"
img=cv.imread(path)
cv.namedWindow("TrackBars")


#hue value supports 360 values i.e 0 to 259 but opencv supports 179
#else all 0 to 255
#size of window specification
cv.resizeWindow("TrackBars",640,240)
#0 to 179 will be displayed in the taskbar to drag
cv.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv.createTrackbar("Val Min","TrackBars",0,255,empty)
cv.createTrackbar("Val Max","TrackBars",255,255,empty)


#HSV=HUE SATURATION VALUE
while True:
  imgHSV=cv.cvtColor(img,cv.COLOR_BGR2HSV)
  h_min=cv.getTrackbarPos("Hue Min","TrackBars")
  h_max=cv.getTrackbarPos("Hue Max","TrackBars")
  s_min=cv.getTrackbarPos("Sat Min","TrackBars")
  s_max=cv.getTrackbarPos("Sat Max","TrackBars")
  v_min=cv.getTrackbarPos("Val Min","TrackBars")
  v_max=cv.getTrackbarPos("Val Max","TrackBars")


  #to get the best masked value v can even use default value
  """cv.createTrackbar("Hue Min", "TrackBars", 60, 179, empty)
  # HUE values range from 0 to 359 (360 values) but opencv supports only 180 values (0 to 179)
  cv.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
  cv.createTrackbar("Sat Min", "TrackBars", 100, 255, empty)
  cv.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
  cv.createTrackbar("Val Min", "TrackBars", 20, 255, empty)
  cv.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
  # there are 180 values for HUE. 179 is the highest."""


  print(h_min,h_max,s_min,s_max,v_min,v_max)

  #masking is hue, saturation is changed and changed all into white and black color
  lower=np.array([h_min,s_min,v_min])
  upper=np.array([h_max,s_max,v_max])
  mask=cv.inRange(imgHSV,lower,upper)


  #masked img is colored
  #only white part will be filtered and rest will remain black
  imgResult=cv.bitwise_and(img,img,mask=mask)


  #hue value changes in the terminal on changing values
  #cv.imshow("original", img)
  #cv.imshow("orIG", imgHSV)
  #cv.imshow("orIG1", mask)
  #cv.imshow("result", imgResult)

  imgStack=stackImages(0.6,([img,imgHSV],[mask,imgResult]))
  cv.imshow("Stacked images",imgStack)

  cv.waitKey(1)



cv.waitKey(0)