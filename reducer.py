#!/usr/bin/python

import sys
from collections import defaultdict

prev_author = None
hour_dict = defaultdict(int)

for line in sys.stdin:
    author, hour = line.strip().split('\t')

    if prev_author and author != prev_author: # process to a new user
	max_hour, max_freq = max(hour_dict.iteritems(), key=lambda t: t[1])
	top_hours = list(h for h in hour_dict if hour_dict[h] == max_freq)
	for h in top_hours:
	    print '{author_id}\t{hour}'.format(author_id=prev_author, hour=h)
	hour_dict.clear()

    prev_author = author
    hour_dict[hour.strip('"')] += 1

# print last record
max_hour, max_freq = max(hour_dict.iteritems(), key=lambda t: t[1])
top_hours = list(h for h in hour_dict if hour_dict[h] == max_freq)
for h in top_hours:
    print '{author_id}\t{hour}'.format(author_id=prev_author, hour=h)
