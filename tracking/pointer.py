import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def select_point(event, x, y, flags, params):
    global point, point_selected
    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x,y)
        point_selected = True
        
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", select_point)

point_selected = False
point=()

while True:
    _, frame = cap.read()

    if point_selected is True:
        cv2.circle(frame, point, 5, (0,255,255), 2)
        cv2.imshow("Frame",frame)
    
    Key= cv2.waitKey(1)
    if Key == 27:
        break
        
cap.release()
cv2.destroyAllWindows()
