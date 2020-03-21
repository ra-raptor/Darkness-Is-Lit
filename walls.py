import pygame
from settings import *
vec = pygame.math.Vector2
import random

class Wall(pygame.sprite.Sprite):
	def __init__(self,game,x,y,w,h):
		self._layer = 5
		self.groups = game.walls
		pygame.sprite.Sprite.__init__(self,self.groups)
		self.game = game
		self.rect = pygame.Rect(x,y,w,h)
		self.rect.center = (x,y)
		self.x = x
		self.y = y
		self.rect.x = x
		self.rect.y = y







