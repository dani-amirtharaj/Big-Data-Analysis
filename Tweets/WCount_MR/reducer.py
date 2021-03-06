#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
topList = []

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    elif current_word:
        if (len(topList) == 0):
            topList.append([current_count, current_word])
        else:
            # ind = 0
            # for boolVal in [current_count > wordCount for wordCount, unused_word in topList]:
            #     if (boolVal):
                    # topList.insert(ind, [current_count, current_word])
                    # if (len(topList) > 50):
                    #    topList.pop(50)
                    # break
                # ind+=1
            topList.append([current_count, current_word])
        current_count = count
        current_word = word
    else:
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    if (len(topList) == 0):
        topList.append([current_count, current_word])
    else:
        # ind = 0
        # for boolVal in [current_count > wordCount for wordCount, word in topList]:
        #     if (boolVal):
                # topList.insert(ind, [current_count, current_word])
                # if (len(topList) > 50):
                #     topList.pop(50)
                # break
            # ind+=1
        topList.append([current_count, current_word])
    def sorter(pair):
        return pair[0]
    topList.sort(key = sorter, reverse = True)
    for count, word in topList:
        print '%s\t%s' % (word, count)
