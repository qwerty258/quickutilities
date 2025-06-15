#!/usr/bin/env python3

# MIT License
# 
# Copyright (c) 2023 yaofei zheng
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

import os
import requests
import bs4


def main():
    dmtf_std_url = "https://www.dmtf.org/standards/published_documents"
    page = requests.get(dmtf_std_url)
    # print(type(page.text))
    # print(page.text)

    soup = bs4.BeautifulSoup(page.text, "html.parser")
    # print(type(soup))

    # DMTF Specifications
    table = soup.find("table", id="views-aggregator-datatable--2")
    # print(type(table))
    # print(table)

    for data in table.find_all("tbody"):
        for row in data.find_all("tr"):
            # print(row)
            # print(type(row))
            file_url = row.find_all("td")[0].find_all("a")[0].attrs["href"]
            print(file_url)
            # print(type(file_url))
            filename = os.path.basename(file_url)
            if os.path.exists(filename):
                continue
            else:
                response = requests.get(file_url)
                open(filename, "wb").write(response.content)


if __name__ == "__main__":
    main()
