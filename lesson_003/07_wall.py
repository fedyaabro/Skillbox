# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (1000, 800)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

wall_width = 700
wall_height = 700
brick_width = 100
brick_height = 50

# TODO сделать так, чтобы куски кирпичей не вылезали за пределы стены

left_bottom_wall = sd.get_point(100, 100)
right_top_wall = sd.get_point(wall_width, wall_height)
sd.rectangle(left_bottom=left_bottom_wall, right_top=right_top_wall, width=1)
brick_shift_index = 0
for brick_y in range(100, wall_height, brick_height):
    for brick_x in range(100, wall_width, brick_width):
        if brick_shift_index % 2 == 0:
            left_bottom = sd.get_point(brick_x, brick_y)
            right_top = sd.get_point(brick_x + brick_width, brick_height + brick_y)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=2)
        else:
            left_bottom = sd.get_point(brick_x - (brick_width * 0.5), brick_y)
            right_top = sd.get_point(brick_x + (brick_width * 0.5), brick_height + brick_y)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=2)
    brick_shift_index += 1
sd.pause()
