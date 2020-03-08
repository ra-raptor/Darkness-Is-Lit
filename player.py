import pygame,random,math
from settings import *
vec = pygame.math.Vector2

''' Player class '''
class Player(pygame.sprite.Sprite):
    
	def __init__(self,game):
		self._layer = 2
		self.groups = game.all_sprites
		pygame.sprite.Sprite.__init__(self,self.groups)
		self.game = game
		self.image = self.game.playerImg
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2,HEIGHT/2)


	def update(self):
		pass