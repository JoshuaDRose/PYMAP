import pygame


class Sidebar(object):
	def __init__(self):
		self.size = [100,770]
		self.position = [0,0]
		self.surface = pygame.Surface(self.size)
		self.surface.fill([248, 161, 69])
		self.rect = self.surface.get_rect()
		self.rect.x = self.position[0]
		self.rect.y = self.position[1]

	def draw(self, surface):
		surface.blit(self.surface, self.rect)