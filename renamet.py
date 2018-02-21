#!/usr/bin/env python

import os
import sys
import libtorrent

def main():
    nametorrent=libtorrent.torrent_info(libtorrent.bdecode(open(sys.argv[1], 'rb').read())).name()+".torrent"
    tip="renaming {} to {}".format(sys.argv[1], nametorrent)
    os.rename(sys.argv[1], nametorrent)

if __name__ == "__main__":
    main()
