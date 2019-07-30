# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

while True:
    ip = input('Введите адрес в формате x.y.z.c: ')
    ip_list = [int(i) for i in ip.split('.')]
    correct = True
    for octet in ip_list:
        if octet >= 0 and octet <= 255:
            pass
        else:
            correct = False
    if correct:
        break
    else:
        print("Неправильный IP-адрес")

if correct and len(ip_list) == 4:
    if ip_list[0] >= 1 and ip_list[0] <= 223:
        print("unicast")
    elif ip_list[0] >= 224 and ip_list[0] <= 239:
        print("multicast")
    elif ip_list[0] == 255 and ip_list[1] == 255 and ip_list[2] == 255 and ip_list[3] == 255:
        print("local broadcast")
    elif ip_list[0] == 0 and ip_list[1] == 0 and ip_list[2] == 0 and ip_list[3] == 0:
        print("unassigned")
    else:
        print("unused")
