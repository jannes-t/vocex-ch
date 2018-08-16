import sys
import os

filename1 = sys.argv[1]
filename2 = sys.argv[2]

if (not os.path.isfile(filename1)):
    print('invalid filename')
    exit()

if (not os.path.isfile(filename2)):
    print('invalid filename')
    exit()

with open(filename1, 'rt') as f:
    lines1 = f.readlines()

with open(filename2, 'rt') as f:
    lines2 = f.readlines()

set1 = set(lines1)
set2 = set(lines2)

diff12 = set1.difference(set2)
diff21 = set2.difference(set1)

print('words in 1 but not 2:')
for item in diff12:
    print(item)

print('words in 2 but not 1:')
for item in diff21:
    print(item)
