# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (600, 600)  # TODO зачем эта строка

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

wall_width = 700
wall_height = 700
brick_width = 100
brick_height = 50

for brick_x in range(0, wall_width, brick_width):
    left_bottom = sd.get_point(brick_x, 0)
    right_top = sd.get_point(brick_width, brick_height)  # TODO почему тут brick_width
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1)

# TODO перед тем как показывать код, нужно убедится, что ты вообще понимаешь каждую строчку, что она выполняет и тд.
# TODO пока у тебя ошибки аля поделки подделки
sd.pause()
