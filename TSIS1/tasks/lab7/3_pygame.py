
import pygame

RESOLUTION = (400, 400)
TICK = 60
DELTA = 1.0 / TICK

pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
done = False
clock = pygame.time.Clock()           

# NO BUILTIN CLAMP ?????
# ?????
# PYTHON ?????
def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

class Input():
       def get_axis():
              pressed = pygame.key.get_pressed()
              hor = pressed[pygame.K_RIGHT] - pressed[pygame.K_LEFT]
              ver = pressed[pygame.K_DOWN] - pressed[pygame.K_UP]
              return (hor, ver)

class Player():
    position = (0, 0)
    color = None
    radius = 0
    speed = 0
    def __init__(self, position, color, radius, speed):
            self.position = position
            self.color = color
            self.radius = radius
            self.speed = speed
    
    def update(self, surface):

            axis = Input.get_axis()
            self.set_position((self.position[0] + axis[0] * self.speed, 
                               self.position[1] + axis[1] * self.speed))
            
            self.set_position((clamp(self.position[0], self.radius, RESOLUTION[0] - self.radius), 
                               clamp(self.position[1], self.radius, RESOLUTION[1] - self.radius)))

            pygame.draw.circle(surface, self.color, self.position, self.radius)

    def set_position(self, new_pos):
           self.position = new_pos
    
    def get_position(self):
           return self.position

player = Player((RESOLUTION[0] / 2, RESOLUTION[1] / 2), (255, 0, 0), 25, 20)
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        screen.fill((255, 255, 255))
        player.update(screen)
        
        pygame.display.flip()
        clock.tick(TICK)