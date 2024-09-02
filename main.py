import pygame
from constants import * 
from player import *

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
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        dt = pyClock.tick(60) / 1000
        screen.fill(color)
        #dt = returnValue / 1000
         
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
if __name__ == "__main__":
    main()
