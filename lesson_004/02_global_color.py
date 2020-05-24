# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

sd.resolution = (1200, 800)

colors_list = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']

colors = {'red': sd.COLOR_RED,
          'orange': sd.COLOR_ORANGE,
          'yellow': sd.COLOR_YELLOW,
          'green': sd.COLOR_GREEN,
          'cyan': sd.COLOR_CYAN,
          'blue': sd.COLOR_BLUE,
          'purple': sd.COLOR_PURPLE}


def draw_shapes(start_point=sd.get_point(100, 100), angle=0, *, step, length, color=sd.COLOR_YELLOW):
    shapes_sides = None
    next_start_point = start_point
# ниже из суммы углов вычетается 1 шаг = угол, так как последняя сторона рисуется отдельно из-за проблемы округления
    for step in range(angle, 360 - step, step):
        shapes_sides = sd.get_vector(start_point=next_start_point, angle=step, length=length, width=5)
        shapes_sides.draw(color=color)
        next_start_point = shapes_sides.end_point
    sd.line(start_point=start_point, end_point=shapes_sides.end_point, width=5, color=color)


for index, color in enumerate(colors_list):
    print(index, ':', color)

while True:
    user_color = int(input('please enter a color number > '))
    if 0 <= user_color <= len(colors) - 1:
        break
    print('incorrect number')

color = colors[colors_list[user_color]]


def triangle(start_point=sd.get_point(500, 200), angle=30, length=100):
    """Draw triangle from start point and angle"""
    draw_shapes(start_point=start_point, angle=angle, step=120, length=length, color=color)


def square(start_point=sd.get_point(200, 200), angle=30, length=100):
    """Draw square from start point and angle"""
    draw_shapes(start_point=start_point, step=90, length=length, angle=angle, color=color)


def pentagon(start_point=sd.get_point(200, 500), angle=30, length=100):
    """Draw pentagon from start point and angle"""
    draw_shapes(start_point=start_point, step=72, length=length, angle=angle, color=color)


def hexagon(start_point=sd.get_point(600, 500), angle=30, length=100):
    """Draw hexagon from start point and angle"""
    draw_shapes(start_point=start_point, step=60, length=length, angle=angle, color=color)


triangle()
pentagon()
hexagon()
square()

sd.pause()
