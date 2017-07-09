import pygame
import sys
import cv2

def uponUs():
    print('DoomsDay as started :( ')
    CASC_PATH = "haarcascade_frontalface_default.xml"

    cap = cv2.VideoCapture(0)
    cap.set(3, 320)
    cap.set(4, 240) 

    pygame.mixer.init()
    pygame.mixer.music.load("10 mission.mp3")
    min_volum = volum = 0.05
    max_volum = 1.0
    volum_jump = 0.23

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
                    cap.release()
                    cap = cv2.VideoCapture(0)
                    cap.set(3, 320)
                    cap.set(4, 240)
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
             # to do if there are ppl
            if len(faces) > 0 :
                volum = volum_jump * len(faces)
                # if no recording is on, play
                if pygame.mixer.music.get_busy() == 0 :
                    pygame.mixer.music.play()
                    
            # calibrate if overflow      
            if volum > max_volum :
                volum = max_volum
            if volum < min_volum :
                volum = min_volum   
            
            pygame.mixer.music.set_volume(volum)
            print(volum)
            
    except KeyboardInterrupt:
        pass
    
        cap.release()

        
