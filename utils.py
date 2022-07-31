""" Basic functions for assisting with song and data loading """
import os
import glob
import json
import pygame
import install

progress = 0
done = False
def load_settings(file) -> dict:
	# print(f'loading settings to {file}')
	data = {}
	with open(file) as f:
		data = json.load(f)
		f.close()
	return data

def save_settings(file, settings):
	# print(f'Saving settings to {file}')
	with open(file, 'w') as f:
		json.dump(settings, f)

def scan_dir(directory) -> list:
	# print(f'scanning {directory}')
	located_files = []
	for file in glob.glob(directory):
		located_files.append(file)
	return located_files

def get_display_size() -> list:
	""" update: not implemented as it messes with display """
	screen = pygame.display.set_mode()
	x, y = screen.get_size()
	del screen 
	return [x,y]

def install_samples(file, directory):
	""" file: json file
	directory: directory to install to 
	"""
	# print(f"Installing {file} to {directory}")
	global progress
	global done
	data = {}
	with open(file) as f:
		data = json.load(f)
		f.close()
	for i in data.keys():
		install.wget_samples(directory, data[i]['wget'], data[i]['filename'])
	done = True

def data_size(file):
	""" Get the amount of install sameple songs for the progress bar """
	data = {}
	# print(f"Getting data size of {file}")
	songs = []
	with open(file) as f:
		data = json.load(f)
		f.close()
	for i in data.keys():
		songs.append(data[i])
	return len(songs)