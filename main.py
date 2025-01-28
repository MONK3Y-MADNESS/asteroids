
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

pygame.init()

def main():

	print("Starting asteroids!")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption("Asteroids")
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.RenderUpdates()
	asteroids = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	AsteroidField.containers = updatable
	Asteroid.containers = (asteroids, updatable, drawable)

	asteroid_field = AsteroidField()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False

		screen.fill("black")
		dt = clock.tick(60) / 1000
		updatable.update(dt)
		drawable.draw(screen)
		pygame.display.flip()

	pygame.quit()

if __name__ == "__main__":
	main()
