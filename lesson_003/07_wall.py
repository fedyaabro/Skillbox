# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (600, 600)



# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

wall_width = 700
wall_height = 700
brick_width = 100
brick_height = 50

for brick_x in range(0, wall_width, brick_width):
    left_bottom = sd.get_point(brick_x, 0)
    right_top = sd.get_point(brick_width, brick_height)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1)
# жду твои тудушки, можешь считать себя прорабом





sd.pause()
