import sys, pygame
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

class x:
        location=10
        velocity=0

class y:
        location=500
        velocity=0

class player(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = image.player
                self.image.set_colorkey((0,0,0))
                self.rect = self.image.get_rect()
                self.rect.center = (self.image.get_size()[0] / 2, self.image.get_size()[1] / 2)
                

screen = pygame.display.set_mode([800,600])
screen.blit(pygame.transform.scale(image.outerCastle,(800,600)),[0,0,800,600])


player=player()
all_sprites.add(player)

running=True
while running:
        all_sprites.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      running = False


pygame.quit()
