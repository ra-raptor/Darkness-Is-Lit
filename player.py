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
		''' animation stuff '''
		self.last_updated = 0
		self.current_frame = 0
		''' state check'''
		self.isRunning = False
		self.isAttackingPrimary = False
		self.isAttackingRanged = False
		self.flipX = False
		self.isAnimationActive = False
		''' image and rect '''
		self.image = self.game.WizardIdle[self.current_frame ]
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2,HEIGHT/2)
		
	def update(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_f]:
			if not self.isAnimationActive:
				self.isAnimationActive = True
				self.isAttackingPrimary = True
				self.current_frame =0
		if keys[pygame.K_g]:
			if not self.isAnimationActive:
				self.isAnimationActive = True
				self.isAttackingRanged = True
				self.current_frame =0
		if keys[pygame.K_LEFT]:
			self.flipX = True
			self.isRunning = True
		if keys[pygame.K_RIGHT]:
			self.flipX = False
			self.isRunning = True
		
		if self.isAttackingPrimary:
			if self.flipX:
				Animation(self,self.game.WizardAttack1Flipped)
			else:
				Animation(self,self.game.WizardAttack1)
			if self.current_frame >= len(self.game.WizardAttack1)-1:
				self.isAttackingPrimary = False
				self.isAnimationActive = False
		elif self.isAttackingRanged:
			if self.flipX:
				Animation(self,self.game.WizardAttack2Flipped)
			else:
				Animation(self,self.game.WizardAttack2)
			if self.current_frame >= len(self.game.WizardAttack2)-1:
				self.isAttackingRanged = False
				self.isAnimationActive = False
		if self.isRunning:
			if self.flipX:
				Animation(self,self.game.WizardRunFlipped)
			else:
				Animation(self,self.game.WizardRun)
			self.isRunning = False
		else:
			if self.flipX:
				Animation(self,self.game.WizardIdleFlipped)
			else:
				Animation(self,self.game.WizardIdle)
		if self.flipX:
			pass
