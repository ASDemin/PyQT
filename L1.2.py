'''
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса. По результатам проверки должно
выводиться соответствующее сообщение.
'''

from ipaddress import ip_address
from subprocess import call,Popen, PIPE


def host_range_pick(host,r):


        for i in range(r):
            n_host = host
            proc = Popen (['ping', str(n_host)], stdout=PIPE)
            data = proc.communicate()
            if proc.returncode == 0:
                 print(n_host, 'reachable')
            else:
                 print(n_host, 'unreachable')
            host = host + 1

host = ip_address(input('Press enter host ip:'))
scope =int(input('Press enter ip range:'))

host_range_pick(host,scope)
