'''
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет
проверяться доступность сетевых узлов. Аргументом функции является список,
в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом
соответствующего сообщения («Узел доступен», «Узел недоступен»).
При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
'''

from subprocess import Popen, PIPE

def host_ping (list):

    for el in list:
        ping = Popen(['ping',el],stdout=PIPE)
        stdout, stderr = ping.communicate()
    if ping.returncode ==0:
        print ('ok')
    else:
        print('error')


list = ['ya.ru','ghgh.ruu']
host_ping(list)