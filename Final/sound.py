import pygame

def change_sound(soundtime):  # CR: maybe should be called `play_sound`?
    #init the sound file
    pygame.mixer.init()
    pygame.mixer.music.load("first photo FOOD.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:  # CR: `get_busy` returns bool, no need to compare to `True`. simply write `while pygame.mixer.music.get_busy():`
        continue  # CR: when executing a busy-loop, use `time.sleep`

# CR: many empty new-lines in the end of the file. leave exactly one


