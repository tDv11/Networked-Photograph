
import pygame

def change_sound( flag, curr, stage ):
    #init the sound file
    pygame.mixer.init()
    pygame.mixer.music.load("first photo FOOD.mp3")
    if( flag ==1  #&& pygame.mixer.music.get_busy() == False:
        ):
        pygame.mixer.music.play()


