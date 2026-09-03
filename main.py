import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import random
from prize import get_random_prize
from spinbutton import Button
from wheel import Wheel

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Spin to Win")
    print(f"Starting Spin to Win with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} Screen height: {SCREEN_HEIGHT}")

    running = True
    spin_button = Button(300,300,200,60, "SPIN")
    font = pygame.font.Font(None, 36)
    current_prize = ""
    spinning = False
    spin_start_time = 0
    animation_prize = ""
    animation_delay = 100
    last_animation_update = 0
    wheel = Wheel()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if spin_button.is_clicked(event) and not spinning:
                    spinning = True
                    wheel.start_spin()
                    spin_start_time = pygame.time.get_ticks()
                    animation_delay = 50
                    last_animation_update = spin_start_time
                    spin_button.text = "SPINNING"
                    spin_button.color = (255, 165, 0)

        if spinning:
            current_time = pygame.time.get_ticks()

            if current_time - last_animation_update > animation_delay:
                animation_prize = get_random_prize()
                if animation_delay < 1000:
                    animation_delay += 50

            if current_time - spin_start_time > 4000:
                current_prize = animation_prize
                spin_button.text = "SPIN"
                spin_button.color = (0, 200, 0)
                spinning = False
                print(f"You won {current_prize}")

        wheel.update()
        screen.fill("teal")
        wheel.draw(screen)
        spin_button.draw(screen, font)

        status_text = (
            "Wheel is spinning"
            if spinning
            else "Click to Spin!"
        )

        status_surface = font.render(
            status_text,
            True,
            "white"
        )

        status_rect = status_surface.get_rect(center=(400, 40))
        screen.blit(status_surface, status_rect)

        display_text = animation_prize if spinning else current_prize
        prize_text = font.render(display_text, True, "yellow")

        prize_rect = prize_text.get_rect(center=(400, 250))
        screen.blit(prize_text, prize_rect)
        pygame.display.flip()
        dt = clock.tick(60)/1000

    



if __name__ == "__main__":
    main()