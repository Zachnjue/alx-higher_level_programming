#!/usr/bin/python3
for i in range(97, 123):
    if 'e' in chr(i):
        continue
    elif 'q' in chr(i):
        continue
    print("{:c}".format(i), end="")
