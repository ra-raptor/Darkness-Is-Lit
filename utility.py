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

