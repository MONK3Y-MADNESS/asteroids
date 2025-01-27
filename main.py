
import pygame
from constants import *

pygame.init()

def main():

	print("Starting asteroids!")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	running = True
	while running:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		screen.fill(0, rect=None, special_flags=0)
		pygame.display.flip()

if __name__ == "__main__":
	main()
