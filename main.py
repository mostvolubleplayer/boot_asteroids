# This line lets us use code from the open-source pygame lib throughout the file:
import pygame
import sys

# import the connect_database function
# and the database_version variable
# from database.py into the current file
#Initi
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

#Use pygame's display.set_mode() to get a new GUI window:

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
	#initialization code
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
#groups
	updatables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatables, drawables)

	Asteroid.containers = (asteroids, updatables, drawables)
	Shot.containers = (updatables, drawables, shots)
	AsteroidField.containers = updatables
	asteroid_field = AsteroidField()

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	dt = 0



# Below is the "GAME LOOP"
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		updatables.update(dt)
		for asteroid in asteroids:
			if player.collision_check(asteroid):
				print("Game over!")
				sys.exit("Game Over!")

		#pygame.Surface.fill(screen, (0,0,0)) REDUNDANT thanks to screen.fill
		screen.fill("black")

		for d in drawables:
			d.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

# remember to label what is this for later understand:
if __name__ == "__main__":
		main()
