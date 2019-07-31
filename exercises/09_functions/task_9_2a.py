# -*- coding: utf-8 -*-
'''
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    config = {}
    for intf, vlans in intf_vlan_mapping.items():
        config[intf] = []
        for line in trunk_template:
            if "allowed vlan" in line:
                config[intf].append(
                    line + " " + ",".join([str(vlan) for vlan in vlans]))
            else:
                config[intf].append(line)
    return config


if __name__ == "__main__":
    result = generate_trunk_config(trunk_config, trunk_mode_template)
    print(result)
