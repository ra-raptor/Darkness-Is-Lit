import pygame,random,math
from settings import *
from player import *
from os import path
from random import choice
from utility import *

#main game class
class Game:
	def __init__(self):
		pygame.init() #initiating pygame
		pygame.mixer.init() #initiating pygame music
		self.MonitorDimentions = [pygame.display.Info().current_w,pygame.display.Info().current_h]
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE) #width,height defined in settings file
		pygame.display.set_caption(TITLE) #Title from settings file
		self.clock = pygame.time.Clock() #game clock
		self.isRunning = True #is the main game loop running?
		self.isPaused = False #is the game paused?
		self.isFullScreen = False #is the window Fullscreen?
		self.loadData() #function to load data

	def loadData(self):
		''' folder structure '''
		game_folder = path.dirname(__file__) #parent folder
		asset_folder = path.join(game_folder,'assets') #assets folder
		self.temp_folder = path.join(asset_folder,'temp') #temporary folder
		self.wizard_folder = path.join(self.temp_folder,'wizard') #wizard folder

		''' images '''
		self.playerImg = LoadResourceFromFile(self.temp_folder,IMAGES['player'],'image')
		#self.wizardImg = Spritesheet(self.temp_folder,SPRITESHEETS['wizardIdle'],(1,6)).extractImg((1,5))
		self.WizardIdle = [Spritesheet(self.wizard_folder,SPRITESHEETS['wizardIdle'],(1,6)).extractImg((1,i)) for i in range(1,7)]
		self.WizardDeath = [Spritesheet(self.wizard_folder,SPRITESHEETS['wizardDeath'],(1,7)).extractImg((1,i)) for i in range(1,8)]
		self.WizardRun = [Spritesheet(self.wizard_folder,SPRITESHEETS['wizardRun'],(1,8)).extractImg((1,i)) for i in range(1,9)]
		self.WizardJump = [Spritesheet(self.wizard_folder,SPRITESHEETS['wizardJump'],(1,2)).extractImg((1,i)) for i in range(1,3)]
		self.WizardFall = [Spritesheet(self.wizard_folder,SPRITESHEETS['wizardFall'],(1,2)).extractImg((1,i)) for i in range(1,3)]
		self.WizardHit = [Spritesheet(self.wizard_folder,SPRITESHEETS['wizardHit'],(1,4)).extractImg((1,i)) for i in range(1,5)]
		self.WizardAttack1 = [Spritesheet(self.wizard_folder,SPRITESHEETS['wizardA1'],(1,8)).extractImg((1,i)) for i in range(1,9)]
		self.WizardAttack2 = [Spritesheet(self.wizard_folder,SPRITESHEETS['wizardA2'],(1,8)).extractImg((1,i)) for i in range(1,9)]
		self.WizardIdleFlipped = FlipImage(self.WizardIdle)
		self.WizardDeathFlipped = FlipImage(self.WizardDeath)
		self.WizardRunFlipped = FlipImage(self.WizardRun)
		self.WizardJumpFlipped = FlipImage(self.WizardJump)
		self.WizardFallFlipped = FlipImage(self.WizardFall)
		self.WizardHitFlipped = FlipImage(self.WizardHit)
		self.WizardAttack1Flipped = FlipImage(self.WizardAttack1)
		self.WizardAttack2Flipped = FlipImage(self.WizardAttack2) 
		

		''' fonts '''
		self.testFont = pygame.font.match_font('Verdana', bold=False, italic=False)
		self.tempFont = LoadResourceFromFile(self.temp_folder,'PopulationZeroBB.otf','font')

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
			if event.type == pygame.VIDEORESIZE: #handles resizing of pygame window
				if not self.isFullScreen:
					self.screen = pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE) #sets screen size to new window size
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.isPaused = not self.isPaused
				if event.key == pygame.K_F11:
					self.isFullScreen = not self.isFullScreen
					if self.isFullScreen:
						self.screen = pygame.display.set_mode(self.MonitorDimentions,pygame.FULLSCREEN)
					else:
						self.screen = pygame.display.set_mode((self.screen.get_width(),self.screen.get_height()),pygame.RESIZABLE)

	def draw(self):
		self.screen.fill(WHITE)
		self.all_sprites.draw(self.screen)
		fpsTxt = "FPS-{:.2f}".format(self.clock.get_fps())
		#self.drawText(fpsTxt,self.testFont,18,BLACK,10,10,'tl')
		Text(self.screen,fpsTxt,self.testFont,18,BLACK,10,10,'tl')
		pygame.display.flip()

	def show_start_screen(self):
		pass

	def show_GO_screen(self):
		pass

#initiation section
if( __name__ == "__main__"):
	g = Game()
	g.show_start_screen()
	while g.isRunning:
		g.new()
		g.show_GO_screen()
	pygame.quit()