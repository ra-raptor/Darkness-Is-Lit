import pygame,random
from settings import *
vec = pygame.math.Vector2
from utility import collideHitRect, collideWithWall,Animation

class Bird(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self._layer = 5
        self.groups = game.all_sprites,game.birds
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        ''' animation Stuff'''
        self.last_updated = 0
        self.current_frame = 0
        ''' image and rect'''
        self.image = self.game.birdFly[self.current_frame]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.hit_rect = pygame.Rect(0,0,32,32)
        self.hit_rect.center = self.rect.center
        ''' movement '''
        self.position = vec(self.rect.centerx,self.rect.centery)
        self.velocity = vec(0,0)
        self.acceleration = vec(0,0)
        self.flipX = False




    def update(self):
        self.animate()
        #self.acceleration = vec(20,0)
        self.followWiz()
        self.avoidMates()
        self.acceleration.x -= self.velocity.x*BIRD_FRICTION
        self.acceleration.y -= self.velocity.y*BIRD_FRICTION
        if abs(self.acceleration.x) < 0.1:
            self.acceleration.x = 0	
            self.velocity.x /= 2
        if abs(self.acceleration.y) < 0.1:
            self.acceleration.y = 0	
            self.velocity.y /= 2
        self.velocity.x += self.acceleration.x*self.game.dt   
        self.velocity.y += self.acceleration.y*self.game.dt   
        self.position += self.velocity*self.game.dt
        self.rect.center = self.position
        self.hit_rect.center = self.position
        if self.velocity.x > 0:
            self.flipX = True
        else:
            self.flipX = False
        #self.rect.y = self.game.player.position.y -random.choice([110,112])

    def avoidMates(self):
        for mate in self.game.birds:
            if mate != self:
                distX = self.position.x-mate.position.x
                distY = self.position.y-mate.position.y
                if abs(distX) < birdAvoidRadius:
                    self.acceleration.x += distX*100
                if abs(distY) < birdAvoidRadius:
                    self.acceleration.y += distY*10
                
    def followWiz(self):
        distX =  self.position.x - self.game.player.position.x 
        distY = self.position.y - self.game.player.position.y + 150
        if abs(distX) > birdCruiseRadius:
            self.acceleration.x = -distX*random.randrange(5,10)
        if abs(distY) > birdCruiseRadius:
            self.acceleration.y = -10*distY
        
            





    def animate(self):
        if self.flipX:
            Animation(self,self.game.birdFlyFlipped)
        else:
            Animation(self,self.game.birdFly)
