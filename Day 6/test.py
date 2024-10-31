import cv2
import numpy as np
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

haar_cascade = cv2.CascadeClassifier('harr_face.xml')
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

face_recongizer = cv2.face.LBPHFaceRecognizer_create()

face_recongizer.read('face_training.yml')

img_test = cv2.imread(r'E:\Techno City\AI python\Session files\Day 6\photos\val\jerry_seinfeld\3.jpg')
gray = cv2.cvtColor(img_test, cv2.COLOR_BGR2GRAY)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)


for (x,y, w,h) in faces_rect :
    face_roi = gray[y: y+h , x:x+w]
    
    label , confidence = face_recongizer.predict(face_roi)
    # print(f'Label = {people[label]} with a confidence of {confidence}')

    cv2.putText(img_test, str(people[label]), (20,20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv2.rectangle(img_test, (x,y), (x+w,y+h), (0,255,0), thickness=2)
cv2.imshow("img", img_test)

cv2.waitKey(0)
    

