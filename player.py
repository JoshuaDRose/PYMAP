import os
import sys
import pygame
import utils
import glob

from threading import *

class Player():

	def __init__(self):
		pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
		pygame.mixer.init()
		self.song_index = 0
		self.volume = 1
		self.shuffle = False
		self.crossfade = False
		self.song_list = utils.scan_dir(os.path.join('../meta','songs'))
		self.song_channel = pygame.mixer.Channel(0)
		self.song_channel.set_volume(self.volume)
		self.songs = self.load_songs()

	def load_songs(self):
		song_directory = os.path.join(os.getcwd(), '../songs/*') 
		return [i for i in glob.glob(song_directory)]
