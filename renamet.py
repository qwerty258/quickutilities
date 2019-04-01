#!/usr/bin/env python

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

import os
import sys
import warnings
warnings.filterwarnings("ignore")
import libtorrent as lt

def main():
    nametorrent=lt.torrent_info(lt.bdecode(open(sys.argv[1], 'rb').read())).name()+".torrent"
    if os.access(nametorrent, os.W_OK):
        print("file name exists: {}".format(nametorrent))
    else:
        tip="renaming '{}' to '{}'".format(sys.argv[1], nametorrent)
        print(tip)
        os.rename(sys.argv[1], nametorrent)

if __name__ == "__main__":
    main()
