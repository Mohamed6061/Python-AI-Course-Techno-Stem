import cv2
import numpy as np
import os 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

video = cv2.VideoCapture("2.avi")
full_body_harcascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

while True :
    _ , frame = video.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY )
    
    bodies = full_body_harcascade.detectMultiScale(gray, scaleFactor=1.1 , minNeighbors= 2 )
    
    for (x,y,w,h) in bodies :
        cv2.rectangle(frame, (x,y) , (x+ w , y+h) , (0,255,0) , 2 )
        
        
    cv2.imshow("Video out" , frame )

    
    if cv2.waitKey(30) & 0xff == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()