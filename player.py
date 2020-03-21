import pygame,random,math,time
from settings import *
vec = pygame.math.Vector2
from utility import *

''' Player class '''
class Player(pygame.sprite.Sprite):
    
	def __init__(self,game,x,y):
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
		self.isJumping = False
		self.flipX = False
		self.isAnimationActive = False
		''' image and rect '''
		self.image = self.game.WizardIdle[self.current_frame ]
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)
		self.hit_rect = pygame.Rect(0,0,40,90)
		self.hit_rect.center = self.rect.center

		''' movement '''
		self.position = self.rect.center
		self.velocity = vec(0,0)
		self.acceleration = vec(0,0)
		
	def update(self):
		''' key press handling '''
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
		if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not self.isAttackingPrimary and not self.isAttackingRanged:
			self.flipX = True
			self.isRunning = True
		if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not self.isAttackingPrimary and not self.isAttackingRanged:
			self.flipX = False
			self.isRunning = True
		if keys[pygame.K_SPACE]:
			self.jump()
			self.isJumping = True



		self.animate()
		self.movement()
		'''movement handling '''
		
		if abs(self.velocity.x) < 0.1:
			self.velocity.x = 0
		if abs(self.velocity.y) < 0.1:
			self.velocity.y = 0
		self.velocity += self.acceleration
		self.position += self.velocity*self.game.dt
		self.rect.center = self.position

		''' wall collision '''
		self.hit_rect.centerx = self.position.x
		collideWithWall(self,self.game.walls,'x')
		self.hit_rect.centery = self.position.y
		collideWithWall(self,self.game.walls,'y')
		self.rect.center = self.hit_rect.center


		
		
	def jump(self):
		'''
		self.rect.y += 1
		hits = pygame.sprite.spritecollide(self,self.game.platforms,False)
		self.rect.y -= 1
		if hits:
		'''	
		self.velocity.y = -JUMP_POWER
		
		
		

	def movement(self):
		self.acceleration = vec(0,GRAVITY)


		keys = pygame.key.get_pressed()
		if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not self.isAttackingPrimary and not self.isAttackingRanged:
			self.acceleration.x = -PLAYER_ACCELERATION
		if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not self.isAttackingPrimary and not self.isAttackingRanged:
			self.acceleration.x = PLAYER_ACCELERATION
		
		self.acceleration.x -= self.velocity.x*FRICTION
		if abs(self.acceleration.x) < 0.1:
			self.acceleration.x = 0	
			self.velocity.x /= 2
		
		if self.isJumping:
			if self.velocity.y > 0:
				hits = pygame.sprite.spritecollide(self.game.player,self.game.walls,False)
				if hits:
					self.isJumping = False
					self.isRunning = True
		
	
	def animate(self):
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
		elif self.isJumping:
			if self.flipX:
				if self.velocity.y < 0:
					Animation(self,self.game.WizardJumpFlipped)
				else:
					Animation(self,self.game.WizardFallFlipped)
			else:
				if self.velocity.y > 0:
					Animation(self,self.game.WizardFall)
				else:
					Animation(self,self.game.WizardJump)
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


