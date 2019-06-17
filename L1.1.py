'''
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет
проверяться доступность сетевых узлов. Аргументом функции является список,
в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом
соответствующего сообщения («Узел доступен», «Узел недоступен»).
При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
'''
from ipaddress import ip_address
from subprocess import Popen, PIPE

def ip (list):
    n_list = []
    for el in list:
        ip=ip_address(el)
        n_list.append(ip)
    return n_list

def host_ping (list):

    for el in list:
        ping = Popen(['ping',str(el)],stdout=PIPE)
        data = ping.communicate()
        if ping.returncode ==0:
            print ('{} is Reachable'.format(el))
        else:
            print('{} is Unreachable'.format(el))

host = list(input('Please enter host which you want to check separated by spaces. If you finished - push enter: ').split())
host_ping(ip(host))