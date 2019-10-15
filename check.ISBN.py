#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2018-2019  yaofei zheng
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

import isbnlib
import sys
import os


def main():
    HEADER___ = '\033[95m'
    OKBLUE___ = '\033[94m'
    OKGREEN__ = '\033[92m'
    WARNING__ = '\033[93m'
    FAIL_____ = '\033[91m'
    ENDC_____ = '\033[0m'
    BOLD_____ = '\033[1m'
    UNDERLINE = '\033[4m'
    for file in os.listdir():
            if isbnlib.is_isbn13(file[0:13]):
                print("{}{}{} {}".format(
                    OKGREEN__, "ISBN      OK:", ENDC_____, file))
            else:
                print("{}{}{} {}".format(
                    FAIL_____, "ISBN Invalid:", ENDC_____, file))


if __name__ == "__main__":
    main()
