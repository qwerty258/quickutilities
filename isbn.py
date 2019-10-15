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


def main():
    isbn13 = " "
    bprint = False
    if isbnlib.is_isbn10(sys.argv[1]):
        isbn13 = isbnlib.to_isbn13(sys.argv[1])
        bprint = True
    elif isbnlib.is_isbn13(sys.argv[1]):
        isbn13 = sys.argv[1]
        bprint = True

    if bprint:
        print(isbn13)
        print(isbnlib.info(isbn13))
    else:
        print("invalid ISBN")


if __name__ == "__main__":
    main()
