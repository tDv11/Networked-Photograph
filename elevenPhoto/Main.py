
import sys

import cv2
import pygame
import pymongo

import light
import log

def main():
    CASC_PATH = "haarcascade_frontalface_default.xml"
    URI = 'mongodb://net_photo:net.photo456@ds139322.mlab.com:39322/net_photographs'
    
    client = pymongo.MongoClient(URI)
    db = client['net_photographs']
    simulation = db.sessions
    my_photo_id = {'photoID': 11}
    

    my_file = open("log.txt", "w")  

    cap = cv2.VideoCapture(0)
    cap.set(3, 320)
    cap.set(4, 240)

    pygame.mixer.init()
    pygame.mixer.music.load("11 ignorance.mp3")

    face_time = 0
    # init face_time from DB
    cursor = simulation.find( my_photo_id )
    for doc in cursor:
        face_time = doc['accumulateViewersPerDay']
    
    prev_faces = 0
    prev_power = 0
    sound_time = 0

    min_volum = volum = 0.05
    max_volum = 1.0
    volum_jump = 0.16
    try:
        while True:
            # Create the haar cascade xml file
            face_cascade = cv2.CascadeClassifier(CASC_PATH)

            # Loop until the camera is working
            rval = False
            while not rval :
                # Read the image
                (rval,image) = cap.read()
                if not rval :
                    print("Failed to open webcam. Trying again...")

            gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
            # flags = cv2.CV_HAAR_SCALE_IMAGE
                )
        
            # call light func with the photo's properties
            ( prev_faces, prev_power ) = light.change_light(prev_faces,len(faces),prev_power)
            simulation.update(my_photo_id, {'$set': {'currentLightning': prev_power}})
            
        
            # to do if there are ppl
            if len(faces) > 0 :
                face_time += len(faces)
                # if no recording is on, play
                if pygame.mixer.music.get_busy() == 0 :
                    pygame.mixer.music.play()
           
                # update curr faces on db + inc FaceTime but the curr faces
                simulation.update(my_photo_id, {'$set': {'currentViewers': len(faces)}})
                simulation.update(my_photo_id, {'$set': {'accumulateViewersPerDay': face_time}})
                
            
                # calculate volume power
                volum = len(faces) * volum_jump

                # logs
                lastUpdate = log.log(faces,face_time,my_file)
                simulation.update(my_photo_id, {'$set': {'lastUpdate': lastUpdate }})
       
                # draw a rectangle around the faces
                #for (x, y, w, h) in faces:
                    #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # calibrate if overflow      
            if volum > max_volum :
                volum = max_voum
            if volum < min_volum :
                volum = min_volum
        
            pygame.mixer.music.set_volume(volum)

            #cv2.imshow("Faces found", image)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
    
    except KeyboardInterrupt:
        pass

    client.close()
    cv2.destroyAllWindows()
    cap.release()
    my_file.close()
                    
        

    
if __name__ == '__main__':
    main()
