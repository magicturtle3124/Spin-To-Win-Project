import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x,y,width, height)
        self.text = text
        self.color = (0,200,0)

    def draw(self, screen, font):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            draw_color = (0,255,0)
        else:
            draw_color = self.color

        pygame.draw.rect(screen, draw_color, self.rect)

        text_surface = font.render(self.text, True, "white")
        text_rect = text_surface.get_rect(center=self.rect.center)

        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        return ( 
            event.type == pygame.MOUSEBUTTONDOWN
            and self.rect.collidepoint(event.pos)
        )
