import sys,pygame
pygame.init()
screen = pygame.display.set_mode([800,600])



def forward(player,playerRect,left):
	if left is True:
		player=pygame.transform.flip(knight,1,0)
		left=False
	screen.fill((252,252,252))
	playerRect=[playerRect[0]+1,playerRect[1],playerRect[2],playerRect[3]]
	print(playerRect)
	return player,playerRect,left

def backward(player, playerRect,left):
	if left is False:
		player=pygame.transform.flip(player,1,0)
		left=True
	playerRect=[playerRect[0]-0.75,playerRect[1],playerRect[2],playerRect[3]]
	return player,playerRect,left

def forward(player,left=False):
	playerRect = player.get_rect()
	playerRect=[playerRect[0],600-(player.get_height()),playerRect[2],playerRect[3]]
	screen.fill((252,252,252))
	screen.blit(player, playerRect)
	pygame.display.flip()
	pygame.event.pump()
	k = pygame.key.get_pressed()
	if k[pygame.K_d]:
		player,playerRect,left=forwardMove(player,playerRect,left)
	if k[pygame.K_a]:
		player,playerRect,left=backMove(player,playerRect,left)
	print(playerRect)
	
def getClassImage(playerClass):
	if playerClass=='Knight':
		player=pygame.image.load('Knight.png')
	else:
		player=pygame.image.load('Archer.png')
	player=pygame.transform.scale(player, (50,75))

