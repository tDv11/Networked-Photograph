import light
import rwfile
import cv2
import pygame

cascPath = "haarcascade_frontalface_default.xml"

file = open("output.txt","w")

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

pygame.mixer.init()
pygame.mixer.music.load("first photo FOOD.mp3")

facetime = 0
prevfaces = 0
prevpower = 0
soundtime = 0

volum = 0.05
volumjump = 0.16
try:
  while True:
    # Create the haar cascade xml file
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Loop until the camera is working
    rval = False
    while(not rval):
        # Read the image
        (rval,image) = cap.read()
        if(not rval):
            print("Failed to open webcam. Trying again...")

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    # flags = cv2.CV_HAAR_SCALE_IMAGE
        )

    #send diff to mongoDB print('difference :' + str(diff))
    
    if( len(faces) > 0 ): #if there r faces
        facetime += len(faces)
        soundtime += len(faces)
        # call light func that deside light power
        light.change_light(prevfaces,len(faces),prevpower)

        #if no recording is on, play
        if( pygame.mixer.music.get_busy() == 0 ):
            pygame.mixer.music.play()
        #calculate volum power
        volum = len(faces) * volumjump
        #logs
        rwfile.rw_file(faces,facetime,file)
       
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #if volum pass max calibrate      
    if( volum >1.0 ):
        volum = 1.0
    #if no faces calibrate
    if( len(faces) == 0 ):
        volum = 0.05
    pygame.mixer.music.set_volume(volum)

    cv2.imshow("Faces found", image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
except KeyboardInterrupt:
    pass


cv2.destroyAllWindows()
cap.release()
file.close()
