import pygame
import findImage,random,classImage


pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()



#player level should influence stats of the enemy


'''




'''

def randomMovement(enemyRect):
	movement=random.randint(0,100)
	if movement<21:
		if enemyRect[0]-8<=350:
			pass
		else:
			enemyRect=[enemyRect[0]-4,enemyRect[1],enemyRect[2],enemyRect[3]]
	elif movement>79:
		if enemyRect[0]+8>=550:
			pass
		else:
			enemyRect=[enemyRect[0]+4,enemyRect[1],enemyRect[2],enemyRect[3]]
		
	else:
		pass
	return enemyRect
   
def randomSpawn(spawnLocation,playerStats):
	playerLevel=playerStats[6]
	maxHealth=10*playerLevel
	currentHealth=10*playerLevel
	item='Slime'
	itemMod='A'+str(2*playerLevel)
	attack=6*playerLevel
	defense=6*playerLevel
	level=playerLevel
	
	enemyStats=[maxHealth,currentHealth,item,itemMod,attack,defense,level]
	enemy=random.choice(['Slime.png','Spider.png'])
	enemy='Spider.png'
	if enemy=='Slime.png':
		enemy=findImage.getPygameImage('Images',enemy)
		location=random.randint(spawnLocation[0],spawnLocation[1])
		location=[location,600-enemy.get_width(),enemy.get_rect()[2],enemy.get_rect()[3]-10]
	else:
		enemy=findImage.getPygameImage('Images',enemy)
		location=random.randint(spawnLocation[0],spawnLocation[1])
		location=[location,531,enemy.get_rect()[2],enemy.get_rect()[3]]
	return enemy,enemyStats,location

def randomSlime(spawnLocation,playerStats):
	playerLevel=stats[8]
	maxHealth=10*playerLevel
	currentHealth=10*playerLevel
	item='Web'
	itemMod='A'+str(2*playerLevel)
	attack=6*playerLevel
	defense=6*playerLevel
	level=playerLevel
	
	enemyStats=[maxHealth,currentHealth,item,itemMod,attack,defense,level]
	enemy='Slime.png'
	enemy=findImage.getPygameImage('Images',enemy)
	location=random.randint(spawnLocation[0],spawnLocation[1])
	location=[location,600-enemy.get_width(),enemy.get_rect()[2],enemy.get_rect()[3]-10]
	return enemy,enemyStats,location

def randomSpider(spawnLocation,playerStats):
	playerLevel=stats[8]
	maxHealth=10*playerLevel
	currentHealth=10*playerLevel
	item='Sword'
	itemMod='A'+str(2*playerLevel)
	attack=6*playerLevel
	defense=6*playerLevel
	level=playerLevel
	
	enemyStats=[maxHealth,currentHealth,item,itemMod,attack,defense,level]
	enemy='Spider.png'
	enemy=findImage.getPygameImage('Images',enemy)
	location=random.randint(spawnLocation[0],spawnLocation[1])
	return enemy,enemyStats,location	

def enemyKnockedback(player,playerRect,background,NPCEnemy,NPCEnemyRect):
	print((800-NPCEnemy.get_width())+3)
	if (NPCEnemyRect[0]+NPCEnemy.get_width())+3>800:
		NPCEnemyRect=[800-NPCEnemy.get_width(),NPCEnemyRect[1]-2,NPCEnemyRect[2],NPCEnemyRect[3]]
	else:
		NPCEnemyRect=[NPCEnemyRect[0]+3,NPCEnemyRect[1]-2,NPCEnemyRect[2],NPCEnemyRect[3]]
	classImage.fullWrite(player,playerRect,background,extra=[NPCEnemy,NPCEnemyRect])
	
	if (NPCEnemyRect[0]+NPCEnemy.get_width())+4>800:
		NPCEnemyRect=[800-NPCEnemy.get_width(),NPCEnemyRect[1]-3,NPCEnemyRect[2],NPCEnemyRect[3]]
	else:
		NPCEnemyRect=[NPCEnemyRect[0]+4,NPCEnemyRect[1]-3,NPCEnemyRect[2],NPCEnemyRect[3]]
	classImage.fullWrite(player,playerRect,background,extra=[NPCEnemy,NPCEnemyRect])
	
	if (NPCEnemyRect[0]+NPCEnemy.get_width())+4>800:
		NPCEnemyRect=[800-NPCEnemy.get_width(),NPCEnemyRect[1]+3,NPCEnemyRect[2],NPCEnemyRect[3]]
	else:
		NPCEnemyRect=[NPCEnemyRect[0]+4,NPCEnemyRect[1]+3,NPCEnemyRect[2],NPCEnemyRect[3]]
	classImage.fullWrite(player,playerRect,background,extra=[NPCEnemy,NPCEnemyRect])
	
	if (NPCEnemyRect[0]+NPCEnemy.get_width())+3>800:
		NPCEnemyRect=[800-NPCEnemy.get_width(),NPCEnemyRect[1]+2,NPCEnemyRect[2],NPCEnemyRect[3]]
	else:
		NPCEnemyRect=[NPCEnemyRect[0]+3,NPCEnemyRect[1]+2,NPCEnemyRect[2],NPCEnemyRect[3]]
	classImage.fullWrite(player,playerRect,background,extra=[NPCEnemy,NPCEnemyRect])
	return NPCEnemyRect
	
def playerKnockback(player,playerRect,background,NPCEnemy,NPCEnemyRect):
	playerRect=[playerRect[0]-3,playerRect[1]-2,playerRect[2],playerRect[3]]
	classImage.fullWrite(player,playerRect,background,extra=[NPCEnemy,NPCEnemyRect])
	playerRect=[playerRect[0]-4,playerRect[1]-3,playerRect[2],playerRect[3]]
	classImage.fullWrite(player,playerRect,background,extra=[NPCEnemy,NPCEnemyRect])
	playerRect=[playerRect[0]-4,playerRect[1]+3,playerRect[2],playerRect[3]]
	classImage.fullWrite(player,playerRect,background,extra=[NPCEnemy,NPCEnemyRect])
	playerRect=[playerRect[0]-3,playerRect[1]+2,playerRect[2],playerRect[3]]
	classImage.fullWrite(player,playerRect,background,extra=[NPCEnemy,NPCEnemyRect])
	return playerRect
