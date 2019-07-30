# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']


try:
    with open(argv[1],'r') as f:
        for line in f:
            if not line.startswith('!'):
                line_ok=True
                for word in ignore:
                    if word in line:
                        line_ok=False
                if line_ok:
                    print(line.rstrip())
except IOError:
    print("File not found")