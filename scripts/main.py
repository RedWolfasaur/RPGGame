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
Hud=classImage.HudImage(findImage.getPygameImage('Images','Hud_Sword.png')) #Todo: make Hud related variables a list to reduce number of arguments
Hud_Coin=classImage.Hud_CoinImage(findImage.getPygameImage('Images','Hud_Coin.png'))
Hud_Health=classImage.Hud_HealthImage(findImage.getPygameImage('Images','Hud_Health.png'))
Hud_Health_Stat = playerStat[1]
Hud_Money_Stat = 0 #playerStat[?] just replace the ? with the stat and all should be good
attack=False
#Beginning area
NPCEnemy,NPCEnemyStats,NPCEnemyRect=enemy.randomSpawn([400,600],playerStat)
NPCEnemyRect=[NPCEnemyRect,600-NPCEnemy.get_width(),NPCEnemy.get_rect()[2],NPCEnemy.get_rect()[3]]
timeForNPCMovement=0
while True:
	player,playerAttack,playerAttack2,playerRect,left,attack=classImage.playerMovement(player,playerAttack,playerAttack2,playerRect,Hud,Hud_Coin,Hud_Health,Hud_Health_Stat,Hud_Money_Stat,background,left,attack,[NPCEnemy,NPCEnemyRect])
	if timeForNPCMovement%60==0:
		NPCEnemyRect=enemy.randomMovement(NPCEnemyRect)
	timeForNPCMovement=timeForNPCMovement+1
	print(timeForNPCMovement)
	if playerClass=='Knight':
		if attack:
			classImage.fullWrite(playerAttack,playerRect,Hud,Hud_Coin,Hud_Health,Hud_Health_Stat,Hud_Money_Stat,background,extra=[NPCEnemy,NPCEnemyRect])
			print(classImage.collisionCheckRect([playerRect[0],playerRect[1],playerRect[2]+20,playerRect[3]],NPCEnemyRect))
		else:
			classImage.fullWrite(player,playerRect,Hud,Hud_Coin,Hud_Health,Hud_Health_Stat,Hud_Money_Stat,background,extra=[NPCEnemy,NPCEnemyRect])
	else:
		if attack:
			classImage.archerAttack(playerAttack,playerAttack2,playerRect,Hud,Hud_Coin,Hud_Health,Hud_Health_Stat,Hud_Money_Stat,background,left)
		else:
			classImage.fullWrite(player,playerRect,Hud,Hud_Coin,Hud_Health,Hud_Health_Stat,Hud_Money_Stat,background)
