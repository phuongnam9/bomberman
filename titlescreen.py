import sys, pygame, config, game, highscore

class Titlescreen():

	def __init__(self):
        # Config
		self.c = config.Config()
		# Exit game
		exitMain = False

        # Game start
		while not exitMain:
            # Start pygame and screen 
			pygame.init()
			self.screen = pygame.display.set_mode((1028,768))
			pygame.display.set_caption("Bomberman")

			imagePath = self.c.IMAGE_PATH + "titlescreen.png"
			img = pygame.image.load(imagePath).convert()
			self.screen.blit(img,(0,0))
			
            # Music
			pygame.mixer.music.load(self.c.AUDIO_PATH + "title.mid")
			pygame.mixer.music.play()

			clock = pygame.time.Clock()
			pygame.mouse.set_visible(True)
			pygame.display.flip()
			userInteracted = False

            # User choose play mode
			while not userInteracted:
				clock.tick(self.c.FPS)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						userInteracted = True
						exitMain = True
						pygame.quit()
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
							userInteracted = True
							exitMain = True
							pygame.quit()
					elif event.type == pygame.MOUSEBUTTONDOWN:
						if self.withinBoundary(25, 250, 500, 540):
							userInteracted = True
							self.singlePlayer() # Single Player game clicked
						elif self.withinBoundary(25, 250, 550, 600):
							userInteracted = True
							self.multiplayer() # Multiplayer game clicked
						elif self.withinBoundary(25, 240, 605, 645):
							userInteracted = True
							self.instructions() # Instructions clicked
						elif self.withinBoundary(25, 240, 655, 700):
							userInteracted = True
							self.highScores() # High Scores clicked
						elif self.withinBoundary(25, 105, 705, 745):
							userInteracted = True
							exitMain = True
							pygame.quit() # Exit clicked

    # Mouse within boundary
	def withinBoundary(self, x1, x2, y1, y2):
		if pygame.mouse.get_pos()[0] >= x1 and pygame.mouse.get_pos()[0] <= x2 and pygame.mouse.get_pos()[1] >= y1 and pygame.mouse.get_pos()[1] <= y2:
			return True
		return False

    # SinglePlayer
	def singlePlayer(self):
		g = game.Game(self.c.SINGLE)

    # MultiPlayer
	def multiplayer(self):
		g = game.Game(self.c.MULTI)

    # Instructions
	def instructions(self):
		print("Instructions clicked!")

    # High score
	def highScores(self):
		h = highscore.Highscore()
		h.displayScore()

	def clearBackground(self):
		bg = pygame.Surface(self.screen.get_size())
		bg = bg.convert()
		bg.fill((0,0,0))
		self.blit(bg,(0,0))

# Test
t = Titlescreen()
