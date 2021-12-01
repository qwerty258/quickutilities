#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2021  yaofei zheng
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
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
