
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


print("Please provide the input path of the image")

print('\n')

path = input()
img = cv.imread(path,0)



img = cv.medianBlur(img,5)
cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=10,maxRadius=35)
circles = np.uint16(np.around(circles))

print('\n')

print("number of pipes present in this image is: " + str(circles.shape[1]))

for i in circles[0,:]:
    # draw the outer circle
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)


# font 
font = cv.FONT_HERSHEY_SIMPLEX 
  
# org 
org = (80, 25) 
  
# fontScale 
fontScale = 1
   
# Blue color in BGR 
color = (255, 0, 0) 
  
# Line thickness of 2 px 
thickness = 2
   
# Using cv2.putText() method 
cimg = cv.putText(cimg, 'Number of pipes detected is: ' + str(circles.shape[1]), org, font,  
                   fontScale, color, thickness, cv.LINE_AA) 


cv.imshow('detected pipes',cimg)
cv.waitKey(0)
cv.destroyAllWindows()


#/home/snehashis/Desktop/python files/image/Task_3_Pipe_Counting.jpeg
