import pygame
import sys
from constants import * 
from player import *
from asteroid import Asteroid 
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0,0,0)
    dt = 0
    pyClock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)

    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    
    #player.add(updatable)
    #player.add(drawable)

    #Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(color)
        #dt = returnValue / 1000
        for objct in updatable:
            objct.update(dt)
        dt = pyClock.tick(60) / 1000
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game o-v-v-v-v-v-er!")
                sys.exit()

        for shot in shots:
            if any(asteroid.collides_with(shot) for asteroid in asteroids):
                shot.kill()
                for asteroid in asteroids:
                    if asteroid.collides_with(shot):
                        asteroid.kill()
                        asteroid.split() 

        for thing in drawable:
            thing.draw(screen)

        player.update(dt)
        player.draw(screen)
        pygame.display.flip() 
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
