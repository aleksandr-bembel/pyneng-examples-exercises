# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

ip = argv[1]

ip1, ip2, ip3, ip4 = ip.split("/")[0].split(".")
ip1=int(ip1)
ip2=int(ip2)
ip3=int(ip3)
ip4=int(ip4)
mask = int(ip.split("/")[1])
bitip="{0:08b}{1:08b}{2:08b}{3:08b}".format(ip1,ip2,ip3,ip4)

bitnet=bitip[0:mask]+"0"*(32-mask)
bitmask = "1"*mask + "0"*(32-mask)

mask1 = int(bitmask[0:8], 2)
mask2 = int(bitmask[8:16], 2)
mask3 = int(bitmask[16:24], 2)
mask4 = int(bitmask[24:32], 2)

net1 = int(bitnet[0:8],2)
net2 = int(bitnet[8:16],2)
net3 = int(bitnet[16:24],2)
net4 = int(bitnet[24:32],2)

print("Network:\n")
print("{0:<10} {1:<10} {2:<10} {3:<10}\n{0:08b}   {1:08b}   {2:08b}   {3:08b}".format(
    net1, net2, net3, net4))
print("\nMask:\n/{}".format(mask))
print("{0:<10} {1:<10} {2:<10} {3:<10}\n{0:<08b}   {1:<08b}   {2:<08b}   {3:<08b}".format(
    mask1, mask2, mask3, mask4))
