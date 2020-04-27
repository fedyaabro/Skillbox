# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

if month == 1:
    days_on_month = 31
    print('Колличество дней в этом месяце', days_on_month)
elif month == 2:
    days_on_month = 28
    print('Колличество дней в этом месяце', days_on_month)
elif month == 3:
    days_on_month = 31
    print('Колличество дней в этом месяце', days_on_month)
elif month == 4:
    days_on_month = 30
    print('Колличество дней в этом месяце', days_on_month)
elif month == 5:
    days_on_month = 31
    print('Колличество дней в этом месяце', days_on_month)
elif month == 6:
    days_on_month = 30
    print('Колличество дней в этом месяце', days_on_month)
elif month == 7:
    days_on_month = 31
    print('Колличество дней в этом месяце', days_on_month)
elif month == 8:
    days_on_month = 30
    print('Колличество дней в этом месяце', days_on_month)
elif month == 9:
    days_on_month = 31
    print('Колличество дней в этом месяце', days_on_month)
elif month == 10:
    days_on_month = 30
    print('Колличество дней в этом месяце', days_on_month)
elif month == 11:
    days_on_month = 31
    print('Колличество дней в этом месяце', days_on_month)
elif month == 12:
    days_on_month = 30
    print('Колличество дней в этом месяце', days_on_month)
else:
    print('Неправильный месяц')


