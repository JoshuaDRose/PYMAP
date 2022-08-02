""" main.py contains main - executes main loop """
from window import *
from utils import *
from player import *

import pygame
import requests
import threading
import console


__all__ = ["__main__"]

console_thread = threading.Thread(target=console.do_console, args=())
console_thread.daemon = True
console_thread.start()

player = Player()
window = Window()

def main():
	window.main_loop()

if __name__ == "__main__":
	main()
	
