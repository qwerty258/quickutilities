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
import parse
# '·' is the separator


def main():
    for file in os.listdir():
        if os.path.isfile(file):
            print("processing {}".format(file))
            ret = parse.parse('{}·{}.{}', file)
            if None != ret:
                if ret[0].isdigit() and ret[1].isdigit():
                    if len(ret[1]) != 4:
                        newfile = "{}·{:04d}.{}".format(
                            ret[0], int(ret[1]), ret[2])
                        print("renaming {} to {}".format(file, newfile))
                        os.rename(file, newfile)
                        continue

            ret = parse.parse('{}.{}.{}', file)
            if None != ret:
                if ret[0].isdigit() and ret[1].isdigit():
                    newfile = "{}·{:04d}.{}".format(
                        ret[0], int(ret[1]), ret[2])
                    print("renaming {} to {}".format(file, newfile))
                    os.rename(file, newfile)
                    continue

            ret = parse.parse('{}-{}.{}', file)
            if None != ret:
                if ret[0].isdigit() and ret[1].isdigit():
                    newfile = "{}·{:04d}.{}".format(
                        ret[0], int(ret[1]), ret[2])
                    print("renaming {} to {}".format(file, newfile))
                    os.rename(file, newfile)
                    continue

            print("")


if __name__ == "__main__":
    main()
