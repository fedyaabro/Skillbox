# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)


def draw_shapes(start_point=sd.get_point(100, 100), incline_angle=0, *, step, length):
    global shapes_sides
    next_start_point = start_point
# ниже из суммы углов вычетается 1 шаг = угол, так как последняя сторона рисуется отдельно из-за проблемы округления
    for step in range(incline_angle, 360 - step, step):
        shapes_sides = sd.get_vector(start_point=next_start_point, angle=step, length=length)
        shapes_sides.draw()
        next_start_point = shapes_sides.end_point
    sd.line(start_point=start_point, end_point=shapes_sides.end_point, width=1)


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

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника


# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Ответ: очень много монотонной работы

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!



# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# another long way triangle
# side_1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
# side_1.draw()
# side_2 = sd.get_vector(start_point=side_1.end_point, angle=angle + 120, length=length)
# side_2.draw()
# sd.line(start_point=side_2.end_point, end_point=side_1.start_point)


# another long way square
# side_1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
# side_1.draw()
# side_2 = sd.get_vector(start_point=side_1.end_point, angle=angle + 90, length=length)
# side_2.draw()
# side_3 = sd.get_vector(start_point=side_2.end_point, angle=angle + 180, length=length)
# side_3.draw()
# sd.line(start_point=side_3.end_point, end_point=side_1.start_point)


# another long way pentagon
# side_1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
# side_1.draw()
# side_2 = sd.get_vector(start_point=side_1.end_point, angle=angle + 72, length=length)
# side_2.draw()
# side_3 = sd.get_vector(start_point=side_2.end_point, angle=angle + 144, length=length)
# side_3.draw()
# side_4 = sd.get_vector(start_point=side_3.end_point, angle=angle + 216, length=length)
# side_4.draw()
# sd.line(start_point=side_4.end_point, end_point=side_1.start_point)


# another long way hexagon
# side_1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
# side_1.draw()
# side_2 = sd.get_vector(start_point=side_1.end_point, angle=angle + 60, length=length)
# side_2.draw()
# side_3 = sd.get_vector(start_point=side_2.end_point, angle=angle + 120, length=length)
# side_3.draw()
# side_4 = sd.get_vector(start_point=side_3.end_point, angle=angle + 180, length=length)
# side_4.draw()
# side_5 = sd.get_vector(start_point=side_4.end_point, angle=angle + 240, length=length)
# side_5.draw()
# sd.line(start_point=side_5.end_point, end_point=side_1.start_point)

