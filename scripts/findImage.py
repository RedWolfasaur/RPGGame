import os,pygame
pygame.init()

def getPygameImage(folder,imageName):
	for direct in os.listdir(path='.'):
		if str(direct)==str(folder):
			direct=direct
			for file in os.listdir(path=direct):
				if str(file)==str(imageName):
					print(os.path.join(direct, file))
					return pygame.image.load(os.path.join(direct, file))
		
	