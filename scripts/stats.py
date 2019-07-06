'''
Stats is a list object

[max health, current health, item, item modifier (ex1), attack, defense, current level]

ex1: Item can change attack or defense:
  A(Number)
  D(Number)

Stats can be used for both player and enemy stats.
'''
def healthCheck(stats): #checks if max health is 0 or below. If it is, it returns True, else it returns false
	try:
		if stats[7] is False:
			return True
	except:
		pass
	if stats[1]>0:
		return True
	else:
		return False

def player(stats):
	maxHealth=stats[0]
	currentHealth=stats[1]
	item=stats[2]
	itemMod=stats[3]
	attack=stats[4]
	defense=stats[5]
	level=stats[6]
	
def levelUp(stats):
	print(stats)
	level=stats[6]
	maxHealth=stats[0]+(2*level)
	currentHealth=stats[1]+(2*level)
	item=stats[2]
	itemMod=stats[3]
	attack=stats[4]+(2*level)
	defense=stats[5]+(2*level)
	
	return [maxHealth,currentHealth,item,itemMod,attack,defense,level]
	
def dealDamage(attackerStats,defenderStats):
	currentHealthAttack=attackerStats[1]
	itemModAttack=attackerStats[3]
	attackAttack=attackerStats[4]
	defenseAttack=attackerStats[5]

	if itemModAttack[1]=='A':
		attackAttack=attackAttack+int(itemModAttack[2])
	
	currentHealthDefender=defenderStats[1]
	itemModDefender=defenderStats[3]
	attackDefender=defenderStats[4]
	defenseDefender=defenderStats[5]

	if itemModDefender[1]=='D':
		defenseDefender=defenseDefender+int(itemModDefender[2])
		
		
	
	if (attackAttack-defenseDefender)<1:
		currentHealthDefender=currentHealthDefender-2

	else:
		currentHealthDefender=currentHealthDefender-(attackAttack-defenseDefender)

		
	defenseStats=[defenderStats[0],currentHealthDefender,defenderStats[2],defenderStats[3],defenderStats[4],defenderStats[5],defenderStats[6]]
		
	return defenseStats
	

	
	