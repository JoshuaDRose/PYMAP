import pygame

class Button(pygame.sprite.Sprite):
	""" Buttons for toolbar(s) """
	def __init__(self, pos, size,color, hover, tick=False,cross=False):
		pygame.sprite.Sprite.__init__(self)
		self.color = color
		self.hover = hover
		self.image = pygame.Surface(size)
		self.invis_surface = pygame.Surface(size)
		self.invis_surface.fill([200,200,200])
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]
		self.tick = tick
		self.cross = cross
		self.hovering = False
		self.visible = True

	def update(self):
		if not self.visible:
			self.image = self.invis_surface
		else:
			if self.hovering:
				self.image.fill(self.hover)
			else:
				self.image.fill(self.color)
			if self.tick:
				pygame.draw.line(self.image,([0,0,0]), (0, 13), (12, 25), 3)
				pygame.draw.line(self.image,([0,0,0]), (12, 25), (25, 0), 3)
			if self.cross:
				pygame.draw.line(self.image,([0,0,0]), (0,0), (25, 25), 3)
				pygame.draw.line(self.image,([0,0,0]), (0,25), (25, 0), 3)