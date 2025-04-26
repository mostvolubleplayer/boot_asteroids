# import pygame module
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    #below is the constructor - to be implemented later
    def __init__(self, x, y, radius):
        #this is for later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x.y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw (self, screen):
        #sub-classes must override
        pass

    def update(self, dt):
        #sub-classes must override
        pass
