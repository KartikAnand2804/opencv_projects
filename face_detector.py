import cv2
from random import randrange

#pretrained data
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # inputting trained data 


# choosing an image
# img = cv2.imread('avengers.png')

# getting the video feed
webcam = cv2.VideoCapture(0)

# parsing through the video feed frame by frame
while True:
	
	# reading the current video feed
	successful_frame_read, frame = webcam.read()
	greyscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# getting face coordinates
	face_coordinates = trained_face_data.detectMultiScale(greyscale_img) 

	# looping through the faces
	# cv2.rectangle(image, (coordinates for the upper left corner), (coordinates for the lower right corner), (colour scheme is B, G, R). thickness of the rect)
	for (x, y, w, h) in face_coordinates:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0 , 0), 2) 
	
	# displaying the video feed
	# cv2.imshow('name of the window', image) 
	cv2.imshow('default', frame)
	
	# cv2.waitKey(time in miliseconds input as an integer)
	key = cv2.waitKey(1)

	# press 'Q' to break from the app
	# ascii code for the key entered
	if key == 81 or key == 113:
		break

# to close the webcam
webcam.release()

#completion message
print("code completed")