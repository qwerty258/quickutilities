#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2022 yaofei zheng
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

import os
import sys


def main():
    # print("Argument of file: {}".format(sys.argv[1]))
    current_working_dir = os.path.abspath(os.getcwd())
    # print("Current Working Dir: {}".format(current_working_dir))
    filelist = open(sys.argv[1], 'r')
    lines = filelist.readlines()
    count = 0
    for line in lines:
        src_path = line.strip('\r').strip('\n')
        # print(os.path.basename(src_path) )
        dest = os.path.join(current_working_dir, os.path.basename(src_path))
        # print(dest)
        count += 1
        # print("Line {}: {}".format(count, src_path))
        try:
            os.link(src_path, dest)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
