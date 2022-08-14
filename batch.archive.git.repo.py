#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2022 yaofei zheng
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import send2trash
  

def main():
    current_working_dir = os.getcwd()
    dir_list = list(filter(os.path.isdir, os.listdir(current_working_dir)))
    for dir in dir_list:
        absolute_dir_path = "{}/{}".format(current_working_dir, dir)
        if os.path.isdir("{}/.git".format(absolute_dir_path)):
            print(absolute_dir_path)
            if os.path.isdir("{}/.vscode".format(absolute_dir_path)):
                cmd = 'tar -cvJf "{}.tar.xz" "{}/.git" "{}/.vscode"'.format(dir, dir, dir)
            else:
                cmd = 'tar -cvJf "{}.tar.xz" "{}/.git"'.format(dir, dir)
            print(cmd)
            os.system(cmd)
            send2trash.send2trash(absolute_dir_path)


if __name__ == "__main__":
    main()
