
import pygame

def change_sound( soundtime ):
    #init the sound file
    pygame.mixer.init()
    pygame.mixer.music.load("first photo FOOD.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue




