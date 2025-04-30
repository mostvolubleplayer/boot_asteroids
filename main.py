# This line lets us use code from the open-source pygame lib throughout the file:
import pygame

# import the connect_database function
# and the database_version variable
# from database.py into the current file
from constants import *
from player import Player

#Use pygame's display.set_mode() to get a new GUI window:

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	updatables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	Player.containers = (updatables, drawables)
	player = Player(SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2)
	dt = 0



# Below is the "GAME LOOP"
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		pygame.Surface.fill(screen, (0,0,0))
		screen.fill("black")
		updatables.update(dt)
		for d in drawables:
			d.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

# remember to label what is this for later understand:
if __name__ == "__main__":
		main()
