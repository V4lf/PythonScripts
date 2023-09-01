#!/usr/bin/python

from socket import *
import optparse
from threading import *
import subprocess

def vulnscan(banner):
        process = subprocess.run(['searchsploit', banner],
                               stdout=subprocess.PIPE,
                               universal_newlines=True,
                               stderr=subprocess.PIPE)
        print(process.stdout)
        print(process.stderr)



def portScan(tgtHost, tgtPorts, checkVersion):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("Unknown host %s" % tgtHost)
    try:
        tgtName = gethostbyaddr(tgtIP)
        print("[+] Scan results for: " + tgtName[0])
    except:
        print("[+] Scan results for: " + tgtIP)
    setdefaulttimeout(30)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort), checkVersion))
        t.start()


def connScan(tgtHost, tgtPort, checkVersion):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print("[+] %d/tcp open" % tgtPort)
        if checkVersion:
            banner = sock.recv(1024)
            print("\t" + str(banner))
            vulnscan(banner)

    finally:
        sock.close()


def main():
    parser = optparse.OptionParser('Usage: ' + '-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports seperated by comma')
    parser.add_option('-V', dest='checkVersion', action="store_true", help='checkVersion')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    checkVersion = options.checkVersion
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts, checkVersion)


if __name__ == '__main__':
    main()
