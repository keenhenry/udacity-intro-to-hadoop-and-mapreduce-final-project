#!/usr/bin/python

import sys
import heapq

prev_tag = None
top10_tags = []
num_questions = 0

for line in sys.stdin:
    tag, count = line.strip().split('\t')

    if prev_tag and tag != prev_tag: # process to a new tag
	if len(top10_tags) < 10:
	    heapq.heappush(top10_tags, (num_questions, prev_tag))
	else: # len(top10_tags) >= 10
	    heapq.heappushpop(top10_tags, (num_questions, prev_tag))
	num_questions = 0

    prev_tag = tag
    num_questions += int(count.strip('"'))

# calculation for the last tag processed
if len(top10_tags) < 10:
    heapq.heappush(top10_tags, (num_questions, prev_tag))
else: # len(top10_tags) >= 10
    heapq.heappushpop(top10_tags, (num_questions, prev_tag))

# print top 10 tags
for t in sorted(top10_tags, key=lambda t: t[0], reverse=True):
    print '{tag}\t{num_questions}'.format(tag=t[1], num_questions=t[0])
