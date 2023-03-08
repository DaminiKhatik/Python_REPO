"""Installing pygame
With pip:
pip install pygame
With conda:
conda install -c tlatorre pygame=1.9.2

"""
import pygame
from pygame import mixer

# Starting the mixer
pygame.mixer.init()
  
# Loading the song
pygame.mixer.music.load("audio.mp3")
  
# Setting the volume
pygame.mixer.music.set_volume(0.7)
  
# Start playing the song
pygame.mixer.music.play()
  
