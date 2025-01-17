# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

with open("ospf.txt", 'r') as f:
    for line in f:
        _, prefix, ad, _, nexthop, last, intf = line.split()
        ad = ad.strip('[]')
        nexthop = nexthop.strip(',')
        last = last.strip(',')

        print("Protocol:              {}".format("OSPF"))
        print("Prefix:                {}".format(prefix))
        print("AD/Metric:             {}".format(ad))
        print("Next-Hop:              {}".format(nexthop))
        print("Last update:           {}".format(last))
        print("Outbound Interface:    {}".format(intf))
        print()
