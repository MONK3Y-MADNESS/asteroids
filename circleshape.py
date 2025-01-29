import pygame

class CircleShape(pygame.sprite.Sprite):
	def __init__(self, x, y, radius, velocity):
		if hasattr(self, "containers"):
			super().__init__(self.containers)
		else:
			super().__init__()

		self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
		self.rect = self.image.get_rect()

		self.position = pygame.Vector2(x, y)
		self.velocity = velocity
		self.radius = radius

	def draw(self, screen):
		pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

	def update(self, dt):
		pass

	def collisions(self, other):
		return self.position.distance_to(other.position) <= self.radius + other.radius
