
import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
	def __init__(self, x, y, velocity):
		self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), pygame.SRCALPHA)
		super().__init__(x, y, SHOT_RADIUS, velocity)

	def update(self, dt):
		self.position += self.velocity * dt
		self.rect.center = self.position

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)
