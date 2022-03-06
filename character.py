import pygame, config

# RFCT NEEDED
class Character(pygame.sprite.Sprite):
	lives = 1
	speed = 1

	def __init__(self, name, imageName, point):
		pygame.sprite.Sprite.__init__(self)
		self.c = config.Config() # Config
		self.name = name # Name
		self.imageName = imageName # Image name
		self.sPosition = point # Move position
		self.reset(True)

	def reset(self,bool):
		self.getImage('down') # Down image
		self.position = self.image.get_rect() # Get position
		self.move(self.sPosition) # Move character

	def getImage(self, direction):
		imagePath = self.c.IMAGE_PATH + self.imageName + direction + ".png" # Direction image
		self.image = pygame.image.load(imagePath).convert()
		
	def update(self):
		print("=D")

    # Get image movement
	def movement(self,key):
		c = config.Config()

		if key == pygame.K_UP:
			self.getImage('up')
			return [0, -1*c.TILE_SIZE]
		elif key == pygame.K_DOWN:
			self.getImage('down')
			return [0, c.TILE_SIZE]
		elif key == pygame.K_LEFT:
			self.getImage('left')
			return [-1*c.TILE_SIZE, 0]
		elif key == pygame.K_RIGHT:
			self.getImage('right')
			return [c.TILE_SIZE, 0]

	def move(self,point):
		self.old = self.position
		self.position = self.position.move(point)
