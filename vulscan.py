#!/usr/bin/python

import socket
import os
import sys


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("! File does not exist")
            exit(0)
        if not os.access(filename, os.R_OK):
            print("Access denied!")
            exit(0)
    else:
        print("Usage: " + str(sys.argv[0]) + " <vuln filename>")
