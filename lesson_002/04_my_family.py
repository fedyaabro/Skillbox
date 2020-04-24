#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:
from pprint import pprint
# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mother', 'father', 'me']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    [my_family[0], 153],
    [my_family[1], 178],
    [my_family[2], 191],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('father height = ', my_family_height[1][1])
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

total_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1]
print(total_height)