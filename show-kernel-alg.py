#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2023 yaofei zheng
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


def main():
    delimiter = '\t'
    header = []

    file = open("/proc/crypto", "r")
    for line in file:
        clean_line = line.strip('\n').strip('\r').strip()
        if 0 == len(clean_line):
            continue

        key = clean_line.split(':')[0].strip()
        value = clean_line.split(':')[1].strip()

        if key not in header:
            header.append(key)

    file.close()
    # print(header)
    for x in header:
        print("{}".format(x), end=delimiter)
    print("")

    row = []
    for x in header:
        row.append("")
    # print(len(row))
    file = open("/proc/crypto", "r")
    for line in file:
        clean_line = line.strip('\n').strip('\r').strip()
        if 0 == len(clean_line):
            for i in range(len(row)):
                print("{}".format(row[i]), end=delimiter)
                row[i] = ""
            print("")
            continue

        key = clean_line.split(':')[0].strip()
        value = clean_line.split(':')[1].strip()

        index = header.index(key)
        # print("index:{}".format(index))
        row[index] = value
    file.close()


if __name__ == "__main__":
    main()
