'''
Stats is a list object

[max health, current health, item, item modifier (ex1), attack, defense, speed, current level]

ex1: Item can change speed, attack, or defense:
  S(Number)
  A(Number)
  D(Number)

Stats can be used for both player and enemy stats.
'''
def healthCheck(stats): #checks if max health is 0 or below. If it is, it returns True, else it returns false
	if stats[1]>1:
		return True
	else:
		return False

def player(stats):
	maxHealth=stats[0]
	currentHealth=stats[1]
	item=stats[3]
	itemMod=stats[4]
	attack=stats[5]
	defense=stats[6]
	speed=stats[7]
	level=stats[8]
