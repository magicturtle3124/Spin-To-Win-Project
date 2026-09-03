import pygame
import math

class Wheel:
    def __init__(self):
        self.angle = 0
        self.spin_speed = 0

    def start_spin(self):
        self.spin_speed = 20

    def update(self):
        if self.spin_speed > 0:
            self.angle += self.spin_speed
            self.spin_speed *= 0.98
        if self.spin_speed < 0.1:
            self.spin_speed = 0

    def draw(self, screen):
        center_x = 400
        center_y = 150
        radius = 80

        pygame.draw.circle(screen, "gold", (center_x, center_y), radius)

        end_x = center_x + math.cos(math.radians(self.angle)) * radius
        end_y = center_y + math.sin(math.radians(self.angle)) * radius

        pygame.draw.line(screen, "red", (center_x, center_y,), (end_x, end_y), 5)
        