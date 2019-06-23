import sys,pygame,findImage
pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
'''
Functions that should be called:

classImage.playerMovement(player,playerRect,background, left=False)
	playerMovement(player,playerRect,left=False)
	The Main Part of this Script. Checks for movement, while writing to the screen.
	inputs:
		player - A Pygame Image
		playerRect - The Pygame Rect belonging to the Image
		left - A Bool indicating whether the image is facing left. If no Bool is given it will be assumed to be False
		Background - A Python Image
	returns:
		player - A Pygame Image
		playerRect - The Pygame Rect belonging to the Image
		left - A Bool indicating whether the image is facing left

classImage.fullWrite(player, playerRect,backGround,backGroundRect=[0,0,800,600],extra=False,extra2=False,extra3=False,extra4=False):
    writePlayer(player, playerRect)
    Writes a player to the screen,
	inputs:
		player - A Pygame Image
		player location - A Pygame Rect Object
		Background - A Pygame Image
		BackgroundRect - A Pygame Rect
		extra - List [(Pygame Image), (Pygame Rect)]
   
classImage.getClassImage(playerClass)
	getClassImage(playerClass)
	checks the class the player has chosen and returns the appropriate image.
	inputs: 
	    playerClass - A string indicating whether the player is a 'Knight' or a 'Archer'
	returns:
		player - A Pygame Image
		playerRect - The Pygame Rect belonging to the Image
		left - A Bool indicating whether the image is facing left
		
classImage.backGroundImage(backGround=None)
	backGroundImage(backGround=None)
	Look im tired and I don't wanna write anymore. The input is self explanatory
	returns:
		backGround - A Pygame Image



All other Functions should not be called, for they are part of the callable scripts.

'''
def smallRightJumpUp(player,playerRect,left,backGround):
	if playerRect[0]+3>=750:
		playerRect=[750,playerRect[1]-4,playerRect[2],playerRect[3]]
	else:
		playerRect=[playerRect[0]+3,playerRect[1]-4,playerRect[2],playerRect[3]]
	fullWrite(player, playerRect,backGround)
	return playerRect

def smallRightJumpDown(player,playerRect,left,backGround):
	if playerRect[0]+3>=750:
		playerRect=[750,playerRect[1]+4,playerRect[2],playerRect[3]]
	else:
		playerRect=[playerRect[0]+3,playerRect[1]+4,playerRect[2],playerRect[3]]
	fullWrite(player, playerRect,backGround)
	return playerRect

def rightJump(player,playerRect,left,backGround):
	x=0
	while x<12:
		playerRect=smallRightJumpUp(player, playerRect,left,backGround)
		x=x+1
	x=0
	while x<12:
		playerRect=smallRightJumpDown(player, playerRect,left,backGround)
		x=x+1
	pygame.time.delay(2)
	return playerRect

def smallLeftJumpUp(player,playerRect,left,backGround):
	if playerRect[0]-3<=0:
		playerRect=[0,playerRect[1]-4,playerRect[2],playerRect[3]]
	else:
		playerRect=[playerRect[0]-3,playerRect[1]-4,playerRect[2],playerRect[3]]
	fullWrite(player, playerRect,backGround)
	return playerRect

def smallLeftJumpDown(player,playerRect,left,backGround):
	if playerRect[0]-3<=0:
		playerRect=[0,playerRect[1]+4,playerRect[2],playerRect[3]]
	else:
		playerRect=[playerRect[0]-3,playerRect[1]+4,playerRect[2],playerRect[3]]
	fullWrite(player, playerRect,backGround)
	return playerRect

def leftJump(player,playerRect,left,backGround):
	x=0
	while x<12:
		playerRect=smallLeftJumpUp(player, playerRect,left,backGround)
		x=x+1
	x=0
	while x<12:
		playerRect=smallLeftJumpDown(player, playerRect,left,backGround)
		x=x+1
	pygame.time.delay(2)
	return playerRect
	
def jumpUp(player, playerRect,left,backGround):
	playerRect=[playerRect[0],playerRect[1]-5,playerRect[2],playerRect[3]]
	fullWrite(player, playerRect,backGround)
	return playerRect

def jumpDown(player, playerRect,left,backGround):
	playerRect=[playerRect[0],playerRect[1]+5,playerRect[2],playerRect[3]]
	fullWrite(player, playerRect,backGround)
	return playerRect	 
	
def jump(player,playerRect,left,backGround):
	x=0
	while x<12:
		playerRect=jumpUp(player, playerRect,left,backGround)
		x=x+1
	x=0
	while x<12:
		playerRect=jumpDown(player, playerRect,left,backGround)
		x=x+1

def forward(player,playerAttack,playerAttack2,playerRect,left):
	if left is True:
		player=pygame.transform.flip(player,1,0)
		playerAttack=pygame.transform.flip(playerAttack,1,0)
		playerAttack2=pygame.transform.flip(playerAttack2,1,0)
		left=False
	if playerRect[0]+4.5>=750:
		return player,playerAttack, [750,playerRect[1],playerRect[2],playerRect[3]], left
	playerRect=[playerRect[0]+4.5,playerRect[1],playerRect[2],playerRect[3]]
	return player,playerAttack,playerAttack2,playerRect,left

