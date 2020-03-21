import pygame,random,math
from settings import *
from player import *
from camera import *
from walls import *
from tilemap import *
from os import path
from bird import *
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
		self.birdFly = [Spritesheet(self.temp_folder,SPRITESHEETS['birdFly'],(1,8)).extractImg((1,i)) for i in range(1,9)]
		self.birdFlyFlipped = FlipImage(self.birdFly)
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

		''' map '''
		self.map = Tilemap(path.join(asset_folder,'hey.tmx'))
		self.map_img = self.map.make_map()
		self.map_rect = self.map_img.get_rect()



	def new(self):
		''' Groups '''
		self.all_sprites = pygame.sprite.LayeredUpdates()
		self.walls = pygame.sprite.Group()                        
		self.birds = pygame.sprite.Group()                        
		for tile_object in self.map.tmxdata.objects:
			if tile_object.name == "Wall":
				Wall(self,tile_object.x,tile_object.y,tile_object.width,tile_object.height)
			if tile_object.name == "Player":
				self.player = Player(self,tile_object.x,tile_object.y)
			if tile_object.name == "Bird":
				Bird(self,tile_object.x,tile_object.y)


		
		self.camera = Camera(self.map.width,self.map.height)
		''' gameLoop '''
		self.run()

	def run(self):
		self.playing = True
		while  self.playing:
			self.clock.tick(FPS) #60fps limit
			self.dt = self.clock.tick(FPS)/1000
			self.events()
			if not self.isPaused:
				#if not paused : Update
				self.update()
			self.draw()

	def update(self):
		
		self.all_sprites.update()
		self.camera.update(self.player)
		#hits = pygame.sprite.spritecollide(self.player,self.walls,False)
		#if hits:
		#	for hit in hits:
		#		if self.player.position.y > hit.rect.bottom:
		#			self.player.position.y = hit.rect.top
		#			self.player.velocity.y = 0

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
		self.screen.blit(self.map_img,self.camera.apply_rect(self.map_rect))
		#self.all_sprites.draw(self.screen)
		fpsTxt = "FPS-{:.2f}".format(self.clock.get_fps())
		for sprite in self.all_sprites:
			self.screen.blit(sprite.image,self.camera.apply(sprite))
			#pygame.draw.rect(self.screen,RED,self.camera.apply_rect(sprite.hit_rect),3)
		#self.drawText(fpsTxt,self.testFont,18,BLACK,10,10,'tl')
		for wall in self.walls:
			pass
			#pygame.draw.rect(self.screen,RED,self.camera.apply_rect(wall.rect),3)
		Text(self.screen,fpsTxt,self.testFont,18,WHITE,10,10,'tl')
		pygame.display.flip()

	def show_start_screen(self):
		while True:
			self.clock.tick(FPS)
			self.screen.fill((0,0,0))
			Text(self.screen,'fpsTxt',self.testFont,18,RED,10,10,'tl')
			
			pygame.display.flip()

	def show_GO_screen(self):
		pass

#initiation section
if( __name__ == "__main__"):
	g = Game()
	#g.show_start_screen()
	while g.isRunning:
		g.new()
		g.show_GO_screen()
	pygame.quit()
	