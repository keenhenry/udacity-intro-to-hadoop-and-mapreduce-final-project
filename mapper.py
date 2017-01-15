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
	tags, node_type = line[2], line[5]
	if node_type != 'question':
	    continue
	for tag in tags.split():
            writer.writerow([tag, 1])

mapper()
