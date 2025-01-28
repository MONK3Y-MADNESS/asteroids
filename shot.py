
import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
	def __init__(self, x, y, velocity):
		super().__init__(x, y,velocity, SHOT_RADIUS)

	def update(self, dt):
		self.position += self.velocity * dt

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)
