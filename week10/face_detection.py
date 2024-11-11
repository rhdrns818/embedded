import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while True:
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
  _,frame = cap.read()
  frame = cv2.flip(frame,0)

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray)
  print('faces : ', faces)
  print("Number of faces detected: " + str(len(faces)))

  for (x,y,w,h) in faces:
    frame = cv2.rectangle(frame, (x,y),(x + w, y +h), ( 255, 0, 0), 1)
    roi_gray = gray[y:y + h, x: x + w]
    roi_color = frame[y:y + h, x: x + w]

    cv2.imshow('face_detection',frame)
    if cv2.waitKey(1) & 0xFF == 27:
      break
cap.release()
cv2.destroyAllWindows()
