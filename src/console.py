import pygame
import sys

""" Debug commands and such """
def do_console():
	while True:
		x = input("DEBUG >> ")
		if x == 'quit_debug':
			print("Exiting debug console")
		elif x == 'quit':
			print("exiting.")
			pygame.quit()
			sys.exit(0)
			
		elif x == 'exit':
			pygame.quit()
			sys.exit(0)
			
		elif x == 'help':
			print('''quit: Exit the program
quit_debug: exit the debug console
exit: Exit all tasks
kill_thread: kill a thread <proc. id needed>
help: display help menu (help <cmd>)''')
