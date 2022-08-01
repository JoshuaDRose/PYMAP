""" main.py contains main - executes main loop """
from window import *
from utils import *
from player import *

import pygame
import requests
import threading
import console

console_thread = threading.Thread(target=console.do_console, args=())
console_thread.daemon = True
console_thread.start()

player = Player()
window = Window()

def main():
	""" Run event loop in window """
	window.main_loop()

if __name__ == "__main__":
	main()
	
