# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen                   = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running                  = True
    backcolor                = (0,0,0)
    drawcolor                = (255, 255, 255)
    updateable               = pygame.sprite.Group()
    drawable                 = pygame.sprite.Group()
    asteroids                = pygame.sprite.Group()
    shots                    = pygame.sprite.Group()
    clock                    = pygame.time.Clock()
    dt                       = 0
    AsteroidField.containers = (updateable)
    Asteroid.containers      = (asteroids, updateable, drawable)
    Player.containers        = (updateable, drawable)
    Shot.containers          = (shots, updateable, drawable)
    player                   = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asterfield               = AsteroidField()
    # Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.did_collide(bullet):
                    bullet.kill()
                    asteroid.split()
                    
            if asteroid.did_collide(player):
                print("Game over!")
                sys.exit()
        screen.fill(backcolor)
        for draw_obj in drawable:
            draw_obj.draw(screen)
        pygame.display.flip()

        delta = clock.tick(60)
        dt = delta / 1000


if __name__ == "__main__":
    main()