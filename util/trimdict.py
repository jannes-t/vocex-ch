import sys
import os

filename = sys.argv[1]
if (not os.path.isfile(filename)):
    print('invalid filename')
    exit()

with open(filename, 'rt') as f:
    lines = f.readlines()

lines2 = list()

for line in lines:
    if '，' not in line:
        lines2.append(line)

output = open('out.txt', 'w')

for line in lines2:
    output.write(line)
