# This line lets us use code from the open-source pygame lib throughout the file:
import pygame

# import the connect_database function
# and the database_version variable
# from database.py into the current file
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

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
	asteroids = pygame.sprite.Group()
	Player.containers = (updatables, drawables)
	Asteroid.containers = (asteroids, updatables, drawables)
	AsteroidField.containers = (updatables,)
	asteroid_field = AsteroidField()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	dt = 0



# Below is the "GAME LOOP"
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		#pygame.Surface.fill(screen, (0,0,0)) REDUNDANT screen.fill
		screen.fill("black")
		updatables.update(dt)
		for d in drawables:
			d.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

# remember to label what is this for later understand:
if __name__ == "__main__":
		main()
