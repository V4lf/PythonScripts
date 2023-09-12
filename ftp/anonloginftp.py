#!/usr/bon/python

import ftplib
import os


def get_all_files_from_directory(ftp, local_directory):
    # TODO:
    # try this see if mlsd is enabled.
    # else use nlst command
    for filename, facts in ftp.mlsd():
        print(filename)

        local_filename = os.path.join(local_directory, filename)
        file = open(local_filename, 'wb')
        ftp.retrbinary('RETR ' + filename, file.write)

        file.close()


def anon_login(host):
    try:
        ftp = ftplib.FTP(host)
        ftp.login("anonymous", "anonymous")
        print("Login successful")
        local_directory = input("Set local directory name to copy to: ")
        get_all_files_from_directory(ftp, local_directory)
        return True
    except:
        print("login failed")
        return False


def main():
    host = input("Enter ip: ")
    anon_login(host)


if __name__ == '__main__':
    main()
