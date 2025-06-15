#!/usr/bin/env python3

# MIT License
# 
# Copyright (c) 2025 Yaofei Zheng
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
import exifread
import datetime

def main():
    files = os.listdir("./")
    for file in files:
        if "JPG" in file:
            f = open(file, "rb")
            tags = exifread.process_file(f)
            f.close()
            # print(tags)
            # print(type(tags["Image DateTime"]))
            rawtimestap = tags["EXIF DateTimeOriginal"].values.split(' ')
            # print(rawtimestap)
            isotimestring = "{}T{}+08:00".format(rawtimestap[0].replace(':', '-'), rawtimestap[1])
            print(isotimestring)
            timestamp = datetime.datetime.fromisoformat(isotimestring)
            creation_time = timestamp.timestamp()
            os.utime(file, (creation_time, creation_time))
            os.system("touch -d {} {}".format(isotimestring, file))


if __name__ == "__main__":
    main()
