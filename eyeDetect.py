import cv2
import sys
import datetime
import time
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

log_file = open("timeLog.txt", "w", 0)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.7,
        minNeighbors = 5,
        minSize = (30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) < 1:
            print "Blink"
            sys.stdout.flush()
            
            #log time to a file
            millis = int(round(time.time() * 1000))
            t =str(millis)
            log_file.write("%s\n"%t)
            
        for (ex, ey, ew, eh) in eyes:
            blinkFlag = False
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh),(255, 0, 0), 2)
    

    # Display the resulting frame
    cv2.imshow('Eye&Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
log_file.close()
