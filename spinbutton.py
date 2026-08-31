import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x,y,width, height)
        self.text = text

    def draw(self, screen, font):
        pygame.draw.rect(screen, (0,200,0), self.rect)

        text_surface = font.render(self.text, True, "white")
        text_rect = text_surface.get_rect(center=self.rect.center)

        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        return ( 
            event.type == pygame.MOUSEBUTTONDOWN
            and self.rect.collidepoint(event.pos)
        )
