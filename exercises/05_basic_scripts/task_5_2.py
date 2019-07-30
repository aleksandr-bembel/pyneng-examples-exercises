# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip = input("Введите IP-адрес в формате 10.1.1.0/24: ")

ip1, ip2, ip3, ip4 = ip.split("/")[0].split(".")
mask = int(ip.split("/")[1])
bitmask = "1"*mask + "0"*(32-mask)
mask1 = int(bitmask[0:8], 2)
mask2 = int(bitmask[8:16], 2)
mask3 = int(bitmask[16:24], 2)
mask4 = int(bitmask[24:32], 2)

ip1 = int(ip1)
ip2 = int(ip2)
ip3 = int(ip3)
ip4 = int(ip4)

print("Network:\n")
print("{0:<10} {1:<10} {2:<10} {3:<10}\n{0:08b}   {1:08b}   {2:08b}   {3:08b}".format(
    ip1, ip2, ip3, ip4))
print("\nMask:\n")
print("{0:<10} {1:<10} {2:<10} {3:<10}\n{0:<08b}   {1:<08b}   {2:<08b}   {3:<08b}".format(
    mask1, mask2, mask3, mask4))


