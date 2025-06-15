/**
 * MIT License
 * 
 * Copyright (c) 2025 yaofei zheng
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <fcntl.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdint.h>
#include <stdbool.h>
#define SECTOR_SIZE 512
static uint8_t zero_data[SECTOR_SIZE] = {0};
static uint8_t ff_data[SECTOR_SIZE] = {0xFF};
static uint8_t sector[SECTOR_SIZE];
int main(int argc, char *argv[])
{
    int fd = open("/dev/sdc", O_RDWR);
    if (0 > fd)
    {
        printf("device open error");
        return -1;
    }

    off_t offset = 0;
    lseek(fd, offset, SEEK_SET);
    ssize_t read_size = 0;
    do
    {
        printf("read offset: %ld\n", offset);
        read_size = read(fd, sector, SECTOR_SIZE);
        if (SECTOR_SIZE == read_size)
        {
            bool need_overwrite = false;
            for (size_t i = 0; i < SECTOR_SIZE; i++)
            {
                printf("%02X", sector[i]);
                if (0 == ((i + 1) % 16))
                    printf("\n");
                if (0 != sector[i])
                    need_overwrite = true;
            }
            if (need_overwrite)
            {
                lseek(fd, offset, SEEK_SET);
                write(fd, ff_data, SECTOR_SIZE);
                lseek(fd, offset, SEEK_SET);
                write(fd, zero_data, SECTOR_SIZE);
                sync();
                printf("overwrite this sector completed\n");
                // getchar();
            }
            offset += read_size;
        }
        else
        {
            printf("read offset: %ld error: %s\n", offset, strerror(errno));
        }
    } while (SECTOR_SIZE == read_size);

    close(fd);
    return 0;
}
