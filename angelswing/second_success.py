import numpy as np
import cv2

img= cv2.imread('test 01.tif')
canny = cv2.Canny(img,30,70)
height=img.shape[0]
width=img.shape[1]

cv2.imwrite('canny.jpg',canny)

ret, thresh = cv2.threshold(canny,127,255,0)
image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

f = open('second success.svg', 'w+')
f.write('<?xml version="1.0" encoding="utf-8"?>')
f.write('<svg version="1.0" id="Layer_1" width="'+str(width)+'" height="'+str(height)+'" xmlns="http://www.w3.org/2000/svg" xml:space="preserve">')

for i in range(len(contours)):
    f.write('<path d= "M')
    for j in range(len(contours[i])):
        x,y = contours[i][j][0]
        f.write(str(x)+  ' ' + str(y)+' ')
    f.write('" style="fill:none;stroke:black;stroke-width:1"/>')
        
f.write('</svg>')
f.close()
