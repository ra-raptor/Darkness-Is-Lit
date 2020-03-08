import pygame,random,math
from settings import *
from player import *
from os import path
from random import choice

#main game class
class Game:
	def __init__(self):
		pygame.init() #initiating pygame
		pygame.mixer.init() #initiating pygame music
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT)) #width,height defined in settings file
		pygame.display.set_caption(TITLE) #Title from settings file
		self.clock = pygame.time.Clock()
		self.isRunning = True #is the main game loop running?
		self.isPaused = False #is the game paused?
		self.loadData() #function to load data

	
	def loadData(self):
		''' folder structure '''
		game_folder = path.dirname(__file__) #parent folder
		asset_folder = path.join(game_folder,'assets')
		''' temporary asset folder '''
		temp_folder = path.join(asset_folder,'temp')

		''' images '''
		self.playerImg = self.ImgFromFile(temp_folder,IMAGES['player'])

		''' fonts '''
		self.testFont = pygame.font.match_font('Verdana', bold=False, italic=False)
		self.tempFont = self.FontFromFile(temp_folder,'PopulationZeroBB.otf')

		
	def FontFromFile(self,folder,file):
		return path.join(folder,file)
	
	def ImgFromFile(self,folder,name):
		return  pygame.image.load(path.join(folder,name)).convert_alpha()


	def new(self):
		''' Groups '''
		self.all_sprites = pygame.sprite.LayeredUpdates()
		self.player = Player(self)
		''' gameLoop '''
		self.run()

	def run(self):
		self.playing = True
		while  self.playing:
			self.clock.tick(FPS) #60fps limit
			self.events()
			if not self.isPaused:
				#if not paused : Update
				self.update()
			self.draw()


	def update(self):
		self.all_sprites.update()


	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				if self.playing:
					self.playing = False
				self.isRunning = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.isPaused = not self.isPaused

	def draw(self):
		self.screen.fill(WHITE)
		self.all_sprites.draw(self.screen)
		fpsTxt = "FPS-{:.2f}".format(self.clock.get_fps())
		self.drawText(fpsTxt,self.testFont,18,BLACK,10,10,'tl')
		pygame.display.flip()

	def show_start_screen(self):
		pass

	def show_GO_screen(self):
		print('GAME OVER')

	def waitForKey(self):
		pass

	def drawText(self,text,fontName,size,color,x,y,align='tl'):
		font = pygame.font.Font(fontName,size)
		text_surface = font.render(text,True,color)
		text_rect = text_surface.get_rect()
		if align == 'tl':
			text_rect.topleft = (x,y)
		if align == 'tr':
			text_rect.topright = (x,y)
		if align == 'bl':
			text_rect.bottomleft = (x,y)
		if align == 'br':
			text_rect.bottomright = (x,y)
		if align == 'mt':
			text_rect.midtop = (x,y)
		if align == 'mb':
			text_rect.midbottom = (x,y)
		if align == 'ml':
			text_rect.midleft = (x,y)
		if align == 'mr':
			text_rect.midright = (x,y)
		if align == 'c':
			text_rect.center = (x,y)
		self.screen.blit(text_surface,text_rect)

#initiation section
if( __name__ == "__main__"):
	g = Game()
	g.show_start_screen()
	while g.isRunning:
		g.new()
		g.show_GO_screen()
	pygame.quit()