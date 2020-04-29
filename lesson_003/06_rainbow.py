# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# x_start, x_end = 50, 450
# step = 5
# i = 0
# for _ in rainbow_colors:
#     start = sd.get_point(x_start, 50)
#     end = sd.get_point(x_end, 550)
#     sd.line(start_point=start, end_point=end, color=rainbow_colors[i], width=5)
#     i += 1
#     x_start += step
#     x_end += step

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
point = sd.get_point(500, 0)
radius = 300
i = 0
for _ in rainbow_colors:
    radius += 30
    sd.circle(center_position=point, radius=radius, color=rainbow_colors[i], width=30)
    i += 1
sd.pause()
