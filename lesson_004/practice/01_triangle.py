# -*- coding: utf-8 -*-

# pip install simple_draw

import simple_draw as sd


# нарисовать треугольник из точки (300, 300) с длиной стороны 200
# length = 200
# angle = 0
# point = sd.get_point(300, 300)
# side_1 = sd.get_vector(start_point=point, angle=angle, length=200)
# side_1.draw()
# side_2 = sd.get_vector(start_point=side_1.end_point, angle=angle + 120, length=200)
# side_2.draw()
# side_3 = sd.get_vector(start_point=side_2.end_point, angle=angle + 240, length=200)
# side_3.draw()


# определить функцию рисования треугольника из заданной точки с заданным наклоном
def triangle(start_point=sd.get_point(200, 200), angle=0):
    for angle in range(0, 360, 120):
        side = sd.get_vector(start_point=start_point, angle=angle)
        side.draw()
        start_point = side.end_point


triangle()

sd.pause()
