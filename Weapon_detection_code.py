import numpy as np
import cv2
import imutils
import datetime
from subprocess import Popen 

gun_cascade = cv2.CascadeClassifier('./Xml_File/Gun_cascade.xml')
camera = cv2.VideoCapture(0)

# initialize the first frame in the video stream
firstFrame = None
# loop over the frames of the video

gun_exist = False

while True:
    (grabbed, frame) = camera.read()

    # if the frame could not be grabbed, then we have reached the end of the video
    if not grabbed:
        break
    frame = imutils.resize(frame, width=700)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    gun = gun_cascade.detectMultiScale(gray, 1.3, 7, minSize = (80, 80))
    
    if len(gun) > 0:
        gun_exist = True
     
    for (x,y,w,h) in gun:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]    
        cv2.imwrite('image.jpg',frame)

    # show the frame and record if the user presses a key
    cv2.imshow("Security Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
			
if gun_exist:
    print("guns detected")
    Popen('python Email_Sending_Code.py')

   
else:
    print("guns NOT detected")

camera.release()
cv2.destroyAllWindows()







