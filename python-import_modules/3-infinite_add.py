#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # faylın öz adı çıxılır
    total = 0
    for num in argv:
        total += int(num)
    print(total)
