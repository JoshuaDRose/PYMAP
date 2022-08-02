import os
import sys
import utils
import pygame
import tkinter
import sidebar
import statusbar
import threading
import player_gui
import tkinter.filedialog
from button import Button
from textbox import TextBox
from pygame.locals import *

class Window():
	def __init__(self):
		pygame.font.init()
		self.settings = utils.load_settings(os.path.join('../meta', 'settings.json'))
		self.running = True
		self.display = pygame.display.set_mode([1280, 720], pygame.SHOWN | pygame.NOFRAME, 32)
		self.dw, self.dh = self.display.get_size()
		self.clock = pygame.time.Clock()
		self.bg_color = (23, 27, 36)
		self.toolbar_icon_group = pygame.sprite.Group()
		self.draw_toolbar_icons()
		self.preview_popup = pygame.sprite.GroupSingle()
		self.tb_w,self.tb_h = 450, 250
		self.install_wizard_page = 0
		self.main_program_font = pygame.font.SysFont('candara', 24, bold=True)
		self.program_h1_title_text = self.main_program_font.render("PyMap", 1, (255, 255,255))
		self.image = pygame.image.load(os.path.join('../assets', 'program_icon.png')).convert()
		self.image = pygame.transform.scale(self.image, (25, 25))
		self.image.set_colorkey([255, 255, 255])
		self.install_surf = statusbar.StatusBar([self.tb_w, 40], [50, 50])
		self.sidebar = sidebar.Sidebar()
		self.player_window = player_gui.Player(self.display)
		if not self.settings['download_box_shown']:
			self.install_folder = os.path.normpath(os.path.join(os.environ['USERPROFILE'],'music'))
			self.install_wizard_page = 1			
			self.preview_popup.add(TextBox([self.dw / 2 - self.tb_w / 2, self.dh / 2 - self.tb_h / 2], [self.tb_w, self.tb_h], "Install Wizard", "Would you like to install a default song library?"))
		else:
			self.install_folder = self.settings['install_folder']
		self.confirm_done = False

		# --- player --- #
		self.current_song = None
		self.showing_no_song_queued = False

	def folder_browser(self):
		""" https://stackoverflow.com/questions/63801960/ """
		r = tkinter.Tk()
		r.withdraw()  
		folder_name = tkinter.filedialog.askdirectory(initialdir=self.install_folder, parent=r)
		r.destroy()
		self.install_folder = folder_name
		self.settings['install_folder'] = folder_name

	def clear_popup(self):
		for i in self.preview_popup:
			self.preview_popup.remove(i)

	def file_browser(self):
		""" https://stackoverflow.com/questions/63801960/ """
		r = tkinter.Tk()
		r.withdraw()  # hide window
		file_name = tkinter.filedialog.askopenfilename(initialdir=self.install_folder, parent=r)
		r.destroy()
		self.song_queued = True
		self.current_song = pygame.mixer.Sound(file_name)
		print(self.current_song)

	def draw_toolbar(self):
		pygame.draw.rect(self.display, (33, 41, 54), (0, 0, self.dw, 25))
		self.display.blit(self.image, (2, 0))
		self.display.blit(self.program_h1_title_text, (36, 2))

	def draw_toolbar_icons(self):
		""" draws exit, windowed, minimize """
		x_pos = self.dw
		
		colors = [[255, 0, 0],[0, 255, 0],[0, 0, 255]]
		for i in range(3):
			x_pos -= 25
			button = Button([x_pos, 0], [25, 25], (200, 0, 0),(255, 0, 0))
			button.image.fill(colors[i])
			if i == 0:
				button = Button([x_pos, 0], [25, 25], (200, 0, 0),(255, 0, 0))
			
			self.toolbar_icon_group.add(button)

	def main_loop(self):
		while self.running:
			self.display.fill(self.bg_color)
			mp = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type == QUIT:
					utils.save_settings(os.path.join('../meta', 'settings.json'), self.settings)
					self.running = False
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						utils.save_settings(os.path.join('../meta', 'settings.json'), self.settings)
						self.running = False

				if event.type == MOUSEBUTTONDOWN:
					# --- detect if play pressed --- #
					if self.install_wizard_page == 0:
						# --- if mouse on play butotn --- #
						if mp[0] in range(605, 625) and mp[1] in range(675, 705):
							if not self.current_song:
								self.showing_no_song_queued = True
								self.preview_popup.add(TextBox([self.dw / 2 - self.tb_w / 2, self.dh / 2 - self.tb_h / 2], [self.tb_w, self.tb_h], "Music Player", "No song queued."))
								for i in self.preview_popup:
									for j in i.button_sprites:
										if j.color[0] > 1:
											j.visible = False
										if j.color[1] > 1:
											j.rect.x = i.rect.width / 2 - j.rect.width / 2
								
						# print(mp)
						# --- PLAY BUTTON --- #
						if mp[0] in range(600, 628) and mp[1] in range(669, 706):
							if not pygame.mixer.get_busy():
								print("PLAYIYNG ")
								self.clear_popup()
								self.file_browser()
								pygame.mixer.Channel(0).play(self.current_song)
							else:
								pygame.mixer.Channel(0).unpause()
							
						# PAUSE BUTTON #
						if mp[0] in range(648, 683) and mp[1] in range(670, 706):
							print("PAUSING")
							pygame.mixer.Channel(0).pause()

					if not self.settings['download_box_shown']:
						if mp[0] in range(515, 540) and mp[1] in range(435, 460):
							if self.install_wizard_page == 2:
								self.clear_popup()
							elif self.install_wizard_page == 1:
								self.clear_popup()
								self.install_wizard_page = 0
						elif mp[0] in range(765, 790) and mp[1] in range(435, 460):
							if self.install_wizard_page == 1:
								self.install_wizard_page += 1
								self.preview_popup.add(TextBox([self.dw / 2 - self.tb_w / 2, self.dh / 2 - self.tb_h / 2], [self.tb_w, self.tb_h], "Install Wizard", f"{self.install_folder}\nChoose different install location?"))

							if self.install_wizard_page == 2:
								self.folder_browser()
								self.clear_popup()
								self.preview_popup.add(TextBox([self.dw / 2 - self.tb_w / 2, self.dh / 2 - self.tb_h / 2], [self.tb_w,self.tb_h], "Install Wizard", "Installing Sample Library"))
								for sprite in self.preview_popup:
									for button in sprite.button_sprites:
										button.visible = False
								install_thread = threading.Thread(target=utils.install_samples, args=(os.path.join('../meta', 'default.json'), self.install_folder))
								install_thread.daemon = True
								install_thread.start()
								self.clear_popup()
						elif mp[0] in range(625, 665) and mp[1] in range(420, 460):
							if self.install_wizard_page == 3:
								self.clear_popup()
								self.install_wizard_page = 0
							
				if event.type == MOUSEMOTION:
					if self.showing_no_song_queued:
						if mp[0] in range(625, 665) and mp[1] in range(420, 460):
							for popup in self.preview_popup:
								for button in popup.button_sprites:
									if button.color[1] > 1:
										button.hovering = True
									else:
										button.hovering = False
						else:
							for popup in self.preview_popup:
								for button in popup.button_sprites:
									button.hovering = False

					if self.install_wizard_page == 3:
						if mp[0] in range(625, 665) and mp[1] in range(420, 460):
							for popup in self.preview_popup:
								for button in popup.button_sprites:
									if button.color[1] > 1:
										button.hovering = True
									else:
										button.hovering = False
						else:
							for popup in self.preview_popup:
								for button in popup.button_sprites:
									button.hovering = False
					if self.install_wizard_page != 0 and self.install_wizard_page < 3:
						if mp[0] in range(515, 540) and mp[1] in range(435, 460):
							for popup in self.preview_popup:
								for button in popup.button_sprites:
									if button.color[0] > 1:
										button.hovering = True
									else:
										button.hovering = False
						elif mp[0] in range(765, 790) and mp[1] in range(435, 460): 
							for popup in self.preview_popup:
								for button in popup.button_sprites:
									if button.color[1] > 1:
										button.hovering = True
									else:
										button.hovering = False
						else:
							for popup in self.preview_popup:
								for button in popup.button_sprites:
									button.hovering = False

			# --- run update on each sprite group --- #
			if self.install_wizard_page == 2:
				if utils.done:
					self.install_wizard_page = 3
			if self.install_wizard_page == 3:
				if not self.confirm_done:
					# print("Finished installation process.")
					self.clear_popup()
					self.preview_popup.add(TextBox([self.dw / 2 - self.tb_w / 2, self.dh / 2 - self.tb_h / 2], [self.tb_w, self.tb_h], "Install Wizard", "Done!"))
					for i in self.preview_popup:
						for j in i.button_sprites:
							if j.color[0] > 1:
								j.visible = False
							if j.color[1] > 1:
								j.rect.x = i.rect.width / 2 - j.rect.width / 2
					self.confirm_done = True 
			self.toolbar_icon_group.update()
			self.preview_popup.update()
			# --- main player ---- #
			if self.install_wizard_page == 0:
				# self.sidebar.draw(self.display)
				self.display.fill([15, 18, 25])
				self.player_window.draw()
			self.draw_toolbar()
			self.toolbar_icon_group.draw(self.display)
			self.preview_popup.draw(self.display)
			self.player_window.draw()

			pygame.display.update()
			self.clock.tick(60)
		pygame.quit()
		sys.exit()
		
