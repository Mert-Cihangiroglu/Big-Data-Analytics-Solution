#!/usr/bin/python

# We want elements 0 (Bankrupt?) and 6 (Operating Profit Rate,)
# We want to write them out to standard output, separated by a tab

import sys
import csv

for line in sys.stdin:
  data = line.strip().split(",")
  if len(data) == len(data):
    data = [col for col in data]
    print("{0},{1}".format(data[0], data[6]))
    #print(data[0],data[6])
    