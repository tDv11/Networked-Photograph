# CR: consider giving this file a better name, such as `main.py`
# CR: imports are organized into the following sections:
#     1. builtins
#     2. externals
#     3. your project
#     an empty line between sections. each section is sorted alphabetically
import sys

import cv2
import pygame
import pymongo

import light
import rwfile

# CR: General CR for this file: don't put logic immediately in the module.
#     Put your logic into functions and have them be called from a main function, which is called from a `__name__ == "__main__"` check.

# CR: consts should be UPPER_CASE
cascPath = "haarcascade_frontalface_default.xml"

# CR: looks like this code appears in `mongodb.py`
uri = 'mongodb://net_photo:net.photo456@ds111771.mlab.com:11771/net_photographs'
client = pymongo.MongoClient(uri)
db = client['net_photographs']
simulation = db.simulation
myphotoid = {'id': 1}

file = open("output.txt", "w")  # CR: don't name your variable `file` as this overrides the builtin type `file`

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

pygame.mixer.init()
pygame.mixer.music.load("first photo FOOD.mp3")

facetime = 0
prevfaces = 0
prevpower = 0
soundtime = 0

volum = 0.05  # CR: `volum` => `volume`
volumjump = 0.125
try:
  while True:
    # Create the haar cascade xml file
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Loop until the camera is working
    rval = False
    while(not rval):  # CR: not need for parentheses to surround `if`/`while` statements
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

    

    facetime += len(faces)
    simulation.update(myphotoid, {'$set': {'faceTime': facetime}})
    soundtime += len(faces)

    simulation.update(myphotoid, {'$set': {'prevLightPower': prevpower}})
        
    # call light func that deside light power
    light.change_light(prevfaces,len(faces),prevpower)
        

    #simulation.update(myphotoid, {'$set': {'lightPower': power}})
    simulation.update(myphotoid, {'$set': {'faces': len(faces)}})
    simulation.update(myphotoid, {'$set': {'prevFaces': prevfaces}})
        

    #if no recording is on, play
    if( len(faces) > 0 ):
        if( pygame.mixer.music.get_busy() == 0 ):
            pygame.mixer.music.play()
        #calculate volum power
        simulation.update(myphotoid, {'$set': {'prevSoundPower': volum}})
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
    simulation.update(myphotoid, {'$set': {'soundPower': volum}})

    cv2.imshow("Faces found", image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
except KeyboardInterrupt:
    pass

client.close()
cv2.destroyAllWindows()
cap.release()
file.close()
