# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
from sys import argv


def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}

    with open(config_filename, 'r') as f:
        for line in f:
            if line.startswith("interface"):
                _, intf = line.split()
                continue
            if "allowed vlan" in line:
                trunk_dict[intf] = [int(vlan)
                                    for vlan in line.split()[4].split(",")]
                continue
            if "access vlan" in line:
                access_dict[intf] = int(line.split()[3])

    return access_dict, trunk_dict


if __name__ == "__main__":
    access, trunk = get_int_vlan_map(argv[1])
    print(access)
    print(trunk)
