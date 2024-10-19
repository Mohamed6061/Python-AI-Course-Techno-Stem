# Basic :
    # Reading img and video
    # Drawing 
    # putting text
# Advanced
    # Edge detection
    # color chanels
    # BITWISE 
    # Masking
# Face
    # Face detection & body & simle & eye
    # Face recongition


import cv2
import numpy as np
import os 

os.chdir(os.path.dirname(os.path.abspath(__file__)))
###################################################################3
# ----------------- color chanels --------------------------------#

# R ---> Red
# G ---> Green
# B ---> blue
# img = cv2.imread('park.jpg')
# blank = np.zeros(img.shape[:2] , dtype= "uint8")
# b , g , r = cv2.split(img)

# blue = cv2.merge([b , blank, blank])
# green = cv2.merge([blank, g , blank])
# red = cv2.merge([blank, blank, r ])

# merage_image = cv2.merge([ blank , g , r ])
# cv2.imshow("merage imge" , merage_image)

# cv2.imshow("main image" , img)
# cv2.imshow("blue image" , blue)
# cv2.imshow("green image" , green)
# cv2.imshow("red image" , red)
# cv2.waitKey(0)

# --------------------- Bitwise ------------------------------#

# blank = np.zeros( (400 ,400), dtype= "uint8")


# rectangule_img = cv2.rectangle(blank.copy() , (10 , 10) , (350,350), 255 , -1 )
# circle_img = cv2.circle(blank.copy() , (200,200) , 200 ,255,  -1 )

# cv2.imshow(" blank_cicle" , rectangule_img)
# cv2.imshow(" blank_rec" , circle_img)

# bitwise_and = cv2.bitwise_and(rectangule_img , circle_img )
# cv2.imshow("bitwise and" , bitwise_and )

# bitwise_or = cv2.bitwise_or(rectangule_img , circle_img )
# cv2.imshow("bitwise or" , bitwise_or )

# bitwise_xor = cv2.bitwise_xor(rectangule_img , circle_img )
# cv2.imshow(" bitwise_xor" , bitwise_xor )

# bitwise_not = cv2.bitwise_not(rectangule_img)
# cv2.imshow(" bitwise  not " , bitwise_not )
# cv2.waitKey(0)

# --------------------- Masking ------------------------------#
# img  = cv2.imread('park.jpg')
# cv2.imshow("part image", img)

# blank = np.zeros(img.shape[:2], dtype= "uint8")
# cv2.imshow("blank image", blank)

# # circle = cv2.circle(blank, (img.shape[1]//2 , img.shape[0]//2) , 200 , 255 , -1 ) 
# rectangule_img = cv2.rectangle(blank , (50 , 50) , (350,350), 255 , -1 )
# cv2.imshow("blank image", rectangule_img)

# masked_img = cv2.bitwise_and(img , img , mask= rectangule_img)
# cv2.imshow("masked image", masked_img)

# print(img.shape )
# cv2.waitKey(0)

# --------------------- Masking with video ------------------------------#
video = cv2.VideoCapture('test1.mp4')

while True :
    _ , frame = video.read()
    frame_reszied = cv2.resize(frame , (500,400))
    blank = np.zeros(frame_reszied.shape[:2], dtype= "uint8")
    
    circle = cv2.circle(blank, (frame_reszied.shape[1]//2 , frame_reszied.shape[0]//2) , 200 , 255 , -1 )
    
    masked_frame = cv2.bitwise_not(frame_reszied, mask=circle)
    cv2.imshow("Video masked_frame " , masked_frame )
    
    cv2.imshow("Video frame_reszied " , frame_reszied )
    if cv2.waitKey(50) & 0xFF == ord('q') :
        break 

video.release()
cv2.destroyAllWindows()
    