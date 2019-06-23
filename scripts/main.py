import sys, pygame
import stats, classSelection, classImage, findImage, enemy

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

#Beginning area
NPCEnemy,NPCEnemyStats,NPCEnemyRect=enemy.randomSpawn([400,600],playerStat)
NPCEnemyRect=[NPCEnemyRect,600-NPCEnemy.get_width(),NPCEnemy.get_rect()[2],NPCEnemy.get_rect()[3]]
timeForNPCMovement=0

while True:
	player,playerAttack,playerAttack2,playerRect,left,attack=classImage.playerMovement(player,playerAttack,playerAttack2,playerRect,background,left,attack,[NPCEnemy,NPCEnemyRect])
	if timeForNPCMovement%60==0:
		NPCEnemyRect=enemy.randomMovement(NPCEnemyRect)
	timeForNPCMovement=timeForNPCMovement+1
	print(timeForNPCMovement)
	if playerClass=='Knight':
		if attack:
			classImage.fullWrite(playerAttack,playerRect,background,extra=[NPCEnemy,NPCEnemyRect])
			print(classImage.collisionCheckRect([playerRect[0],playerRect[1],playerRect[2]+20,playerRect[3]],NPCEnemyRect))
		else:
			classImage.fullWrite(player,playerRect,background,extra=[NPCEnemy,NPCEnemyRect])
	else:
		if attack:
			classImage.archerAttack(playerAttack,playerAttack2,playerRect,background,left)
		else:
			classImage.fullWrite(player,playerRect,background)