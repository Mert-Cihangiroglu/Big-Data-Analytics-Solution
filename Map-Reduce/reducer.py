#!/usr/bin/env python

import sys

total_bankrupt = 0
total_non_bankrupt = 0

for line in sys.stdin:
    data = line.strip().split(",")

    if len(data) != 2:
        continue

    this_key, this_data = data


    if this_key != 'Bankrupt?':
        if float(this_data) > 0.5:
            if this_key == 1:
                total_bankrupt += 1
            else:
                total_non_bankrupt += 1

print("total_bankrupt","total_non_bankrupt")
print(total_bankrupt,total_non_bankrupt)
