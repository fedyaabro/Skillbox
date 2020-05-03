# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# TODO sd.resolution убрал, требований по размеру экрана нет + в этой роли переменные wall_width и wall_height

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

wall_width = 700
wall_height = 700
brick_width = 100
brick_height = 50

for brick_x in range(0, wall_width, brick_width):
    left_bottom = sd.get_point(brick_x, 0)
    right_top = sd.get_point(brick_width + brick_x, brick_height)
    # TODO координаты верхней правой точки = x + ширина кирвича, y + высота кирпича, поторопился и наебался
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1)

# TODO пока у тебя ошибки аля поделки подделки - четкая кепка. Теперь строится нижний ряд нормально
sd.pause()
