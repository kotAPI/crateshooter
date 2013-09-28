##IMPORT MODULES
import pygame,os,sys
from pygame.locals import *
import random
##############################
##SET UP
##############################
color=0,120,120
black=255,255,255
red=255,0,0
blue=0,255,0
height=600
width=1200
screen=pygame.display.set_mode((width,height),0,0)


##############################
## CLASS DECL and OBJS
##############################
class Block(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
###############################
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

###############################
def reset():
    for i in range(150):
        # This represents a block
        block = Block(black, 25, 25)
    
        # Set a random location for the block
        block.rect.x = random.randrange(-300,width)
        block.rect.y = random.randrange(-3300,0)
    
        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)
###############################

###############################

reset()    
score=0
player = Block(red, 40, 40)
bullet=Block(blue,5,45)
all_sprites_list.add(player)
all_sprites_list.add(bullet)
bullet_y=560
i=1
score=1
#############
pygame.init()
t=0
u=0
lives=3
###############
###MAIN LOOP###
while 1:
    i=i+30
    screen.fill(color)
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==KEYDOWN and event.key==K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif event.type==MOUSEBUTTONDOWN:
            t,u = pygame.mouse.get_pos()
            bullet_y=560
            i=1
            
    
    bullet.rect.x=t
    bullet.rect.y=bullet_y-i
        
    
    # Fetch the x and y out of the list, 
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    ##
    
    ##
    a,b = pygame.mouse.get_pos()
    player.rect.x=a-20
    player.rect.y=560
    ##
    for block in block_list:
        block.rect.y+=1
        if block.rect.y==600:
            block.rect.y=random.randrange(-800,-50)
            
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
    blocks_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
    
     
    # Check the list of collisions.
    for block in blocks_hit_list:
        score +=1
        
         
    # Draw all the spites
    all_sprites_list.draw(screen)
     
    # Limit to 20 frames per second
    #clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    
    pygame.display.flip()
    pygame.display.update()
## END OF MAIN LOOP
