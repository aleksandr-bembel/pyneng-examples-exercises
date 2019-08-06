# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import subprocess


def ping_ip_addresses(ip_list):
    reachable_list = []
    unreachable_list = []

    for ip in ip_list:
        result = subprocess.run(
            f'ping -c 5 {ip}', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if result.returncode == 0:
            reachable_list.append(ip)
        else:
            unreachable_list.append(ip)
    return reachable_list, unreachable_list


if __name__ == "__main__":
    test_list = ['8.8.8.8', '8.8.4.4', '10.54.14.1']
    print(ping_ip_addresses(test_list))