def backward(player,playerAttack,playerAttack2, playerRect,left):
	if left is False:
		player=pygame.transform.flip(player,1,0)
		playerAttack=pygame.transform.flip(playerAttack,1,0)
		playerAttack2=pygame.transform.flip(playerAttack2,1,0)
		left=True
	if playerRect[0]-4.25<=0:
		return player,playerAttack, [0,playerRect[1],playerRect[2],playerRect[3]], left
	playerRect=[playerRect[0]-4.25,playerRect[1],playerRect[2],playerRect[3]]
	return player,playerAttack,playerAttack2,playerRect,left

def backGroundImage(backGround):
	backGround=pygame.transform.scale(backGround,(800,600))
	return backGround

def writeBackground(backGround,backGroundRect=[0,0,800,600]):
	screen.fill((252,252,252))
	if backGround==None:
		pass
	else:
		screen.blit(backGround,backGroundRect)

def writePlayer(player, playerRect):
	screen.blit(player, playerRect)

def fullWrite(player, playerRect,backGround,backGroundRect=[0,0,800,600],arrow=False,extra=False,extra2=False,extra3=False):
	writeBackground(backGround,backGroundRect=[0,0,800,600])
	if arrow is not False:
		screen.blit(arrow[0],arrow[1])
	if extra is not False:
		screen.blit(extra[0],extra[1])
	if extra2 is not False:
		screen.blit(extra2[0],extra2[1])
	if extra3 is not False:
		screen.blit(extra3[0],extra3[1])
		
	'''
	NPC Writes go between here
	'''
	writePlayer(player, playerRect)
	pygame.display.flip()
	
	
def playerMovement(player,playerAttack,playerAttack2,playerRect,backGround,left=False,attack=False):
	print(playerRect)
	clock.tick(60)
	if attack:
		attack=False
	pygame.event.pump()
	k = pygame.key.get_pressed()
	if k[pygame.K_d]:
		player,playerAttack,playerAttack2,playerRect,left=forward(player,playerAttack,playerAttack2,playerRect,left)
	if k[pygame.K_a]:
		player,playerAttack,playerAttack2,playerRect,left=backward(player,playerAttack,playerAttack2,playerRect,left)
	if k[pygame.K_w]:
		if k[pygame.K_d]:
			playerRect=rightJump(player,playerRect,left,backGround)
		elif k[pygame.K_a]:
			playerRect=leftJump(player,playerRect,left,backGround)
		else:
			jump(player,playerRect,left,backGround)
	if k[pygame.K_SPACE]:
			attack=True
	return player,playerAttack,playerAttack2,playerRect,left,attack

def archerAttack(playerAttack,playerAttack2,playerRect,backGround,left,backGroundRect=[0,0,800,600]):
	fullWrite(playerAttack, playerRect,backGround)
	pygame.time.delay(1000)
	fullWrite(playerAttack2, playerRect,backGround)
	pygame.time.delay(1000)
	x=0
	arrowRect=playerRect
	arrow=findImage.getPygameImage('Images','arrow.png')
	if left:
		arrow=pygame.transform.flip(arrow,1,0)
		while True:
			fullWrite(playerAttack, playerRect,backGround,arrow=[arrow,arrowRect])
			arrowRect,x=arrowFlyLeft(arrowRect,x)
			if x==60:
				break
	else:
		arrowRect=[arrowRect[0]+10,arrowRect[1],arrowRect[2],arrowRect[3]]
		while True:
			fullWrite(playerAttack, playerRect,backGround,arrow=[arrow,arrowRect])
			arrowRect,x=arrowFlyRight(arrowRect,x)
			if x>=40:
				break
	fullWrite(playerAttack, playerRect,backGround)

def arrowFlyLeft(arrowRect,x):
	x=x+1
	arrowRect=[arrowRect[0]-4,arrowRect[1],arrowRect[2],arrowRect[3]]
	return arrowRect,x
	
def arrowFlyRight(arrowRect,x):
	x=x+1
	arrowRect=[arrowRect[0]+4,arrowRect[1],arrowRect[2],arrowRect[3]]
	return arrowRect,x
		
def collisionCheckRect(player,checkRect):
	if pygame.Rect(checkRect).colliderect(pygame.Rect(player)):
		return True
	return False
	
def getClassImage(playerClass):
	if playerClass=='Knight':
		player=findImage.getPygameImage('Images','Knight.png')
		playerAttack=findImage.getPygameImage('Images','KnightAttack.png')
		playerAttack2=playerAttack
	else:
		player=findImage.getPygameImage('Images','Archer.png')
		playerAttack=findImage.getPygameImage('Images','Archer-1.png')
		playerAttack2=findImage.getPygameImage('Images','Archer-2.png')
	player=pygame.transform.scale(player, (75,75))
	playerAttack=pygame.transform.scale(playerAttack, (75,75))
	playerAttack2=pygame.transform.scale(playerAttack2, (75,75))
	playerRect = player.get_rect()
	playerRect=[playerRect[0],600-(player.get_height()),playerRect[2]-20,playerRect[3]]
	return player, playerRect,playerAttack,playerAttack2, False

