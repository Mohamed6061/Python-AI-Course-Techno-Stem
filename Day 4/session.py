import cv2
import numpy as np
#################################################
#---------- Essention Fuctions-----------------#

# img = cv2.imread(r'E:\Techno City\AI python\Session files\Day 4\cat_large.jpg')
# resized = cv2.resize(img, (300, 400))
# cv2.imshow("people" , resized )

# # convert o gray
# gray_img = cv2.cvtColor(resized , cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray image" , gray_img )

# # Blur
# blur_img = cv2.GaussianBlur(resized , (7,7) , cv2.BORDER_DEFAULT )
# cv2.imshow("Blur image" , blur_img)

# canny = cv2.Canny(resized , 125 , 175)
# cv2.imshow("canny image" , canny)

# canny = cv2.Canny(blur_img , 125 , 175)
# cv2.imshow("canny  with blur image" , canny)

# cropped = resized[100:200 , 100:3100 ]
# cv2.imshow("cropped image" , cropped)
# cv2.waitKey(0)

#################################################
#---------- Contours Detection -----------------#

# img = cv2.imread(r'E:\Techno City\AI python\Session files\Day 4\CV2_logo.jpeg')

# blank = np.zeros((400, 400 ,3), dtype='uint8') 
# cv2.imshow("blank" , blank )

# resized = cv2.resize(img, (300, 400))
# cv2.imshow("people" , resized )

# # Blur
# blur_img = cv2.GaussianBlur(resized , (7,7) , cv2.BORDER_DEFAULT )
# # cv2.imshow("Blur image" , blur_img)

# canny = cv2.Canny(blur_img , 125 , 175)
# # cv2.imshow("canny  with blur image" , canny)

# contours, _ = cv2.findContours(canny, cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE )


# cv2.drawContours(blank , contours, -1  , (0,255,0), 2)
# cv2.imshow('Contours Drawn', blank)


# cv2.waitKey(0)

#################################################
#---------- Contours Detection  Video ----------#

cap = cv2.VideoCapture(r"E:\Techno City\AI python\Session files\Day 4\test1.mp4")
blank = np.zeros((300, 400 ,3), dtype='uint8') 
while True :
    ret , frame  = cap.read()
    frame = cv2.resize(frame , (500,250) )
    cv2.imshow("video", frame)

    # Blur
    blur_img = cvq2.GaussianBlur(frame , (7,7) , cv2.BORDER_DEFAULT )
    cv2.imshow("Blur image" , blur_img)

    canny = cv2.Canny(blur_img , 125 , 175)
    cv2.imshow("canny  with blur image" , canny)

    contours, _ = cv2.findContours(canny, cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE )


    cv2.drawContours(blank , contours, -1  , (0,255,0), 2)
    cv2.imshow('Contours Drawn', blank)
    blank = np.zeros((400, 400 ,3), dtype='uint8') 
    
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()