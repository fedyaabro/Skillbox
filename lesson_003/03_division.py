# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# с a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 142523, 4435

while a > b:
    result = int(a / b)
    print('Целочисленное деление', a, 'на', b, 'дает', result)
    break
else:
    print('некорректный ввод')