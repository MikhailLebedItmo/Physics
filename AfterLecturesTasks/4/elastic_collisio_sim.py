import pygame
import pymunk
import pymunk.pygame_util
import math
from random import randint

DEBUG = False


# Входные параметры
if not DEBUG:
    mass1 = float(input("Введите массу первого тела: "))
    mass2 = float(input("Введите массу второго тела: "))
    v1 = float(input("Введите скорость первого тела: "))
    v2 = float(input("Введите скорость второго тела: "))
    angle1 = math.radians(float(input("Введите угол первого тела (градусы): ")))
    angle2 = math.radians(float(input("Введите угол второго тела (градусы): ")))
    width = int(input("Введите ширину оболочки(целое положительное число): "))
    height = int(input("Введите высоту оболочки(целое положительное число): "))
else:
    mass1 = 50
    mass2 = 10
    v1 = 1000
    v2 = 2000
    angle1 = 60
    angle2 = 45
    width = 5000
    height = 3000


scale = 900 / max(width, height)
width = int(scale * width)
height = int(scale * height)
v1 = int(scale * v1)
v2 = int(scale * v2)

# Инициализация Pygame и Pymunk
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 0)
draw_options = pymunk.pygame_util.DrawOptions(screen)
pygame.display.set_caption("Симуляция абсолютно упругого соударения")


# Создание прямоугольной оболочки
static_lines = [
    pymunk.Segment(space.static_body, (0, 0), (width, 0), 1),  # Верх
    pymunk.Segment(space.static_body, (0, height), (width, height), 1),  # Низ
    pymunk.Segment(space.static_body, (0, 0), (0, height), 1),  # Левая стена
    pymunk.Segment(space.static_body, (width, 0), (width, height), 1)  # Правая стена
]
for line in static_lines:
    line.elasticity = 1.0
space.add(*static_lines)


# Функция для создания круга
def create_body(mass, radius, pos, velocity):
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    body.position = pos
    body.velocity = velocity
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 1.0
    space.add(body, shape)
    return shape


# Создание тел с разными начальными скоростями
if mass1 > mass2:
    radius1, radius2 = 30, 20  # Радиусы
elif mass2 > mass1:
    radius1, radius2 = 20, 30
else:
    radius1, radius2 = 30, 30

pos1 = (randint(15, width - 15), randint(15, height - 15))
pos2 = (randint(15, width - 15), randint(15, height - 15))
body1 = create_body(mass1, radius1, pos1, (v1 * math.cos(angle1), v1 * math.sin(angle1)))
body2 = create_body(mass2, radius2, pos2, (v2 * math.cos(angle2), v2 * math.sin(angle2)))

# Основной цикл симуляции
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    space.step(1 / 60)
    space.debug_draw(draw_options)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
