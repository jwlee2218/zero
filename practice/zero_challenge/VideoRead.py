import cv2
from matplotlib import pyplot as plt
import numpy as np
import copy

cap = cv2.VideoCapture('video.MOV')
# cap = cv2.VideoCapture(0)

## VideoWrite (혹은 XVID) 는 BGR format만 저장 가능하다
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 25.0,(1080,1920))

while True:
    ret,frame = cap.read()
    if ret:
#         frame = cv2.bilateralFilter(frame,9,25,75)
#         gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
        img_hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
        s_channel=img_hsv[:,:,2]
        s_thresh_min=0
        s_thresh_max=255
        s_binary=np.zeros_like(s_channel)
        s_binary[(s_channel >= s_thresh_min) & (s_channel <= s_thresh_max)] = 1

        cv2.namedWindow('original', cv2.WINDOW_NORMAL)
        out.write(frame)
        cv2.imshow('original', s_binary)
        c=cv2.waitKey(1)
        if c == 27:
            break
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
