import pygame
import sys
import time

#initialize pygame
pygame.init()

#load click sounds
click_sound = pygame.mixer.Sound('click.wav') 

#function to play click sound
def play_click_sound():
    click_sound.play()
    time.sleep(0.1)  # Optional delay to prevent overlapping sounds

#event handling loop
def main():
    pygame.display.set_mode((800, 600))

    while True:
        for event in pygame.event.get():  # If you're using Pygame
            if event.type == pygame.MOUSEBUTTONDOWN:  # If you're using Pygame
                play_click_sound()
                
                
#call main function
if __name__ == '__main__':
    main()



