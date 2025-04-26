# This line lets us use code from the open-source pygame lib throughout the file:
import pygame

# import the connect_database function
# and the database_version variable
# from database.py into the current file
from constants import *

#Use pygame's display.set_mode() to get a new GUI window:

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	clock = pygame.time.Clock()
	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return
		pygame.Surface.fill(screen, (0,0,0))
		pygame.display.flip()
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
		main()





