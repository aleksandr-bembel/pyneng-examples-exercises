# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip = input('Введите адрес в формате x.y.z.c: ')

ip_list = [int(i) for i in ip.split('.')]

correct = True
for octet in ip_list:
    if octet >= 0 and octet <= 255:
        pass
    else:
        correct = False
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
else:
    print("Неправильный IP-адрес")
