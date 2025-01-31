import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius, pygame.Vector2(0, 0))

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		if self.radius <= ASTEROID_MIN_RADIUS:
			return

		random_angle = random.uniform(20, 50)

		new_1 = self.velocity.rotate(random_angle)
		asteroid = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid.velocity = new_1 * 1.2

		new_2 = self.velocity.rotate(-random_angle)
		asteroid = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid.velocity = new_2 * 1.2
