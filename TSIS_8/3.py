import pygame
import random
import math

# Making canvas
screen = pygame.display.set_mode((900, 700))

# Setting Title
pygame.display.set_caption('My Paint App')

draw_on = False
last_pos = (0, 0)
eraser_width = 50
# Radius of the Brush
radius = 5

# My code
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

COLOR_BUTTONS = [
    {"color": RED, "rect": pygame.Rect(10, 10, 50, 50)},
    {"color": WHITE, "rect": pygame.Rect(70, 10, 50, 50)},
    {"color": YELLOW, "rect": pygame.Rect(130, 10, 50, 50)},
    {"color": GREEN, "rect": pygame.Rect(190, 10, 50, 50)},
    {"color": BLUE, "rect": pygame.Rect(250, 10, 50, 50)},
    {"color": PURPLE, "rect": pygame.Rect(310, 10, 50, 50)}
]

eraser_image = pygame.image.load('pngtree-grey-road-cartoon-illustration-image_1447103.png')
eraser_image_resized = pygame.transform.scale(eraser_image, (eraser_width, eraser_width))

eraser_rect = pygame.Rect(360, 10, 50, 50)

draw_rect = False

def draw_rect(canvas, color, rect_start_pos, rect_end_pos, radius=1):
    pygame.draw.rect(canvas, color, (rect_start_pos[0], rect_end_pos[0]))

def roundline(canvas, color, start, end, radius=1):
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist):
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)

selected_color = WHITE

def draw_eraser(canvas, color, start, end):
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(canvas, color, rect, 2)

def draw_circle(canvas, color, center, radius):
    pygame.draw.circle(canvas, color, center, radius)

def draw_rectangle(canvas, color, start, end):
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(canvas, color, rect, 2)

def draw_triangle(canvas, color, start, end):
    x1, y1 = start
    x2, y2 = end
    x3 = x1
    y3 = y2
    pygame.draw.polygon(canvas, color, [(x1, y1), (x2, y2), (x3, y3)])

try :
    while True :
        event = pygame.event.wait()

        if event.type == pygame.QUIT :
            raise StopIteration

        if event.type == pygame.MOUSEBUTTONDOWN :
            if eraser_rect.collidepoint(event.pos):
                selected_color = BLACK
            for button in COLOR_BUTTONS:
                if button["rect"].collidepoint(event.pos):
                    selected_color = button['color']

            if event.button == 1: 
                start_pos = event.pos
                shape_type = 'circle'
            elif event.button == 3: 
                start_pos = event.pos
                shape_type = 'rectangle'
            elif event.button == 2: 
                start_pos = event.pos
                shape_type = 'triangle'

        if event.type == pygame.MOUSEBUTTONUP :
            draw_on = False

            if shape_type == 'circle':
                end_pos = event.pos
                distance = math.hypot(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
                draw_circle(screen, selected_color, start_pos, int(distance))
            elif shape_type == 'rectangle':
                end_pos = event.pos
                draw_rectangle(screen, selected_color, start_pos, end_pos)
            elif shape_type == 'triangle':
                end_pos = event.pos
                draw_triangle(screen, selected_color, start_pos, end_pos)
            elif shape_type == 'eraser':
                end_pos = event.pos
                draw_rectangle(screen, (0, 0, 0), start_pos, end_pos)

        if event.type == pygame.MOUSEMOTION :
            if draw_on :
                pygame.draw.circle(screen, selected_color, event.pos, radius)
                roundline(screen, selected_color, event.pos, last_pos, radius)
            last_pos = event.pos
        for button in COLOR_BUTTONS:
            pygame.draw.rect(screen, button["color"], button["rect"])

        pygame.display.flip()

except StopIteration :
    pass

# Quit
pygame.quit()
