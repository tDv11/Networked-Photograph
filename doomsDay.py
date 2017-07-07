import pygame
import sys
import cv2

def uponUs():
    cap.release()
    
    CASC_PATH = "haarcascade_frontalface_default.xml"

    min_volum = volum = 0.05
    max_volum = 1.0
    volum_jump = 0.16

    cap = cv2.VideoCapture(0)
    cap.set(3, 320)
    cap.set(4, 240)

    pygame.mixer.init()
    pygame.mixer.music.load("8 Dostoevsky.mp3")

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
                # if no recording is on, play
                if pygame.mixer.music.get_busy() == 0 :
                    pygame.mixer.music.play()
                    
            # calculate volume power
            volum = len(faces) * volum_jump
            if volum > max_volum :
                volum = max_volum
            if volum < min_volum :
                volum = min_volum
            
            pygame.mixer.music.set_volume(volum)
            
    except KeyboardInterrupt:
        break
    
        cap.release()

        
