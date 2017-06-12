import cv2
import sys
from datetime import datetime
from phue import Bridge
import random
import pygame

# Get user supplied values
cascPath = "haarcascade_frontalface_default.xml"
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)
# Create the txt file for Face Time value
file = open("output.txt","w")
FaceTime = 0
FaceRatio = 0
diff = 0
Power = 0
#philips hue light connection
b = Bridge("10.0.9.252")
#b.connect()

#init the sound file
pygame.mixer.init()
pygame.mixer.music.load("first photo FOOD.mp3")

while 1:
    now = datetime.now()
    # Create the haar cascade xml file
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    _, image = cap.read()

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    # flags = cv2.CV_HAAR_SCALE_IMAGE
        )

    #print("Found {0} faces!".format(len(faces)))
    if( Power >= 250 ):
        Power = 0
    if( len(faces) != 0 ):
        if( Power == 5 ):
            pygame.mixer.music.play()
        if( FaceRatio < len(faces)):
            diff = len(faces) - FaceRatio
            #send diff to mongoDB
            print('difference :' + str(diff))
        # Add the current num of faces to the existing count
        FaceRatio = len(faces)
        FaceTime += FaceRatio
        Power += len(faces)
        #if there r faces activate light
        b.set_light(1, 'bri', Power)
        # Timestamp in txt
        file.write(now.strftime('%Y-%m-%d %H:%M ->\n'))
        # current num of faces in txt
        file.write('Faces Detected=' + format(len(faces)) + '\n')
        # coordinates in txt
        for (x, y, w, h) in faces:
           file.write('x=' + str(x) + ' y=' + str(y) + '\n')
        #num of faces so far in txt
        file.write('Face Time=' + str(FaceTime) + 'seconds')
        file.write('\n¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Faces found", image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
file.close()
