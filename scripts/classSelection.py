'''
Class selection.

Functions that should be called:
classSelection.classSelection()
	classSelection()
	Runs the class selection screen
	returns:
		a Boolean indicating whther the player has chosen Knight or Archer
			0 - Knight
			1 - Archer
			
All others should not be called

'''



import sys, pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
TNR = pygame.font.Font('8bitOperatorPlus-Regular.ttf', 30)

#location [x,y,width,height] 
def border(color,location):
	pygame.draw.rect(screen, color, (location))
	pygame.draw.rect(screen, (252,252,252), (location[0]+5,location[1]+5,location[2]-10,location[3]-10))

#Writes text, returns width of text
def textWrite(text,location,wh=0):
	textsurface = TNR.render(text, False, (0, 0, 0))
	screen.blit(textsurface,location)
	if wh==0:
		return textsurface.get_width()
	else:
		return textsurface.get_height()

def startingPage(class1=(0,0,0),class2=(0,0,0)):
	textWidth=(textWrite('Choose your class.',(400,100)))/2
	screen.fill((252,252,252))
	textWrite('Choose your class.',(400-textWidth,50))
	border(class1,[25,100,350,230])
	textHeight=textWrite('Class One: Knight',(35,110),1)
	textHeight=textWrite('Attack: 10',(35,textHeight+110),1)
	textWrite('Defense: 10',(35,(42*2)+110),1)
	textWrite('Item:',(35,(42*3)+110))
	textWrite('  Sword (+5 Attack)',(35,(42*4)+110))
	border(class2,[425,100,350,230])
	textWrite('Class Two: Archer',(435,110))
	textWrite('Attack: 10',(435,(42*1)+110),1)
	textWrite('Defense: 5',(435,(42*2)+110),1)
	textWrite('Item:',(435,(42*3)+110),1)
	textWrite('  Bow (+5 Attack)',(435,(42*4)+110),1)
	pygame.display.flip()	

def classSelection():
	while True:
		startingPage()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				if (pygame.Rect([25,100,350,200])).collidepoint(pygame.mouse.get_pos()):
					startingPage(class1=(255,69,0))
					pygame.time.delay(500)
					startingPage()
					print('a')
					return 0
					
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				if (pygame.Rect([425,100,350,200])).collidepoint(pygame.mouse.get_pos()):
					startingPage(class2=(255,69,0))
					pygame.time.delay(500)
					startingPage()
					return 1
