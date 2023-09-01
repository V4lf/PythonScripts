#!/usr/bin/python

import pexpect

PROMPT = ['#', '>>>', '> ', '\$ ']


def connect(host, user, password):
    ssh_newKey = "Are you sure you want to continue "
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newKey, '[P|p]assword: '])
    if ret == 0:
        print('Connection Error')
    if ret == 1:
        child.sendline("yes")
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print("Connection Error")
            return
    child.sendline(password)
    child.expect(PROMPT)
    return child


def send_command(connection, command):
    connection.sendline(command)
    connection.expect(PROMPT)
    print(connection.before)


def main():
    host = '127.0.0.1'
    user = ""
    password = ""
    child = connect(host, user, password)
    send_command(child, 'cat /etc/shadow | grep root;ps')


main()
