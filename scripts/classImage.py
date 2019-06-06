import sys,pygame,findImage
pygame.init()
screen = pygame.display.set_mode([800,600])

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

classImage.writePlayer(player, playerRect,backGround,backGroundRect=[0,0,800,600])
    writePlayer(player, playerRect)
    Writes a player to the screen,
	inputs:
		player - A Pygame Image
		player location - A Pygame Rect Object
		Background - A Pygame Image
		BackgroundRect - A Pygame Rect
   
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
	if playerRect[0]+5>=750:
		playerRect=[750,playerRect[1]-10,playerRect[2],playerRect[3]]
	else:
		playerRect=[playerRect[0]+5,playerRect[1]-10,playerRect[2],playerRect[3]]
	writePlayer(player, playerRect,backGround)
	pygame.time.delay(25)
	return playerRect

def smallRightJumpDown(player,playerRect,left,backGround):
	if playerRect[0]+5>=750:
		playerRect=[750,playerRect[1]+10,playerRect[2],playerRect[3]]
	else:
		playerRect=[playerRect[0]+5,playerRect[1]+10,playerRect[2],playerRect[3]]
	writePlayer(player, playerRect,backGround)
	pygame.time.delay(25)
	return playerRect

def rightJump(player,playerRect,left,backGround):
	playerRect=smallRightJumpUp(player,playerRect,left,backGround)
	playerRect=smallRightJumpUp(player,playerRect,left,backGround)
	playerRect=smallRightJumpUp(player,playerRect,left,backGround)
	playerRect=smallRightJumpDown(player,playerRect,left,backGround)
	playerRect=smallRightJumpDown(player,playerRect,left,backGround)
	playerRect=smallRightJumpDown(player,playerRect,left,backGround)
	pygame.time.delay(25)
	return playerRect

def smallLeftJumpUp(player,playerRect,left,backGround):
	if playerRect[0]-5<=0:
		playerRect=[0,playerRect[1]-10,playerRect[2],playerRect[3]]
	else:
		playerRect=[playerRect[0]-5,playerRect[1]-10,playerRect[2],playerRect[3]]
	writePlayer(player, playerRect,backGround)
	pygame.time.delay(25)
	return playerRect

def smallLeftJumpDown(player,playerRect,left,backGround):
	if playerRect[0]-5<=0:
		playerRect=[0,playerRect[1]+10,playerRect[2],playerRect[3]]
	else:
		playerRect=[playerRect[0]-5,playerRect[1]+10,playerRect[2],playerRect[3]]
	writePlayer(player, playerRect,backGround)
	pygame.time.delay(25)
	return playerRect

def leftJump(player,playerRect,left,backGround):
	playerRect=smallLeftJumpUp(player,playerRect,left,backGround)
	playerRect=smallLeftJumpUp(player,playerRect,left,backGround)
	playerRect=smallLeftJumpUp(player,playerRect,left,backGround)
	playerRect=smallLeftJumpDown(player,playerRect,left,backGround)
	playerRect=smallLeftJumpDown(player,playerRect,left,backGround)
	playerRect=smallLeftJumpDown(player,playerRect,left,backGround)
	pygame.time.delay(25)
	return playerRect
	
def jump(player,playerRect,left,backGround):
	playerRect=[playerRect[0],playerRect[1]-10,playerRect[2],playerRect[3]]
	writePlayer(player, playerRect,backGround)
	pygame.time.delay(25)
	playerRect=[playerRect[0],playerRect[1]-10,playerRect[2],playerRect[3]]
	writePlayer(player, playerRect,backGround)
	pygame.time.delay(25)
	playerRect=[playerRect[0],playerRect[1]-10,playerRect[2],playerRect[3]]
	writePlayer(player, playerRect,backGround)
	pygame.time.delay(25)
	playerRect=[playerRect[0],playerRect[1]+15,playerRect[2],playerRect[3]]
	writePlayer(player, playerRect,backGround)
	pygame.time.delay(25)
	playerRect=[playerRect[0],playerRect[1]+15,playerRect[2],playerRect[3]]
	writePlayer(player, playerRect,backGround)
	pygame.time.delay(50)
	

def forward(player,playerRect,left):
	if left is True:
		player=pygame.transform.flip(player,1,0)
		left=False
	if playerRect[0]+1.5>=750:
		return player, [750,playerRect[1],playerRect[2],playerRect[3]], left
	playerRect=[playerRect[0]+1.5,playerRect[1],playerRect[2],playerRect[3]]
	return player,playerRect,left

def backward(player, playerRect,left):
	if left is False:
		player=pygame.transform.flip(player,1,0)
		left=True
	if playerRect[0]-1.25<=0:
		return player, [0,playerRect[1],playerRect[2],playerRect[3]], left
	playerRect=[playerRect[0]-1.25,playerRect[1],playerRect[2],playerRect[3]]
	return player,playerRect,left

def backGroundImage(backGround):
	backGround=pygame.transform.scale(backGround,(800,600))
	return backGround

def writePlayer(player, playerRect,backGround,backGroundRect=[0,0,800,600]):
	screen.fill((252,252,252))
	if backGround==None:
		pass
	else:
		screen.blit(backGround,backGroundRect)
	screen.blit(player, playerRect)
	pygame.display.flip()

def playerMovement(player,playerRect,backGround,left=False):
	print(playerRect)
	writePlayer(player, playerRect,backGround)
	pygame.event.pump()
	k = pygame.key.get_pressed()
	if k[pygame.K_d]:
		player,playerRect,left=forward(player,playerRect,left)
	if k[pygame.K_a]:
		player,playerRect,left=backward(player,playerRect,left)
	if k[pygame.K_w]:
		if k[pygame.K_d]:
			playerRect=rightJump(player,playerRect,left,backGround)
		elif k[pygame.K_a]:
			playerRect=leftJump(player,playerRect,left,backGround)
		else:
			jump(player,playerRect,left,backGround)
	return player,playerRect,left
	
def getClassImage(playerClass):
	if playerClass=='Knight':
		player=findImage.getPygameImage('Images','Knight.png')
	else:
		player=findImage.getPygameImage('Images','Archer.png')
	player=pygame.transform.scale(player, (50,75))
	playerRect = player.get_rect()
	playerRect=[playerRect[0],600-(player.get_height()),playerRect[2],playerRect[3]]
	return player, playerRect, False

