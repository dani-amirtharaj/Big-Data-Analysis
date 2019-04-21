#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_pair = None
current_count = 0
pair = None
topList = []
dupList = []

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    pair = word.split("~")

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_pair == pair:
        current_count += count
    elif current_pair:
        if (len(topList) == 0):
            topList.append([current_count, current_pair])
        elif [current_pair[1], current_pair[0]] not in dupList:
            dupList.append(current_pair)
            topList.append([current_count, current_pair])
        current_count = count
        current_pair = pair
    else:
        current_count = count
        current_pair = pair

# do not forget to output the last pair if needed!
if current_pair == pair:
    if (len(topList) == 0):
        topList.append([current_count, current_pair])
    elif [current_pair[1], current_pair[0]] not in dupList:
        topList.append([current_count, current_pair])
    def sorter(pair):
        return pair[0]
    topList.sort(key = sorter, reverse = True)
    for count, pair in topList:
        print '%s\t%s' % (pair[0]+"~"+pair[1], count/2)
