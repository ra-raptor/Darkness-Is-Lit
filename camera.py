import pygame
from settings import *

class Camera:
	def __init__(self,width,height):
		self.camera = pygame.Rect(0,0,width,height)
		self.width = width
		self.height = height

	def apply(self,entity):
		return entity.rect.move(self.camera.topleft)
		
	def apply_rect(self,rect):
		return rect.move(self.camera.topleft)

	def update(self,target):
		x = -target.rect.centerx + int(WIDTH/2)
		y = -target.rect.centery + int(HEIGHT* 0.6) 
		#map restrictions
		x = min(0,x)
		y = min(0,y)
		x = max(-(self.width-WIDTH),x)
		y = max(-(self.height-HEIGHT),y)
		self.camera = pygame.Rect(x,y,self.width,self.height)
























