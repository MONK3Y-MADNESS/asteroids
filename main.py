
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

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

	shots.containers = (shots, updatable, drawable)
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
				if event.key == pygame.K_SPACE:
					new_shot = player.shoot()
					shots.add(new_shot)


		for obj in updatable:
			obj.update(dt)
		shots.update(dt)

		screen.fill("black")

		for obj in drawable:
			obj.draw(screen)
		shots.draw(screen)

		for asteroid in asteroids:
			if player.collisions(asteroid):
				print("Game over!")
				running = False

		pygame.display.flip()

		dt = clock.tick(60) / 1000

	pygame.quit()

if __name__ == "__main__":
	main()
