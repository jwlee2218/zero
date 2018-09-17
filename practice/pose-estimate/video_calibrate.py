# import opencv module
import cv2
from matplotlib import pyplot as plt
import numpy as np
import copy

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.01)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)

objp = np.zeros((7*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:7].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

cap = cv2.VideoCapture('input.avi')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT)) 

out = cv2.VideoWriter('output.avi', fourcc, 30.0,(frame_width,frame_height))

while True:
    success,frame = cap.read()
    if success:     
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret,corners = cv2.findChessboardCorners(gray, (7,7), None)
        
        if ret:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
            cv2.drawChessboardCorners(frame, (7,7), corners, ret)
            imgpoints.append(corners2)
        
        cv2.namedWindow('original', cv2.WINDOW_NORMAL)        
        cv2.imshow('original', frame)
        out.write(frame)
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


ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
np.savez('calib.npz', mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)


