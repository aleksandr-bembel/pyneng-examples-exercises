# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']


try:
    with open(argv[1],'r') as src, open('config_sw1_cleared.txt','w') as dest:
        for line in src:
            line_ok=True
            for word in ignore:
                if word in line:
                    line_ok=False
            if line_ok:
                dest.write(line)
except IOError:
    print("File not found")