# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
from sys import argv
from pprint import pprint


def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}

    with open(config_filename, 'r') as f:
        intf = ""
        for line in f:
            if line.startswith("interface"):
                if intf != "" and not(access_dict.get(intf) or trunk_dict.get(intf)):
                    access_dict[intf] = 1
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
    result = get_int_vlan_map(argv[1])
    pprint(result)