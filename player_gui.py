""" Player gui in bottom right """
import pygame
import os



class Player():
	def __init__(self, surface):
		self.surface = surface
		self.width = self.surface.get_width()
		self.xpos = 0
		self.ypos = self.surface.get_height()-60
		self.main_surface = pygame.Surface([self.width, 60])
		self.main_surface.fill([37,44,62])
		self.play_icon = pygame.image.load(os.path.join('..\\assets','play.png')).convert_alpha()
		self.skip_forward = pygame.image.load(os.path.join('..\\assets','forward.png')).convert_alpha()
		self.skip_back = pygame.transform.flip(self.skip_forward,True,False)
		self.pause = pygame.image.load(os.path.join('..\\assets','pause.png')).convert_alpha()

	def draw(self):
		# pause = 25+self.width/2....
		self.main_surface.blit(self.pause, (25+self.width/2-self.pause.get_width()/2, 60/2-self.pause.get_height()/2))
		self.main_surface.blit(self.play_icon, (-25+self.width/2-self.play_icon.get_width()/2, 60/2-self.play_icon.get_height()/2))
		self.main_surface.blit(self.skip_forward, (615.0/7+self.width/2-self.skip_forward.get_width()/2, 60/2-self.skip_forward.get_height()/2))
		self.main_surface.blit(self.skip_back, (-615.0/7+self.width/2-self.skip_back.get_width()/2, 60/2-self.skip_back.get_height()/2))
		self.surface.blit(self.main_surface, (self.xpos, self.ypos))
		