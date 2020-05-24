# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (1200, 800)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,


# def draw_branches(start_point=sd.get_point(300, 10), angle=30, length=50):
#     branch_1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
#     branch_1.draw()
#     branch_2 = sd.get_vector(start_point=start_point, angle=angle + 120, length=length)
#     branch_2.draw()


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# def draw_many_branches(start_point, angle, length):
#     """Draw a tree"""
#     if length < 5:
#         return
#     branch_1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
#     branch_1.draw()
#     branch_2 = sd.get_vector(start_point=start_point, angle=angle + 60, length=length)
#     branch_2.draw()
#     next_length = length * .75
#     draw_many_branches(start_point=branch_1.end_point, angle=angle - 20, length=next_length)
#     draw_many_branches(start_point=branch_2.end_point, angle=angle + 20, length=next_length)


# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

def draw_many_branches(start_point, angle, length):
    """Draw a tree"""
    if length < 5:
        return
    branch_1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
    branch_1.draw()
    branch_2 = sd.get_vector(start_point=start_point, angle=angle + 60, length=length)
    branch_2.draw()
    random_deflection_1 = random.randint(18, 48)
    # random_deflection_2 = random.randint(18, 48)
    random_length_index = random.uniform(0.60, 0.90)
    next_length = length * random_length_index
    draw_many_branches(start_point=branch_1.end_point, angle=angle - random_deflection_1, length=next_length)
    draw_many_branches(start_point=branch_2.end_point, angle=angle + random_deflection_1, length=next_length)


branch_start_point = sd.get_point(600, 50)
trunk_start_point = sd.get_point(600, 0)
trunk = sd.line(start_point=trunk_start_point, end_point=branch_start_point)
draw_many_branches(start_point=branch_start_point, angle=60, length=150)
sd.pause()
