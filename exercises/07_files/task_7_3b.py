# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from operator import itemgetter

vlan_num = int(input('Введите номер VLAN для выборки: '))

list = []
with open("CAM_table.txt",'r') as f:
    for line in f:
        if 'DYNAMIC' in line:
            vlan, mac, _, intf = line.split()
            vlan=int(vlan)
            if vlan_num == vlan:
                list.append((int(vlan),mac,intf))

list.sort(key=itemgetter(0))
for line in list:
    vlan, mac, intf = line
    print("{:<7} {} {:>7}".format(vlan, mac, intf))