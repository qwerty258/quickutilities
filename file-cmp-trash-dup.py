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


import sys
import os
import hashlib
import send2trash


def main():
    print(hashlib.algorithms_available)

    origin_file_list_file = open(sys.argv[1])
    new_file_list_file = open(sys.argv[2])
    
    while True:
        origin_file_path = origin_file_list_file.readline().strip('\r').strip('\n')
        if not origin_file_path:
            break
        print(origin_file_path)
        new_file_path = new_file_list_file.readline().strip('\r').strip('\n')
        print(new_file_path)

        if os.path.exists(origin_file_path) and os.path.exists(new_file_path):
            read_size = 1024*1024
            origin_file_sha1_ctx = hashlib.sha1()
            new_file_sha1_ctx = hashlib.sha1()
            with open(origin_file_path, "rb") as file:
                while True:
                    data = file.read(read_size)
                    if not data:
                        break
                    origin_file_sha1_ctx.update(data)
            with open(new_file_path, "rb") as file:
                while True:
                    data = file.read(read_size)
                    if not data:
                        break
                    new_file_sha1_ctx.update(data)
            origin_file_sha1 = origin_file_sha1_ctx.hexdigest()
            new_file_sha1 = new_file_sha1_ctx.hexdigest()
            if origin_file_sha1 == new_file_sha1:
                send2trash.send2trash(new_file_path)
            else:
                print("The files are different: {}, {}".format(
                    origin_file_path, new_file_path))
        else:
            print("File not found: {}, {}".format(
                origin_file_path, new_file_path))


if __name__ == "__main__":
    main()
