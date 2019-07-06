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
timeForNPCMovement=0

while stats.healthCheck(playerStat):
	player,playerAttack,playerAttack2,playerRect,left,attack=classImage.playerMovement(player,playerAttack,playerAttack2,playerRect,background,left,attack,[NPCEnemy,NPCEnemyRect])
	
	if timeForNPCMovement%60==0:
		NPCEnemyRect=enemy.randomMovement(NPCEnemyRect)
	timeForNPCMovement=timeForNPCMovement+1
	if stats.healthCheck(NPCEnemyStats):
		pass
	else:
		NPCEnemy=False
		NPCEnemyStats.append(False)
		NPCEnemyRect=[0,0,0,0]
		playerStat=stats.levelUp(playerStat)
	
	if playerClass=='Knight':
		if attack:
			classImage.fullWrite(playerAttack,playerRect,background,extra=[NPCEnemy,NPCEnemyRect])
			if classImage.collisionCheckRect([playerRect[0],playerRect[1],playerRect[2],playerRect[3]],NPCEnemyRect):
				NPCEnemyStats=stats.dealDamage(playerStat,NPCEnemyStats)
				print(playerStat)
				NPCEnemyRect=enemy.enemyKnockedback(player,playerRect,background,NPCEnemy,NPCEnemyRect)
		else:
			classImage.fullWrite(player,playerRect,background,extra=[NPCEnemy,NPCEnemyRect])
			if classImage.collisionCheckRect([playerRect[0],playerRect[1],playerRect[2],playerRect[3]],NPCEnemyRect):
				playerStat=stats.dealDamage(NPCEnemyStats,playerStat)
				print(playerStat)
				playerRect=enemy.playerKnockback(player,playerRect,background,NPCEnemy,NPCEnemyRect)
				
				
				
				
	else:
		if attack:
			classImage.archerAttack(playerAttack,playerAttack2,playerRect,background,left)
		else:
			classImage.fullWrite(player,playerRect,background)