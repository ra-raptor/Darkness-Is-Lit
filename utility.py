import pygame
from settings import * 
from os import path 

class Spritesheet:
    def __init__(self,folder,file,dimention = (1,1)):
        self.pathToImg = path.join(folder,file)
        self.spritesheet = pygame.image.load(self.pathToImg)
        self.width,self.height = self.spritesheet.get_size()
        self.rowCount,self.columnCount = dimention
        self.singleHeight = int(self.height/self.rowCount)
        self.singleWidth = int(self.width/self.columnCount)

    def extractImg(self,pos=(1,1)):
        self.xIndex,self.yIndex = pos
        image = pygame.Surface((self.singleWidth,self.singleHeight))
        image.blit(self.spritesheet,(0,0),(self.singleWidth*(self.yIndex-1),self.singleHeight*(self.xIndex-1),self.singleWidth,self.singleHeight))
        return image

def LoadResourceFromFile(folder,file,type='image'):
    pathToFile = path.join(folder,file)
    if type == "image":
        return (pygame.image.load(pathToFile).convert_alpha())	
    if type == "font":
        return pathToFile

def Animation(object,frames):
    now = pygame.time.get_ticks()
    if now - object.last_updated > 100:
        object.last_updated = now
        object.current_frame = (object.current_frame+1) % len(frames)
        center = object.rect.center
        object.image = frames[object.current_frame]
        object.image.set_colorkey(BLACK)
        object.rect = object.image.get_rect()
        object.rect.center = center

def Text(surface,text,font,size,colour,x,y,align='tl'):
    font = pygame.font.Font(font,size)
    text_surface = font.render(text,True,colour)
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
    surface.blit(text_surface,text_rect)

def FlipImage(set):
    flipped = []
    for i in set:
        Img = pygame.transform.flip(i,True,False)
        flipped.append(Img)
    return flipped