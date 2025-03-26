import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    shape = 'freehand'  # new: default shape mode
    points = []
    shapes = []  # Store drawn shapes
    start_pos = None  # Store start position for shapes
    color = (0, 0, 255)
    font_small = pygame.font.SysFont("Verdana", 20)
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # Color selection
                if event.key == pygame.K_r:
                    mode = 'red'
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    mode = 'green'
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    mode = 'blue'
                    color = (0, 0, 255)
                elif event.key == pygame.K_e:  # Eraser
                    mode = 'eraser'
                    color = (0, 0, 0)

                # Shape selection
                if event.key == pygame.K_f:
                    shape = 'freehand'
                    radius = 15
                elif event.key == pygame.K_c:
                    shape = 'circle'
                elif event.key == pygame.K_l:
                    shape = 'rectangle'
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos  # Store start position for shape drawing

            if event.type == pygame.MOUSEMOTION:
                if shape == 'freehand' and pygame.mouse.get_pressed()[0]:
                    position = event.pos
                    points.append((position, color, radius))
                    points = points[-256:]

            if event.type == pygame.MOUSEBUTTONUP:
                end_pos = event.pos
                if shape == 'rectangle':
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    rect_x = min(x1, x2)
                    rect_y = min(y1, y2)
                    rect_width = abs(x2 - x1)
                    rect_height = abs(y2 - y1)
                    shapes.append(('rectangle', (rect_x, rect_y, rect_width, rect_height), color))
                elif shape == 'circle':
                    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                    radius = max(abs(end_pos[0] - start_pos[0]) // 2, abs(end_pos[1] - start_pos[1]) // 2)
                    shapes.append(('circle', center, radius, color))

        screen.fill((0, 0, 0))
        for pos, c, r in points:
            pygame.draw.circle(screen, c, pos, r)
        
        for shape_data in shapes:
            if shape_data[0] == 'rectangle':
                pygame.draw.rect(screen, shape_data[2], shape_data[1])
            elif shape_data[0] == 'circle':
                pygame.draw.circle(screen, shape_data[3], shape_data[1], shape_data[2])
        
        shapetext = font_small.render(str(shape), True, (255, 255, 255))
        screen.blit(shapetext, (0,0))

        pygame.display.flip()
        clock.tick(60)


main()
