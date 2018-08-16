# this script is for converting DuChinese vocabulary from csv file to text file
# with one word (simplified) per line

import regex as re
import sys

input_filename = sys.argv[1]
output_filename = sys.argv[2]

in_f = open(input_filename)
with in_f:
    lines = in_f.readlines()
    in_f.close()

pattern = re.compile(r'\p{isHan}', re.UNICODE)
out = ''
for line in lines:
    if pattern.match(line[0]) is not None:
        out+=line.split(',')[0]
        out+='\n'

out_f = open(output_filename, 'wt')
with out_f:
    out_f.write(out)
    out_f.close()
