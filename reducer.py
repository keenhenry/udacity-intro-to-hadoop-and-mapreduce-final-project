#!/usr/bin/python

import sys

prev_node = None
students = []

for line in sys.stdin:
    node, student_id = line.strip().split('\t')

    if prev_node and node != prev_node: # process to a new node
	print '{node_id}: {student_list}'.format(node_id=prev_node.strip('"'), student_list=students)
	del students[:]

    prev_node = node
    students.append(int(student_id.strip('"')))

# print for the last node processed
print '{node_id}: {student_list}'.format(node_id=prev_node.strip('"'), student_list=students)
