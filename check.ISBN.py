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
import os


def main():
    HEADER___ = '\033[95m'
    OKBLUE___ = '\033[94m'
    OKGREEN__ = '\033[92m'
    WARNING__ = '\033[93m'
    FAIL_____ = '\033[91m'
    ENDC_____ = '\033[0m'
    BOLD_____ = '\033[1m'
    UNDERLINE = '\033[4m'
    for file in os.listdir():
        str13 = file[0:13]
        str10 = file[0:10]
        if isbnlib.is_isbn13(str13):
            print("{}{}{} {}".format(
                OKGREEN__, "ISBN      OK:", ENDC_____, file))
        elif isbnlib.is_isbn10(str10):
            str13 = isbnlib.to_isbn13(str10)
            newfilename = str13 + file[10:]
            os.rename(file, newfilename)
            print("{}{}{} {}".format(
                OKGREEN__, "ISBN      OK:", ENDC_____, newfilename))
        else:
            print("{}{}{} {}".format(
                FAIL_____, "ISBN Invalid:", ENDC_____, file))


if __name__ == "__main__":
    main()
