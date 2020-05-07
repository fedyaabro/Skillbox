# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random

sd.resolution = (1200, 800)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def draw_the_boy_who_alive(x, y, color=sd.COLOR_YELLOW):
    """Draw boy with scar in point(x, y)"""

    # голова и глаза
    head_center = sd.get_point(x, y)
    sd.circle(center_position=head_center, radius=100, width=2, color=color)
    left_eye_center = sd.get_point(x - 30, y + 25)
    sd.circle(center_position=left_eye_center, radius=15, color=color)
    right_eye_center = sd.get_point(x + 30, y + 25)
    sd.circle(center_position=right_eye_center, radius=15, color=color)

    # нос
    end_nose = sd.get_point(x, y - 20)
    sd.line(start_point=head_center, end_point=end_nose, width=1, color=color)

    # рот
    mouth_center = sd.get_point(x, y - 60)  # 200, 140
    smoothing_mouth_point = sd.get_point(x + 50, y - 50)
    right_end_of_mouth = sd.get_point(x - 50, y - 50)
    left_end_of_mouth = sd.get_point(x + 50, y - 50)
    mouth_point_list = (right_end_of_mouth,
                        mouth_center,
                        smoothing_mouth_point,
                        left_end_of_mouth)
    sd.lines(point_list=mouth_point_list, closed=True, width=2, color=color)

    # дужки очков
    start_left_tempera = sd.get_point(x - 45, y + 25)
    end_left_tempera = sd.get_point(x - 90, y + 30)
    start_right_tempera = sd.get_point(x + 45, y + 25)
    end_right_tempera = sd.get_point(x + 90, y + 30)
    start_middle_tempera = sd.get_point(x + 15, y + 25)
    end_middle_tempera = sd.get_point(x - 15, y + 25)
    sd.line(start_point=start_left_tempera, end_point=end_left_tempera, color=color)
    sd.line(start_point=start_right_tempera, end_point=end_right_tempera, color=color)
    sd.line(start_point=start_middle_tempera, end_point=end_middle_tempera, color=color)

    # шрам
    scar_start = sd.get_point(x - 20, y + 70)
    scar_point_1 = sd.get_point(x - 30, y + 70)
    scar_point_2 = sd.get_point(x - 40, y + 50)
    end_of_scar = sd.get_point(x - 50, y + 50)

    scar_points_list = (scar_start,
                        scar_point_1,
                        scar_point_2,
                        end_of_scar)
    sd.lines(point_list=scar_points_list, closed=False, width=2, color=color)

    # волосы
    hair_start = sd.get_point(x - 30, y + 95)
    hair_point_1 = sd.get_point(x - 30, y + 120)
    hair_point_2 = sd.get_point(x - 10, y + 100)
    hair_point_3 = sd.get_point(x, y + 120)
    hair_point_4 = sd.get_point(x + 20, y + 95)
    hair_point_5 = sd.get_point(x + 30, y + 120)
    end_of_hair = sd.get_point(x + 40, y + 90)

    hairs_points_list = (hair_start,
                         hair_point_1,
                         hair_point_2,
                         hair_point_3,
                         hair_point_4,
                         hair_point_5,
                         end_of_hair)
    sd.lines(point_list=hairs_points_list, closed=False, width=2, color=color)


for _ in range(10):
    draw_the_boy_who_alive(sd.random_number(0, sd.resolution[0]), sd.random_number(0, sd.resolution[1]))

sd.pause()
