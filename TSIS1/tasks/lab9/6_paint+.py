import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    shape = 'freehand'  # Currently selected shape
    points = []  # Lines for freehand drawing
    shapes = []  # List of saved shapes
    start_pos = None  # Start position for drawing shapes
    color = (0, 0, 255)  # Default color
    font_small = pygame.font.SysFont("Verdana", 20)
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key in {pygame.K_w, pygame.K_F4, pygame.K_ESCAPE} and (ctrl_held or alt_held):
                    return
                
                # Color selection
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)
                
                # Shape selection
                if event.key == pygame.K_f:
                    shape = 'freehand'
                elif event.key == pygame.K_c:
                    shape = 'circle'
                elif event.key == pygame.K_l:
                    shape = 'rectangle'
                elif event.key == pygame.K_s:
                    shape = 'square'
                elif event.key == pygame.K_t:
                    shape = 'triangle'
                elif event.key == pygame.K_y:
                    shape = 'right_triangle'
                elif event.key == pygame.K_d:
                    shape = 'rhombus'
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos  # Store start position
                
            if event.type == pygame.MOUSEMOTION and event.buttons[0]:  
                if shape == 'freehand':
                    points.append((event.pos, color))
                    points = points[-256:]
                
            if event.type == pygame.MOUSEBUTTONUP and start_pos is not None:
                end_pos = event.pos
                
                if shape == 'rectangle':
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    shapes.append(('rectangle', pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), color))
                elif shape == 'square':
                    size = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    shapes.append(('rectangle', pygame.Rect(start_pos[0], start_pos[1], size, size), color))
                elif shape == 'circle':
                    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                    radius = max(abs(end_pos[0] - start_pos[0]) // 2, abs(end_pos[1] - start_pos[1]) // 2)
                    shapes.append(('circle', center, radius, color))
                elif shape == 'triangle':
                    x, y = start_pos
                    size = abs(end_pos[0] - x)
                    shapes.append(('polygon', [(x, y), (x + size, y), (x + size // 2, y - int(size * 0.866))], color))
                elif shape == 'right_triangle':
                    x, y = start_pos
                    shapes.append(('polygon', [(x, y), (end_pos[0], y), (x, end_pos[1])], color))
                elif shape == 'rhombus':
                    x, y = start_pos
                    dx = abs(end_pos[0] - x) // 2
                    dy = abs(end_pos[1] - y) // 2
                    shapes.append(('polygon', [(x, y - dy), (x + dx, y), (x, y + dy), (x - dx, y)], color))
                
        screen.fill((0, 0, 0))  # Clear screen
        
        for pos, c in points:
            pygame.draw.circle(screen, c, pos, 3)
        
        for shape_data in shapes:
            if shape_data[0] == 'rectangle':
                pygame.draw.rect(screen, shape_data[2], shape_data[1])
            elif shape_data[0] == 'circle':
                pygame.draw.circle(screen, shape_data[3], shape_data[1], shape_data[2])
            elif shape_data[0] == 'polygon':
                pygame.draw.polygon(screen, shape_data[2], shape_data[1])
        
        shapetext = font_small.render(str(shape), True, (255, 255, 255))
        screen.blit(shapetext, (10, 10))

        pygame.display.flip()
        clock.tick(60)

main()
