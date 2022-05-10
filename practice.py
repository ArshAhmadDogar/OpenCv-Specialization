import cv2
import sys

capture = cv2.VideoCapture(sys[1])

while capture.isOpened():
    ret,frame = capture.read()
    if ret is True:
        cv2.imshow('frame',frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break 
    else:
        break
capture.release()
cv2.destroyAllWindows()

