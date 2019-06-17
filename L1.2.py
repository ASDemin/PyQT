'''
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса. По результатам проверки должно
выводиться соответствующее сообщение.
'''

from ipaddress import ip_address
from subprocess import call,Popen, PIPE


def host_range_pick(host, r):
    for i in range(r):
        n_host = host +i
        proc = Popen (['ping',n_host], stdout=PIPE)
        success = proc.wait()
        if success ==0:
            print(n_host, 'reachable')
        else:
            print(n_host, 'unreachable')
        host=n_host


host_range_pick(ip, scope)