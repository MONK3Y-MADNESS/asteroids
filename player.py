import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape, pygame.sprite.Sprite):
	def __init__(self, x, y):
		CircleShape.__init__(self, PLAYER_RADIUS, x, y)
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([PLAYER_RADIUS * 3, PLAYER_RADIUS * 3], pygame.SRCALPHA)
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self._draw_triangle()

	def _draw_triangle(self):
		self.image.fill((0,0,0,0))
		pygame.draw.rect(self.image, (255, 0, 0, 128), self.image.get_rect(), 1)
		pygame.draw.polygon(self.image, "white", self._transform_points(), 2)

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def update(self, dt):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_a]:
			self.rotate(-dt)

		self.rect.center = (self.position.x, self.position.y)
		self._draw_triangle()

	def _transform_points(self):
		points = self.triangle()
		local_points = [
			(
				point.x - self.position.x + self.rect.width / 2,
				point.y - self.position.y + self.rect.height / 2
			)

			for point in points
		]
		return local_points

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def triangle(self):
		forward = pygame.Vector2(0, -1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
