import cv2
import numpy as np

img = cv2.imread('i.jpg')
img = cv2.resize(img , (300 , 200))
imggray = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
imgh = np.hstack((img , img))
imgv = np.vstack((img , imggray))
cv2.imshow("img" , img)
cv2.imshow("imgh" , imgh)
cv2.imshow("imgv" , imgv)
cv2.imshow("imgg" , imggray)
cv2.waitKey(0)
