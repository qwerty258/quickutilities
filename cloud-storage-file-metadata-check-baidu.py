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

import sys
import os
import json
import hashlib


def main():
    if 2 != len(sys.argv):
        print("Please pass the json file after {}".format(sys.argv[0]))
        return
    f = open(sys.argv[1], "r")
    metadata = json.load(f)
    # print(metadata["list"])
    for file_metadata in metadata["list"]:
        if 1 != file_metadata["isdir"]:
            filename = os.path.basename(file_metadata["path"])
            if os.path.exists(filename):
                # print(filename)
                md5sum = hashlib.md5(open(filename, "rb").read()).hexdigest()
                # print("file md5: {}".format(md5sum))
                # print("metadata md5: {}".format(file_metadata["md5"]))
                if md5sum == file_metadata["md5"].lower():
                    print("File MD5 OK: {}".format(filename))
                else:
                    print("File MD5 mismatch: {}".format(filename))
            else:
                print("File do not exists: {}".format(filename))


if __name__ == "__main__":
    main()
