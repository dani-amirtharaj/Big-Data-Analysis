#!/usr/bin/env python
"""mapper.py"""

import sys

topList = ["music", "video", "like", "love", "song", "listen", "new", "good", "playing", "one"]

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        if (word in topList):
            for neighbour in words:
                # write the results to STDOUT (standard output);
                # what we output here will be the input for the
                # Reduce step, i.e. the input for reducer.py
                #
                # tab-delimited; the trivial word count is 1
                if (neighbour != word):
                    print '%s\t%s' % (word+"~"+neighbour, 1)
