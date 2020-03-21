import pygame
from settings import *
from os import path 
import pytmx

class Tilemap:
    def __init__(self,filename):
        tm = pytmx.load_pygame(filename,pixelalpha=True)
        self.width = tm.width*tm.tilewidth
        self.height = tm.height*tm.tileheight
        self.tmxdata = tm

    def render(self,surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer,pytmx.TiledTileLayer):
                for x,y,gid in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile,(x*self.tmxdata.tilewidth,y*self.tmxdata.tileheight))

    def make_map(self):
        temp_surface = pygame.Surface((int(self.width),int(self.height)))
        self.render(temp_surface)
        return temp_surface
    



