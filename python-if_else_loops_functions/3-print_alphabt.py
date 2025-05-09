#!/usr/bin/python3
exclude = (101, 113)
for code in range(97, 123):
    if code in exclude:
        continue
    print("{:c}".format(code), end='')
