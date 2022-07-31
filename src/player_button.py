import os
import pygame

class PlayerButton(pygame.sprite.Sprite):
	def __init__(self, position, size, image):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.size = size
		self.image = pygame.image.load(os.path.join('../assets', image+'.png'))
		self.rect = self.image.get_rect()
		self.rect.x = self.position[0]
		self.rect.y = self.position[1]
		self.hovering = False
		
