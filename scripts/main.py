import sys, pygame
import stats, classSelection, classImage, findImage

playerClass=classSelection.classSelection() #Main Menu
if playerClass==0:
	playerStat=[100,100,'Sword','A5',10,10,1]
	playerClass='Knight'
	
if playerClass==1:
	playerStat=[100,100,'Bow','A5',15,5,1]
	playerClass='Archer'


	
	
player,playerRect,left=classImage.getClassImage(playerClass)
backGround=classImage.backGroundImage(findImage.getPygameImage('Images','dogger.gif'))



while True:
	player,playerRect,left=classImage.playerMovement(player,playerRect,backGround,left)