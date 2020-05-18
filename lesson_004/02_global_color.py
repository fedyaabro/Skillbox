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
colors = (sd.COLOR_RED,
          sd.COLOR_ORANGE,
          sd.COLOR_YELLOW,
          sd.COLOR_GREEN,
          sd.COLOR_CYAN,
          sd.COLOR_BLUE,
          sd.COLOR_PURPLE)

user_color = int(input("""Please, enter color number:
                       0: COLOR_RED
                       1: COLOR_ORANGE
                       2: COLOR_YELLOW
                       3: COLOR_GREEN
                       4: COLOR_CYAN
                       5: COLOR_BLUE
                       6: COLOR_PURPLE
                       """))


def draw_shapes(start_point=sd.get_point(100, 100), incline_angle=0, *, step, length, color=colors[user_color]):
    shapes_sides = None
    next_start_point = start_point
    # ниже из суммы углов вычетается 1 шаг = угол, так как последняя сторона рисуется отдельно из-за проблемы округления
    for step in range(incline_angle, 360 - step, step):
        shapes_sides = sd.get_vector(start_point=next_start_point, angle=step, length=length)
        shapes_sides.draw(color=color)
        next_start_point = shapes_sides.end_point
    sd.line(start_point=start_point, end_point=shapes_sides.end_point, width=1, color=color)


def triangle(start_point=sd.get_point(500, 200), angle=0, length=100):
    """Draw triangle from start point and angle"""
    draw_shapes(start_point=start_point, incline_angle=angle, step=120, length=length)


def square(start_point=sd.get_point(200, 200), angle=0, length=100):
    """Draw square from start point and angle"""
    draw_shapes(start_point=start_point, step=90, length=length, incline_angle=angle)


def pentagon(start_point=sd.get_point(200, 500), angle=0, length=100):
    """Draw pentagon from start point and angle"""
    draw_shapes(start_point=start_point, step=72, length=length, incline_angle=angle)


def hexagon(start_point=sd.get_point(600, 500), angle=0, length=100):
    """Draw hexagon from start point and angle"""
    draw_shapes(start_point=start_point, step=60, length=length, incline_angle=angle)


triangle()
pentagon()
hexagon()
square()

sd.pause()
