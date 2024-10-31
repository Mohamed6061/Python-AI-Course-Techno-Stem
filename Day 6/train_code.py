import cv2
import numpy as np
import os 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

dir = r'E:\Techno City\AI python\Session files\Day 6\photos\train'

harcascade = cv2.CascadeClassifier('harr_face.xml')

features = []
labels = []
def create_train() :
    for person in people :
        path = os.path.join(dir ,person  )

        label = people.index(person)
        for img in os.listdir(path) :
            img_path = os.path.join(path , img)
            img_array= cv2.imread(img_path)
            # print(img_path)
            gray = cv2.cvtColor(img_array , cv2.COLOR_BGR2GRAY)
           
            face_rect = harcascade.detectMultiScale(gray , scaleFactor=1.5 , minNeighbors= 10)
            # print(face_rect)
            for (x,y, w,h) in face_rect :
                face_roi = gray[y: y+h , x:x+w]
                features.append(face_roi )
                labels.append(label)

            # cv2.imshow('image' , img_array)
            # cv2.waitKey(50)
        
create_train()

print("Train Done -------------------------------")

face_recongizer = cv2.face.LBPHFaceRecognizer_create()
# Train to recongizer on the features list and labels
features = np.array(features , dtype='object')
labels = np.array(labels)
face_recongizer.train(features , labels)
face_recongizer.save('face_training.yml')