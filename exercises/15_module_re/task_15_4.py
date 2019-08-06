# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
'''
import re
from pprint import pprint

def get_ints_without_description(filename):
    result=[]
    regex=r"(?:^interface (\S+)|description (\S+))"
    intf=""
    with open(filename) as f:
        for line in f:
            match = re.search(regex,line)
            if match and match.lastindex == 1:
                intf=match.group(match.lastindex)
            elif intf and match and match.lastindex == 2:
                intf=""
            elif intf != "":
                result.append(intf)
                intf=""

                

        
    return result

if __name__ == "__main__":
    pprint(get_ints_without_description("config_r1.txt"))
