# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
'''

import tabulate


def print_ip_table(reachable_list, unreachable_list):
    print(tabulate.tabulate({"Reachable": reachable_list, "Unreachable": unreachable_list}, headers="keys"))

    return None


if __name__ == "__main__":
    reachable_list = ["10.1.1.1", "10.1.1.2"]
    unreachable_list = ["10.1.1.7", "10.1.1.8", "10.1.1.9"]
    print_ip_table(reachable_list, unreachable_list)
