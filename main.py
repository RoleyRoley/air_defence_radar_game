# Handles game loop, rendering, and overall game state.

import pygame
import radar
import target
import tracking



# call radar
#radar = radar()

# call target
#target = target()

# call tracking
#tracking = tracking()



# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Radar game")
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(500, 400)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "green", player_pos, radar.radius, 1)  # draw radar range
    #radar.draw(screen, player_pos)  # draw radar sweep

    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    
    
    radar.update(dt)
    target.update(dt)
    detections = radar.detect(target)
    tracking.update(detections, dt)

pygame.quit()