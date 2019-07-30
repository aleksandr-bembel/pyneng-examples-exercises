# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip = input('Введите адрес в формате x.y.z.c: ')

ip_list = [int(i) for i in ip.split('.')]

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
