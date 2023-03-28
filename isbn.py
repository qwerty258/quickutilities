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
