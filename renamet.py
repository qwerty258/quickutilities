#!/usr/bin/env python

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
