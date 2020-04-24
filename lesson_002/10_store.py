#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

# table_id = goods['Стол']
# table_items_1 = store[table_id][0]
# table_items_2 = store[table_id][1]
# tables_quantity_1 = table_items_1['quantity']
# tables_quantity_2 = table_items_2['quantity']
# total_tables_quantity = tables_quantity_1 + tables_quantity_1
# tables_price_1 = table_items_1['price']
# tables_price_2 = table_items_2['price']
# total_tables_price = tables_price_1 + tables_price_2
#
# tables_result = total_tables_quantity * total_tables_price
# print(tables_result)


# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.


# диваны
sofas_cost_1 = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
sofas_cost_2 = store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
total_sofas_cost = sofas_cost_1 + sofas_cost_2
total_sofas_quantity = store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity']

# стулья


chairs_cost_1 = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
chairs_cost_2 = store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']
chairs_cost_3 = store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']
total_chairs_cost = chairs_cost_1 + chairs_cost_2 + chairs_cost_3
total_chairs_quantity = store[goods['Стул']][0]['quantity'] + store[goods['Стул']][1]['quantity']

# столы


tables_cost_1 = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
tables_cost_2 = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
total_table_cost = tables_cost_1 + tables_cost_2
total_tables_quantity = store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1]['quantity']

print('Столы - ', total_tables_quantity, 'шт, стоимость: ', total_table_cost, 'руб')
print('Диваны - ', total_sofas_quantity, 'шт, стоимость: ', total_sofas_cost, 'руб')
print('Стулья - ', total_chairs_quantity, 'шт, стоимость: ', total_chairs_cost, 'руб')


##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################


#
# lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# # или проще (/сложнее ?)
# lamp_code = goods['Лампа']
# lamps_item = store[lamp_code][0]
# lamps_quantity = lamps_item['quantity']
# lamps_price = lamps_item['price']
# lamps_cost = lamps_quantity * lamps_price
# print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')
