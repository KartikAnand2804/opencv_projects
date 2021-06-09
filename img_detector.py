import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

src_img = 'chris.png'

greyscale_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY) #converts image to grey scale

face_coordinates = trained_face_data.detectMultiScale(greyscale_img) # detecting faces

print(face_coordinates)

for (x, y, w, h) in face_coordinates:
	cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2) #constructing the rectangle

cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2) # constructing the rectangle


cv2.imshow('face detector app', img)
cv2.waitKey() # to delay the code otherwise the image closes instantly