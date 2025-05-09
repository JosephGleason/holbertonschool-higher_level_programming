#!/usr/bin/python3

for alphabet in range(97, 123):
    print("{:c}".format(alphabet),
          end='\n' if alphabet == 122 else '')
