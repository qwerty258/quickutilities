#!/bin/sh

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

DEFAULT_INSTALL_LOCATION="/usr/local/bin"

cp archive-eml \
    batch.644.file \
    batch.755.folder \
    batch.7z2tarxz \
    batch.7z.test \
    batch.archive.git.repo.py \
    batch.AVI.test \
    batch.dos2unix \
    batch.GBK2UTF-8.convert \
    batch.git.gc \
    batch.hardlink.py \
    batch.jpg.test \
    batch.JPG.test \
    batch.md2docx \
    batch.msxmldocs.test \
    batch.rar.test \
    batch.sha1sum.rename \
    batch.tar.xz.test \
    batch.torrent.rename \
    batch.zip.test \
    check.ISBN.py \
    currentdir.md5sum \
    currentdir.sha1sum \
    currentdir.sha256sum \
    dmtf-std-update.py \
    extract-html-links.py \
    file-cmp-trash-dup.py \
    file-name-replace-string \
    gitallbranch \
    gitfetchandpull \
    iconv.GBK2UTF-8 \
    iconv.UTF-16toUTF-8 \
    isbn.py \
    iTunesBackupCleanup.py \
    md2docx.sh \
    old-cn-std-book-number.py \
    python-show-path.py \
    readbarcode.py \
    renamet.py \
    sha1sum.rename \
    tardir2xz \
    unzipmbcs.py \
    xhtml5format \
    "${DEFAULT_INSTALL_LOCATION}"
