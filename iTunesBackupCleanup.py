#!/usr/bin/env python3
import sqlite3
import send2trash
import sys

def main():
    dbrootdir = r'C:\Users\Admin\AppData\Roaming\Apple Computer\MobileSync\Backup\f07c12dde64d708259d23f19ae8406b019c83a00'

    uni = list()

    con = sqlite3.connect(dbrootdir+r'\Manifest.db')
    print(con)

    c = con.cursor()

    for row in c.execute("SELECT `fileID`, `relativePath` FROM `Files`"):
        if row[1].find("SMS") == -1:
            print(row)
            uni.append(row[0])
            try:
                send2trash.send2trash(dbrootdir+'\\'+row[0][:2]+'\\'+row[0])
            except FileNotFoundError :
                print(dbrootdir+'\\'+row[0][:2]+'\\'+row[0]+' Not Found.')

    for id in uni:
        c.execute("DELETE FROM `Files` WHERE `fileID` = '{0}'".format(id))

    c.execute("COMMIT")

    con.close()

if __name__ == "__main__":
    main()
