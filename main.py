import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import random
from prize import get_random_prize
from spinbutton import Button

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Spin to Win")
    print(f"Starting Spin to Win with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} Screen height: {SCREEN_HEIGHT}")

    running = True
    spin_button = Button(300,250,200,60, "SPIN")
    font = pygame.font.Font(None, 36)
    current_prize = ""
    spinning = False
    spin_start_time = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if spin_button.is_clicked(event) and not spinning:
                    spinning = True
                    spin_start_time = pygame.time.get_ticks()
                    spin_button.text = "SPINNING"

        if spinning:
            current_time = pygame.time.get_ticks()

            if current_time - spin_start_time > 500:
                current_prize = get_random_prize()
                spin_button.text = "SPIN"
                spinning = False
                print(f"You won {current_prize}")

        screen.fill("teal")
        spin_button.draw(screen, font)
        prize_text = font.render(current_prize, True, "white")
        screen.blit(prize_text, (250, 150))
        pygame.display.flip()
        dt = clock.tick(60)/1000

    



if __name__ == "__main__":
    main()