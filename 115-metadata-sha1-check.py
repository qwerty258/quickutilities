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

import sys
import os
import json
import hashlib


def main():
    if 2 != len(sys.argv):
        print("Please pass the json file after {}".format(sys.argv[0]))
        return
    f = open(sys.argv[1], 'r')
    metadata = json.load(f)
    # print(metadata["data"])
    for item in metadata["data"]:
        # print(item)
        if "sha" in item:
            if os.path.exists(item["n"]):
                sha1 = hashlib.sha1(open(item["n"],"rb").read()).hexdigest()
                # print(sha1)
                if sha1 == item["sha"].lower():
                    print("File SHA1 OK: {}".format(item["n"]))
                else:
                    print("File SHA1 mismatch: {}".format(item["n"]))
            else:
                print("File do not exists: {}".format(item["n"]))


if __name__ == "__main__":
    main()
