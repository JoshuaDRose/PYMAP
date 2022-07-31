""" STatus bar for installing stuff and showing progress """
import os
import utils
import pygame
import install


class StatusBar(object):
	def __init__(self, size, position):
		self.size = size
		self.data = utils.data_size(os.path.join('../meta','default.json'))
		self.position = position 
		self.show_status_bar = False 
		self.image = pygame.Surface(size)
		self.rect = self.image.get_rect()
		self.rect.x = position[0]
		self.rect.y = position[1]
		self.current_chunk = 0
		self.chunk_surfaces = []
		self.chunk_pos_x = 0
		self.chunk_width = round(self.size[0]/self.data)
		for chunk in range(self.data):
			chunk = pygame.Surface([self.chunk_width, self.size[1]])
			self.chunk_surfaces.append(chunk)
		self.chunks_visible = 0


	def update(self):
		""" Update the status bar by a certain amount """
		self.chunk_surfaces[self.current_chunk].fill([45,210,24])
		self.chunk_pos_x += self.chunk_width

	def incrament_chunk(self, amount=1):
		""" default amount should essentially just be 1 """
		self.chunks_visible += amount

	def draw(self, surface):
		if self.show_status_bar:
			surface.blit(self.chunk_surfaces[self.current_chunk], [self.chunk_pos_x, 0])

	def toggle_visible(self):
		self.show_status_bar = not self.show_status_bar
