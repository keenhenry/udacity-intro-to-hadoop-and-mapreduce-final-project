#!/usr/bin/python

"""`mapper`

The fields from sample data is as follows:

id	title	tagnames	author_id	body	node_type	parent_id	abs_parent_id added_at ...

What we are interested in is author_id and added_at.
"""

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    _ = next(reader)
    for line in reader:
	thread_id, author_id, node_type, parent_id = line[0], line[3], line[5], line[6]
	if node_type == 'question':
	    writer.writerow([thread_id, author_id])
	else:
	    writer.writerow([parent_id, author_id])

mapper()
