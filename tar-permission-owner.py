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
import subprocess
import json


def run_cmd(cmd: list, current_working_dir: str = None, use_shell=False) -> dict:
    cmd_result = subprocess.run(
        cmd, capture_output=True, cwd=current_working_dir, shell=use_shell
    )
    json_result = {
        "cmd": cmd,
        "returncode": cmd_result.returncode,
        "stderr": cmd_result.stderr.decode(),
        "stdout": cmd_result.stdout.decode(),
    }
    if 0 != json_result["returncode"]:
        print(json.dumps(json_result, ensure_ascii=False, indent=4, sort_keys=True))
    return json_result


def main():
    workspace = "/tmp/tar-po-workspace"
    cmd_mkdir = ["mkdir", "-p", workspace]
    print("Begin processing: {}".format(sys.argv[1]))
    run_cmd(cmd_mkdir)

    cmd_clean_up = 'rm -rfv "{}/"*'.format(workspace)
    run_cmd(cmd=cmd_clean_up, use_shell=True)

    cmd_extract = ["tar", "-xf", sys.argv[1], "-C", workspace]
    run_cmd(cmd_extract)

    new_file = "new-{}".format(os.path.basename(sys.argv[1]))
    wd_current = os.getcwd()
    cmd_compress = 'tar --owner=root --group=root -cJf "{}" *'.format(new_file)
    run_cmd(cmd=cmd_compress, current_working_dir=workspace, use_shell=True)

    new_file_path = os.path.join(workspace, new_file)
    atime = os.path.getatime(sys.argv[1])
    mtime = os.path.getmtime(sys.argv[1])
    cmd_compare = ["pkgdiff", sys.argv[1], new_file_path]
    compare_result = run_cmd(cmd_compare)
    if "UNCHANGED" in compare_result["stdout"]:
        cmd_copy_file = ["cp", new_file_path, sys.argv[1]]
        run_cmd(cmd_copy_file)
        os.utime(sys.argv[1], (atime, mtime))
    else:
        print("Error happend in while processing {}".format(sys.argv[1]))
        os.utime(new_file_path, (atime, mtime))
        cmd_copy_file = ["cp", new_file_path, wd_current]
        run_cmd(cmd_copy_file)


if __name__ == "__main__":
    main()
