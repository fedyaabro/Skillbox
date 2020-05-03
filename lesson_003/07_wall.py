# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# TODO увеличил размер окна, а то он меньше размера стены
sd.resolution = (1000, 800)


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

wall_width = 650  # TODO изменил ширину стены. тем самым сломав тебе программу. Исправляй!!!
wall_height = 700
brick_width = 100
brick_height = 50

# TODO сделал границы стены
left_bottom_wall = sd.get_point(0, 0)
right_top_wall = sd.get_point(wall_width, wall_height)
sd.rectangle(left_bottom=left_bottom_wall, right_top=right_top_wall, width=1)

for brick_x in range(0, wall_width, brick_width):
    left_bottom = sd.get_point(brick_x, 0)
    right_top = sd.get_point(brick_width + brick_x, brick_height)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1)

sd.pause()
