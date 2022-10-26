#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2022  yaofei zheng
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


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
