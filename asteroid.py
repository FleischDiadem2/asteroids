import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (128, 128, 128), (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        split_angle = random.uniform(20, 50)
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_asteroid_1 = Asteroid(int(self.position.x), int(self.position.y), split_radius)
            new_asteroid_2 = Asteroid(int(self.position.x), int(self.position.y), split_radius)
            new_asteroid_1.velocity = self.velocity.rotate(split_angle) * 1.2
            new_asteroid_2.velocity = self.velocity.rotate(-split_angle) * 1.2
        