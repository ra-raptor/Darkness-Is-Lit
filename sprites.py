import pygame
from settings import *
vec = pygame.math.Vector2
import random

''' Player class '''
class Player(pygame.sprite.Sprite):
	def __init__(self,game):
		self.image = pygame.surface((WIDTH/2,HEIGHT/2),RED)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2,HEIGHT/2)

	def update(self):
		pass