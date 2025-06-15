#!/usr/bin/env python3

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
