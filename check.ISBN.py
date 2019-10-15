#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2018-2019  yaofei zheng
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

import isbnlib
import sys
import os


def main():
    for file in os.listdir():
        isbnstr = file[0:13]
        #print(isbnstr)
        #print(file[0])
        #print(file[1])
        if isbnlib.is_isbn13(isbnstr):
            print("{} {}".format("ISBN      OK:", file))
        else:
            print("{} {}".format("ISBN Invalid:", file))


if __name__ == "__main__":
    main()
