#!/usr/bin/env python3

# MIT License
# 
# Copyright (c) 2023 Yaofei Zheng
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
import libtorrent as lt


def main():
    nametorrent = lt.torrent_info(lt.bdecode(
        open(sys.argv[1], 'rb').read())).name()+".torrent"
    if os.access(nametorrent, os.W_OK):
        print("ERROR:\n{}\nfile name exists:\n{}".format(sys.argv[1], nametorrent))
    else:
        tip = "renaming '{}' to '{}'".format(sys.argv[1], nametorrent)
        print(tip)
        os.rename(sys.argv[1], nametorrent)


if __name__ == "__main__":
    main()
