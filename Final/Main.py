
import sys

import cv2
import pygame
import pymongo

import light
import log

def main():
    CASC_PATH = "haarcascade_frontalface_default.xml"
    uri = 'mongodb://net_photo:net.photo456@ds111771.mlab.com:11771/net_photographs'
    client = pymongo.MongoClient(uri)
    db = client['net_photographs']
    simulation = db.simulation
    my_photo_id = {'id': 1}

    my_file = open("log.txt", "w")  

    cap = cv2.VideoCapture(0)
    cap.set(3, 320)
    cap.set(4, 240)

    pygame.mixer.init()
    pygame.mixer.music.load("first photo FOOD.mp3")

    face_time = 0
    prev_faces = 0
    prev_power = 0
    sound_time = 0

    volum = 0.05  # CR: `volum` => `volume`
    volumjump = 0.125
    try:
        while True:
        # Create the haar cascade xml file
        faceCascade = cv2.CascadeClassifier(CASC_PATH)

        # Loop until the camera is working
        rval = False
        while not rval :
            # Read the image
            (rval,image) = cap.read()
            if not rval :
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
        
        # call light func that deside light power
        ( prev_faces, prev_power ) = light.change_light(prev_faces,len(faces),prev_power)    
        
        # to do if there are ppl
        if len(faces) > 0 :
            # if no recording is on, play
            if pygame.mixer.music.get_busy() == 0 :
                pygame.mixer.music.play()
           
            # update curr faces on db + inc FaceTime but the curr faces
            simulation.update(myphotoid, {'$set': {'faces': len(faces)}})
            simulation.findOneAndUpdate( myphotoid, { $inc: { "faceTime" : len(faces) } } )
            
            # calculate volume power
            volum = len(faces) * volumjump
            soundtime += len(faces)
            # logs
            log.log(faces,facetime,my_file)
       
            # draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # if volume pass max calibrate      
        if volum >1.0 :
            volum = 1.0
        # if no faces calibrate
        if len(faces) == 0 :
            volum = 0.05
        pygame.mixer.music.set_volume(volum)

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
    
if __name__ == '__main__':
    main()
