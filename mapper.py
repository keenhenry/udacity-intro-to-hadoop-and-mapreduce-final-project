#!/usr/bin/python

"""`mapper`

The fields from sample data is as follows:

id	title	tagnames	author_id	body	node_type	parent_id	abs_parent_id added_at ...

What we are interested in is author_id and added_at.
"""

import sys
import csv
import datetime

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    _ = next(reader)
    for line in reader:
	author_id, added_at = line[3], line[8]
	time = datetime.datetime.strptime(added_at[:added_at.rfind('+')], '%Y-%m-%d %H:%M:%S.%f')
        writer.writerow([author_id, time.hour])

mapper()
