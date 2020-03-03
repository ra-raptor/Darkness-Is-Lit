import pygame
import random
from settings import *
from sprites import *
from os import path



#hey this is me
class Game:
	def __init__(self):
		pygame.init()
		pygame.mixer.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()
		self.running = True
		self.basic_font = pygame.font.match_font(FONT_BASIC)

	def new(self):
		self.all_sprites = pygame.sprite.LayeredUpdates()
		self.player = Player(self)
		''' gameLoop '''
		self.run()

	def run(self):
		self.playing = True
		while  self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()

	def update(self):
		self.all_sprites.update()

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				if self.playing:
					self.playing = False
				self.running = False

	def draw(self):
		self.screen.fill(BGCOLOR)
		self.all_sprites.draw(self.screen)
		pygame.display.flip()

	def show_start_screen(self):
		print("Hello")

	def show_GO_screen(self):
		print('GAME OVER')

	def waitForKey(self):
		pass

	def drawText(self):
		font = pygame.font.Font(self.basic_font,size)
		text_surface = font.render(text,True,color)
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x,y)
		self.screen.blit(text_surface,text_rect)

g = Game()
g.show_start_screen()
while g.running:
	g.new()
	g.show_GO_screen()
pygame.quit()

