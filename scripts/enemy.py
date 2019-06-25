import pygame
import findImage,random


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
	item='Sword'
	itemMod='A'+str(2*playerLevel)
	attack=6*playerLevel
	defense=6*playerLevel
	level=playerLevel

	enemyStats=[maxHealth,currentHealth,item,itemMod,attack,defense,level]
	enemy=random.choice(['Slime.png','Spider.png'])
	enemy=findImage.getPygameImage('Images',enemy)
	location=random.randint(spawnLocation[0],spawnLocation[1])
	return enemy,enemyStats,location

def randomSlime(spawnLocation,playerStats):
	playerLevel=stats[8]
	maxHealth=10*playerLevel
	currentHealth=10*playerLevel
	item='Sword'
	itemMod='A'+str(2*playerLevel)
	attack=6*playerLevel
	defense=6*playerLevel
	level=playerLevel

	enemyStats=[maxHealth,currentHealth,item,itemMod,attack,defense,level]
	enemy='Slime.png'
	enemy=findImage.getPygameImage('Images',enemy)
	location=random.randint(spawnLocation[0],spawnLocation[1])
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
