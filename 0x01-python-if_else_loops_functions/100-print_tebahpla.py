#!/usr/bin/python3

for i in range(25, -1, -1):
    print(chr(ord('Z') - i) if i % 2 else chr(ord('z') - i), end="")
