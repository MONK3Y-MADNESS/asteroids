
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	print("Starting asteroids!")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption("Asteroids")
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	AsteroidField.containers = updatable
	Asteroid.containers = (asteroids, updatable, drawable)
	asteroid_field = AsteroidField()
	Shot.containers = (shots, updatable, drawable)

	Player.containers = (updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	dt = 0

	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False


		for obj in updatable:
			result = obj.update(dt)
			if result is not None:
				shots.add(result)

		for asteroid in asteroids:
			if player.collisions(asteroid):
				print("Game over!")
				running = False
			for shot in shots:
				if asteroid.collisions(shot):
					shot.kill()
					asteroid.split()

		screen.fill("black")
		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		dt = clock.tick(60) / 1000

	pygame.quit()

if __name__ == "__main__":
	main()
