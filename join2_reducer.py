#!/usr/bin/env python
import sys

last_key = ""
key = ""

total = int(0)
abc = False

num_lines = 0

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)

    num_lines += 1

    if key != last_key:

        if num_lines > 1 and abc:
            print('%s %d' % (last_key, total))

        abc = False
        total = int(0)

        last_key = key

    if value == 'ABC':
        abc = True

    else:
        total += int(value)

print('%s %d' % (key, total))
