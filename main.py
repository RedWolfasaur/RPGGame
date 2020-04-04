import sys
import pygame
import classSelection

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

class image:
        player=pygame.image.load('Images/Knight.png').convert_alpha()
        outerCastle=pygame.image.load('Images/FrontCastle.png').convert()
        innerCastle=pygame.image.load('Images/innerCastle.png').convert()
        knight=pygame.image.load('Images/Knight.png').convert_alpha()
        knightAttack=pygame.image.load('Images/KnightAttack.png').convert_alpha()
        archer=pygame.image.load('Images/Archer.png').convert_alpha()
        archerReadybow=pygame.image.load('Images/Archer-1.png').convert_alpha()
        ArcherAttack=pygame.image.load('Images/Archer-2.png').convert_alpha()
        arrow=pygame.image.load('Images/arrow.png').convert_alpha()
        slime=pygame.image.load('Images/Slime.png').convert_alpha()
        spider=pygame.image.load('Images/Spider.png').convert_alpha()
        
'''
weaponBonus has three types attack (1), speed (2), health (3)
attackBonus is divided by two added to base attack
defense is divided by 5, rounded, and subtracted from the damage dealt
'''

class stats:
        loadout='Knight'
        health=100
        maxHealth=100
        weapon='Sword'
        weaponBonusType=1
        weaponBonusAdd=5
        baseAttack=10
        baseDefense=10

playerClass=classSelection.classSelection() #Main Menu

if playerClass==1:
        stats.loadout='Archer'
        stats.health=100
        stats.maxHealth=100
        stats.weapon='Bow'
        stats.weaponBonusType=1
        stats.weaponBonusAdd=5
        stats.baseAttack=15
        stats.baseDefense=5
        image.player='Images/Archer.png'
        
class background:
        image = image.outerCastle
        
        def refresh():
                screen.blit(pygame.transform.scale(image.outerCastle,(800,600)),[0,0,800,600])
                player.update()
                pygame.display.flip()

class x:
        location = 10
        velocity = 0
        maxSpeed = 20
        

class y:
        location=500
        velocity=0

class player(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = image.player
                x.location = 10
                y.location = 600-self.image.get_height()
                self.rect = self.image.get_rect()
                print(self.image.get_rect())
                self.rect.topleft = [x.location,y.location]
                
        def update(self):
                self.rect.topleft = [x.location,y.location]
                screen.blit(player.image,player.rect)
        
                

screen = pygame.display.set_mode([800,600])


player=player()
all_sprites.add(player)

all_sprites.draw(screen)

running = True
moveLeft = False
while running:
        clock.tick(40)
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                                moveLeft = True                                
                                
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_d:
                                moveLeft = False
                                print('d')
                                
                                
                if event.type == pygame.QUIT:
                        running = False
                        
        if moveLeft:
                pygame.time.delay(10)
                x.velocity+=5
                x.location+=4

                
        print(x.location)
                
        background.refresh()
                
                        

print('why')
pygame.display.quit()
pygame.quit()
sys.exit(2)