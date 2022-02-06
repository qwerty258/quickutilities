#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2021 yaofei zheng
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

import sys
import cv2
from pyzbar.pyzbar import decode


def main():
    img = cv2.imread(sys.argv[1])
    decode_result = decode(img)
    if not decode_result:
        print("No barcode detected")
    else:
        for barcode in decode_result:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(
                img,
                (x-10, y-10),
                (x+w+10, y+h+10),
                (255, 0, 0),
                2)
            if barcode.data != "":
                print(barcode.data)
                print(barcode.type)

    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
