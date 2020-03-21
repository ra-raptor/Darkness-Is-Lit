#Configuration for game
TITLE = "Darkness is Lit"
HEIGHT = 768
WIDTH = 1080
FPS = 60



#Colours
WHITE = (255,255,255) 
BLACK = (0,0,0) 
RED = (255,0,0) 
GREEN = (0,255,0) 
BLUE = (0,0,255)
LIGHT_BLUE = (0,155,155)
BGCOLOR = BLUE


#
GRAVITY = 80
PLAYER_ACCELERATION = 300
FRICTION = 0.6
JUMP_POWER = 800
BIRD_FRICTION = 4


#SINGLE IMAGES
IMAGES = {
    'player' : 'manBlue_gun.png',

}
#SPRITESHEET
SPRITESHEETS = {
    'wizardIdle' : 'Idle.png',
    'wizardDeath' : 'Death.png',
    'wizardFall' : 'Fall.png',
    'wizardRun' : 'Run.png',
    'wizardJump' : 'Jump.png',
    'wizardHit' : 'Hit.png',
    'wizardA1' : 'Attack1.png',
    'wizardA2' : 'Attack2.png',
    'birdFly' : 'birdman2.png'
}

birdCruiseRadius = 100
birdAcceleration = 50
birdAvoidRadius = 10
