import keyboard
import os
import webbrowser
from playsound import playsound
while 10 > 1:
    if keyboard.is_pressed('b'):  # if key 'q' is pressed 
        playsound("SoundEffects/bruh.mp3")
    if keyboard.is_pressed("e"):
        playsound("SoundEffects/gun.mp3")
    if keyboard.is_pressed("q"):
        break
    else:
        pass
