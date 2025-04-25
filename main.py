# This line lets us use code from the open-source pygame lib throughout the file:
import pygame

# import the connect_database function
# and the database_version variable
# from database.py into the current file
from database import connect_database, database_version

def main():
	print("Starting Asteroids!")
	
if __name__ == "__main__":
		main()
