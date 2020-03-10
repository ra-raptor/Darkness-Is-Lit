import pygame,random,math,time
from settings import *
vec = pygame.math.Vector2
from utility import *

''' Player class '''
class Player(pygame.sprite.Sprite):
    
	def __init__(self,game):
		self._layer = 2
		self.groups = game.all_sprites
		pygame.sprite.Sprite.__init__(self,self.groups)
		self.game = game
		self.loadImages()
		''' animation stuff '''
		self.last_updated = 0
		self.current_frame = 0
		''' state check'''
		self.isRunning = False
		self.isAttacking = False
		''' image and rect '''
		self.image = self.Idle[self.current_frame ]
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2,HEIGHT/2)
		


	def update(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			self.isRunning = True
		if keys[pygame.K_TAB]:
			self.isAttacking = True
			self.current_frame =0
		
		if self.isAttacking:
			
			self.AttackA()
			if self.current_frame >= len(self.Attack1)-1:
				self.isAttacking = False
		else:
			self.playAnimation()
		
	
	def AttackA(self):
		now = pygame.time.get_ticks()
		if now - self.last_updated > 100:
			self.last_updated = now
			self.current_frame = (self.current_frame+1) % len(self.Attack1)
			self.center = self.rect.center
			self.image = self.Attack1[self.current_frame]
			self.image.set_colorkey(BLACK)
			self.rect = self.image.get_rect()
			self.rect.center = self.center

	def playAnimation(self):
		now = pygame.time.get_ticks()
		if self.isRunning:
			if now - self.last_updated > 100:
				self.last_updated = now
				self.current_frame = (self.current_frame+1) % len(self.Run)
				self.center = self.rect.center
				self.image = self.Run[self.current_frame]
				self.image.set_colorkey(BLACK)
				self.rect = self.image.get_rect()
				self.rect.center = self.center
				self.isRunning = False
		if not self.isRunning and not self.isAttacking:
			if now - self.last_updated > 100:
				self.last_updated = now
				self.current_frame = (self.current_frame+1) % len(self.Idle)
				self.center = self.rect.center
				self.image = self.Idle[self.current_frame]
				self.image.set_colorkey(BLACK)
				self.rect = self.image.get_rect()
				self.rect.center = self.center
				

	def loadImages(self):
		''' wizard '''
		self.Idle = [Spritesheet(self.game.wizard_folder,SPRITESHEETS['wizardIdle'],(1,6)).extractImg((1,i)) for i in range(1,7)]
		self.Death = [Spritesheet(self.game.wizard_folder,SPRITESHEETS['wizardDeath'],(1,7)).extractImg((1,i)) for i in range(1,8)]
		self.Run = [Spritesheet(self.game.wizard_folder,SPRITESHEETS['wizardRun'],(1,8)).extractImg((1,i)) for i in range(1,9)]
		self.Jump = [Spritesheet(self.game.wizard_folder,SPRITESHEETS['wizardJump'],(1,2)).extractImg((1,i)) for i in range(1,3)]
		self.Fall = [Spritesheet(self.game.wizard_folder,SPRITESHEETS['wizardFall'],(1,2)).extractImg((1,i)) for i in range(1,3)]
		self.Hit = [Spritesheet(self.game.wizard_folder,SPRITESHEETS['wizardHit'],(1,4)).extractImg((1,i)) for i in range(1,5)]
		self.Attack1 = [Spritesheet(self.game.wizard_folder,SPRITESHEETS['wizardA1'],(1,8)).extractImg((1,i)) for i in range(1,9)]
		self.Attack2 = [Spritesheet(self.game.wizard_folder,SPRITESHEETS['wizardA2'],(1,8)).extractImg((1,i)) for i in range(1,9)]


