import sys, pygame
import stats, classSelection, classImage, findImage

playerClass=classSelection.classSelection() #Main Menu
if playerClass==0:
	playerStat=[100,100,'Sword','A5',10,10,1]
	playerClass='Knight'
	
if playerClass==1:
	playerStat=[100,100,'Bow','A5',15,5,1]
	playerClass='Archer'


	
	
player,playerRect,playerAttack,playerAttack2,left=classImage.getClassImage(playerClass)
background=classImage.backGroundImage(findImage.getPygameImage('Images','FrontCastle.png'))
attack=False


while True:
	player,playerAttack,playerAttack2,playerRect,left,attack=classImage.playerMovement(player,playerAttack,playerAttack2,playerRect,background,left,attack)
	if playerClass=='Knight':
		if attack:
			classImage.fullWrite(playerAttack,playerRect,background)
		else:
			classImage.fullWrite(player,playerRect,background)
	else:
		if attack:
			classImage.archerAttack(playerAttack,playerAttack2,playerRect,background,left)
		else:
			classImage.fullWrite(player,playerRect,background)