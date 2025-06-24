import sys
import pygame
from constants import * 
from player import *
from asteroidfield import *

def main():
    # Initialize all imported pygame modules
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0

    # Print statements
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(pygame.font.get_default_font(), 36)
    running = True

    # Groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updateable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    Shot.containers = (updateable, drawable, shots)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()

    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updateable.update(dt)
        screen.fill("black")
        
        text_surface = font.render(f'{player.score}', True, pygame.Color("white"))
        screen.blit(text_surface, dest=(0,0))

        for item in drawable:
            item.draw(screen)

        for obj in asteroids:
            if obj.collision(player):
                print("Game over")
                sys.exit()

        for obj in asteroids:
            for bullet in shots:
                if obj.collision(bullet):
                    player.score += 10
                    obj.split()
                    bullet.kill()

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
