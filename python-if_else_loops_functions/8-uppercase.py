#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord('a') <= ord(ch) <= ord('z'):
            print(chr(ord(ch) - 32), end="")
        else:
            print(ch, end="")
    print()
