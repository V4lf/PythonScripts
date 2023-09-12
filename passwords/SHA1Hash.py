#!/usr/bin/python

import hashlib
from urllib.request import urlopen


def main():
    sha1hash = input("Enter SHA1 hash: ")
    passlist = str(urlopen(
        "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt").read(),
                   "utf-8")

    for i in passlist.split("\n"):
        hashguess = hashlib.sha1(bytes(i, "utf-8")).hexdigest()
        if hashguess == sha1hash:
            print(" The password is: " + str(i))
            quit()

    print("Password not in list!")

if (__name__ == '__main__'):
    main()
