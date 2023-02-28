#!/usr/bin/env python
# find the count of bankrupts and non bankrupts where Operating Profit Rate > 0.5
import sys

total_bankrupt = 0
total_non_bankrupt = 0

for line in sys.stdin:
    data = line.strip().split(",")
    # If the line lenght isn't equal to 2, there's is something wrong but just continue.
    if len(data) != 2:
        print(f"There's an error at {line}, and data is {data}")
        continue

    this_key, this_data = data

    # Mapper passed the label names, so if I wasn't checking this, it was throwing an error.
    # TO DO: In the mapper make sure that the label names are not passed.
    if this_key != 'Bankrupt?':
        if float(this_data) > 0.5:
            if this_key == 1:
                total_bankrupt += 1
            else:
                total_non_bankrupt += 1

print("total_bankrupt","total_non_bankrupt")
print(total_bankrupt,total_non_bankrupt)
