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

import sys
import os


def main():
    workspace = "/tmp/tar-po-workspace"
    cmd_mkdir = 'mkdir -p "{}"'.format(workspace)
    print(cmd_mkdir)
    os.system(cmd_mkdir)

    cmd_clean_up = 'rm -rfv "{}/"*'.format(workspace)
    os.system(cmd_clean_up)

    cmd_extract = 'tar -xf "{}" -C "{}"'.format(sys.argv[1], workspace)
    print(cmd_extract)
    os.system(cmd_extract)
    new_file = "new-{}".format(os.path.basename(sys.argv[1]))
    wd_current = os.getcwd()
    os.chdir(workspace)
    cmd_compress = 'tar --owner=root --group=root -cJf "{}" *'.format(new_file)
    print(cmd_compress)
    os.system(cmd_compress)
    os.chdir(wd_current)
    new_file_path = os.path.join(workspace, new_file)
    cmd_copy_file = 'cp "{}" "{}"'.format(new_file_path, wd_current)
    print(cmd_copy_file)
    os.system(cmd_copy_file)


if __name__ == "__main__":
    main()
