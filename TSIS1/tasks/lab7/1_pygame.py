import math
import pygame
from datetime import datetime

RESOLUTION = (600, 600)
TICK = 60
DELTA = 1.0 / TICK
SONG_END = pygame.USEREVENT + 1

pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
done = False
clock = pygame.time.Clock()   

font = pygame.font.SysFont("comicsansms", 68)
number = []
for i in range(1, 13):
    number.append(font.render(str(i), True, (64, 64, 64)))
arrow = pygame.image.load('arrow.png')
w, h = arrow.get_size()

def draw_clock(surface):
    text_center = (RESOLUTION[0] // 2 - number[0].get_width() // 1.3, RESOLUTION[1] // 2 - number[0].get_height() // 2)
    center = (RESOLUTION[0] // 2, RESOLUTION[1] // 2)
    gray = (128, 128, 128)
    dark_gray = (64, 64, 64)
    pygame.draw.circle(surface, gray, center, 250)
    pygame.draw.circle(surface, dark_gray, center, 250, 10)

    onesixth = math.pi / 6.0
    angular_offset = math.pi / 4 + math.pi / 10
    dist = 200
    for i in range(12):
        pos = (text_center[0] + math.cos(i * onesixth - angular_offset) * dist, 
               text_center[1] + math.sin(i * onesixth - angular_offset) * dist)
        screen.blit(number[i], pos)
    
def blitRotate(surf, image, pos, originPos, angle):

    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)
  
    # draw rectangle around the image
    # pygame.draw.rect(surf, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()),2)

def draw_hour(surface):
    center = (RESOLUTION[0] // 2, RESOLUTION[1] // 2)

    now = datetime.now()
    seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

    blitRotate(surface, arrow, center, (w // 2, h), -(360 / 12 / 60 / 60) * seconds_since_midnight)

def draw_minutes(surface):
    center = (RESOLUTION[0] // 2, RESOLUTION[1] // 2)

    now = datetime.now()
    seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    scaled = pygame.transform.smoothscale_by(arrow, 1.1)
    blitRotate(surface, scaled, center, (w // 2, h), -(360 / 60 / 60) * seconds_since_midnight)

def draw_seconds(surface):
    center = (RESOLUTION[0] // 2, RESOLUTION[1] // 2)

    now = datetime.now()
    seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    scaled = pygame.transform.smoothscale_by(arrow, 1.3)
    blitRotate(surface, scaled, center, (w // 2, h), -(360 / 60) * seconds_since_midnight)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                
        
        screen.fill((255, 255, 255))
        draw_clock(screen)
        draw_hour(screen)
        draw_minutes(screen)
        draw_seconds(screen)

        pygame.display.flip()
        clock.tick(TICK)