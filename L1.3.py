'''
3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном
формате (использовать модуль tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:
Reachable
10.0.0.1
10.0.0.2
Unreachable
10.0.0.3
10.0.0.4
'''

from ipaddress import ip_address
from subprocess import call,Popen, PIPE
from tabulate import tabulate

def host_range_pick(host,r):
    reachable = []
    unreachable = []
    dict1 = {}
    dict2 = {}
    for i in range(r):
        n_host = host
        proc = Popen(['ping', str(n_host)], stdout=PIPE)
        data = proc.communicate()
        if proc.returncode == 0:
            reachable.append(n_host)
        else:
            unreachable.append(n_host)
        host = host + 1
    dict1['Reachable'] = reachable
    dict2['Unreachable'] = unreachable
    dict1.update(dict2)
    print(tabulate(dict1,headers='keys'))



host = ip_address(input('Press enter host ip:'))
scope =int(input('Press enter ip range:'))

host_range_pick(host,scope)

