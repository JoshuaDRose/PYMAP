import pygame
from button import Button

class TextBox(pygame.sprite.Sprite):
	def __init__(self, pos, size, title, description):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(size)
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]
		self.image.fill([200, 200, 200])
		self.description = description
		self.lines = self.description.count('\n')
		self.to_render = self.description.split('\n', self.lines) 
		self.max_chars_per_line = 50
		self.button_sprites = pygame.sprite.Group()
		self.button_affirm_color = [0, 200, 0]
		self.button_decline_color = [200, 0, 0]
		# =========================== #
		# ---------- FONTS ---------- #
		# =========================== #
		self.fontsize = 28
		self.face = pygame.font.get_default_font()
		self.font_title = pygame.font.SysFont(self.face, 32)
		self.title_text = self.font_title.render(title, 1, [0, 0, 0])
		self.desc_text = []
		for line in self.to_render:
			if len(line) > self.max_chars_per_line:
				lines_over = len(line) - self.max_chars_per_line
				for i in range(0, lines_over, 2):
					self.fontsize -= 2
				self.font_desc = pygame.font.SysFont(self.face, self.fontsize)
				self.desc_text.append(self.font_desc.render(line, 1, [0, 0, 0]))
			else:
				self.fontsize = 28
				self.font_desc = pygame.font.SysFont(self.face, self.fontsize)
				self.desc_text.append(self.font_desc.render(line, 1, [0, 0, 0]))
			

		# =========================== #
		# -------- HEADER ----------- #
		# =========================== #
		self.header_bar = pygame.Surface([size[0], 25])
		self.header_rect = self.header_bar.get_rect()
		self.header_rect.x = 0
		self.header_rect.y = 0
		self.header_bar.fill((140, 140, 140))
		self.header_bar.blit(self.title_text, [self.header_rect.width / 2 - self.font_title.size(title)[0] / 2,3])
		self.image.blit(self.header_bar, self.header_rect)

		# ============================= #
		# -------- MAIN SECTION ------- #
		# ============================= #
		height = 0
		for POSITION, RENDERED_TEXT in enumerate(self.desc_text):
			middle = self.rect.height / 2
			text_height = self.font_desc.size(self.to_render[POSITION])[1] / 2
			self.image.blit(RENDERED_TEXT, [self.rect.width / 2-self.font_desc.size(self.to_render[POSITION])[0] / 2,middle + text_height + height])
			height += self.font_desc.size(self.to_render[POSITION])[1]

		self.button_affirm = Button([self.rect.width - 100, self.rect.height - 50], [25, 25], self.button_affirm_color, (0, 255, 0), tick=True)
		self.button_decline = Button(100, self.rect.height - 50], [25, 25],self.button_decline_color, (255, 0, 0), cross=True)

		self.button_sprites.add(self.button_affirm)
		self.button_sprites.add(self.button_decline)

	def update(self):
		self.button_sprites.update()
		self.button_sprites.draw(self.image)
