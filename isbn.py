#!/usr/bin/env python

import isbnlib
import sys

def main():
    isbn13 = " "
    bprint = False
    if isbnlib.is_isbn10(sys.argv[1]):
        isbn13 = isbnlib.to_isbn13(sys.argv[1])
        bprint = True
    elif isbnlib.is_isbn13(sys.argv[1]):
        isbn13 = sys.argv[1]
        bprint = True

    if bprint:
        print("{}".format(isbn13))
        print("{}".format(isbnlib.info(isbn13)))
    else:
        print("invalid ISBN")
        

if __name__ == "__main__":
    main()

