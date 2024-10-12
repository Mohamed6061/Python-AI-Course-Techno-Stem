
# ## Start with openCV
# <ul> 
# Basics :
# <li>Reading Images and video</li>
# <li> Images Transformations</li>
# <li>Drawing Shapes</li>
# <li>Puttinh Text</li>
# </ul>
# <hr> 
# <ul> 
# advanced :
# <li>Colors Spaces</li>
# <li>BITWISE operations</li>
# <li>Masking</li>
# <li>Histogram Computation</li>
# <li>Edge Detection</li>
# </ul>
# <hr>

# <ul> 
# Face :
# <li>Face Detection</li>
# <li>Face Recognition</li>
# <li>Deep computer vision model</li>
# </ul>

import cv2
import numpy as np
########### part 1

# Read image]
# img = cv2.imread(r'E:\Techno City\AI python\Session files\Day3\Photos\cat.jpg')
# cv2.imshow('image title', img)
# cv2.waitKey(0)

# Video

# cap = cv2.VideoCapture(r"E:\Techno City\AI python\Session files\Day3\test.avi")
# while True :
#     ret , frame  = cap.read()
#     cv2.imshow("video", frame)
#     if cv2.waitKey(50) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
# ---------------------------------------------
######## part 2 Resizing & Rescaling

# cap =  cv2.VideoCapture(r"E:\Techno City\AI python\Session files\Day3\test.avi")

# def rescaleFrame(frame , scale =0.75) :
#     width = int(frame.shape[1] *scale)
#     height = int(frame.shape[0] * scale)
    
#     dimensions = (width , height)
#     return cv2.resize(frame , dimensions , interpolation=cv2.INTER_AREA )


# while True :
#     ret , frame  = cap.read()
#     cv2.imshow("video", frame)
#     frame_resized = rescaleFrame(frame , 0.3)

#     cv2.imshow("resized video", frame)
#     cv2.imshow("resized video", frame_resized)

#     if cv2.waitKey(50) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

# with image
# img = cv2.imread(r'E:\Techno City\AI python\Session files\Day3\Photos\cat.jpg')
# riMG = rescaleFrame(img , 0.3)
# cv2.imshow('image title', riMG)
# cv2.imshow('image ', img)
# cv2.waitKey(0)

# ---------------------------------------------
# ########################### part 3 Drawing

# blank = np.zeros((500,500,3), dtype='uint8') 
# BGR (Blue, Green, Red)

# blank[:] = 0, 255 ,0
# cv2.rectangle(blank, (10,10), (490,490), (0,255,0) , thickness=2)
# cv2.rectangle(blank, (10,10), (490,490), (0,255,0) , thickness= cv2.FILLED)

# Circle
# cv2.circle(blank , (250,250) , 40 , (0,0,255),thickness= -1 )

# Line
# cv2.line(blank, (10,10), (490,490) ,  (255, 0 ,0) , thickness= 2 )

# write text on img
# cv2.putText(blank , "put text here to write on img" , (0,200) , cv2.FONT_HERSHEY_DUPLEX ,1.0 ,(0,255,0) , 2 )

# cv2.imshow('REC', blank)

# cv2.waitKey(0)
# --------------------------------------------------------
# ##################### part 4 Essential Function in opencv

# img = cv2.imread(r'E:\Techno City\AI python\Session files\Day3\Photos\park.jpg')

# Converting to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Blur 
# blur = cv2.GaussianBlur(img , (7,7) ,cv2.BORDER_DEFAULT )

# Edge cascade
# canny = cv2.Canny(blur, 125 ,175 )

# # Dialating the image
# dialated = cv2.dilate(canny , (7,7) , iterations= 5 )

# # Eroding the image
# rode = cv2.erode(dialated, (7, 7), iterations=5)

# # resize
# resized = cv2.resize(img , (500,500) )

# Cropped 
# cropped = img[50:200 , 100:300 ]

# cv2.imshow('image ', img)
# cv2.imshow('BLUR ', canny  )
# cv2.imshow('dialated ', dialated  )
# cv2.imshow('erode ', rode  )
# cv2.imshow('resized ', resized  )
# cv2.imshow('cropped ', cropped  )
# cv2.waitKey(0)

# --------------------------------------------------------
# ##################### part 5 | Contour Detection

img = cv2.imread(r'E:\Techno City\AI python\Session files\Day3\Photos\cats.jpg')
blank = np.zeros((500,500,3), dtype='uint8') 

blank = np.zeros(img.shape, dtype='uint8')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)

canny = cv2.Canny(blur, 125, 175)

# ret, thresh = cv2.thresho 

contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv2.drawContours(blank, contours, -1, (0,0,255), 1)
cv2.imshow('Contours Drawn', blank)

cv2.waitKey(0)
