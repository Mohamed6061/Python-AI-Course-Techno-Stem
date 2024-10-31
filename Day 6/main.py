# Basic : Reading images 
#         Drawing Shapes 
#         Puttinh Text

# advanced :
#       Colors Chanels
#       BITWISE operations 
#       Masking 
#       Edge Detection  

# Face :
#       Face Detection , body, smile 
#       Face Recognition    
import cv2
import numpy as np
import os 

# harr cascade 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
img = cv2.imread('lady.jpg')
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

# harcascade = cv2.CascadeClassifier('harr_face.xml')
# harcascade = cv2.CascadeClassifier('body.xml')
harcascade = cv2.CascadeClassifier('smile.xml')
face_rect = harcascade.detectMultiScale(gray , scaleFactor=1.5 , minNeighbors= 10)

print(face_rect)

for (x,y, w,h) in face_rect :
    cv2.rectangle(img , (x,y) , (x+w , y+h ) , (0,255 , 0) , thickness= 2 )
    
cv2.imshow("image " , img )
cv2.imshow("image gray " , gray )
cv2.waitKey(0)