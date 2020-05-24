# -*- coding: utf-8 -*-

import simple_draw as sd
# TODO сделать и выбор фигуры и выбор цвета
# TODO доработать и сделать рефактор, избавится от elif


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

shape_list = ['triangle', 'square', 'hexagon', 'pentagon']


def draw_shapes(start_point=sd.get_point(100, 100), angle=0, *, step, length, color=sd.COLOR_YELLOW):
    shapes_sides = None
    next_start_point = start_point
# ниже из суммы углов вычетается 1 шаг =  1 углу, так как последняя сторона рисуется отдельно из-за проблемы округления
    for step in range(angle, 360 - step, step):
        shapes_sides = sd.get_vector(start_point=next_start_point, angle=step, length=length, width=5)
        shapes_sides.draw(color=color)
        next_start_point = shapes_sides.end_point
    sd.line(start_point=start_point, end_point=shapes_sides.end_point, width=5, color=color)


for index, shape in enumerate(shape_list):
    print(index, ':', shape)

while True:
    user_shape = int(input('please enter a figure number > '))
    if 0 <= user_shape <= len(shape_list) - 1:
        break
    print('incorrect number')


def triangle(start_point=sd.get_point(500, 200), angle=30, length=100):
    """Draw triangle from start point and angle"""
    draw_shapes(start_point=start_point, angle=angle, step=120, length=length)


def square(start_point=sd.get_point(200, 200), angle=30, length=100):
    """Draw square from start point and angle"""
    draw_shapes(start_point=start_point, step=90, length=length, angle=angle)


def pentagon(start_point=sd.get_point(200, 500), angle=30, length=100):
    """Draw pentagon from start point and angle"""
    draw_shapes(start_point=start_point, step=72, length=length, angle=angle)


def hexagon(start_point=sd.get_point(600, 500), angle=30, length=100):
    """Draw hexagon from start point and angle"""
    draw_shapes(start_point=start_point, step=60, length=length, angle=angle)


new_start_point = sd.get_point(300, 200)
if user_shape == 0:
    triangle(start_point=new_start_point)
elif user_shape == 1:
    square(start_point=new_start_point)
elif user_shape == 2:
    hexagon(start_point=new_start_point)
elif user_shape == 3:
    pentagon(start_point=new_start_point)


sd.pause()
