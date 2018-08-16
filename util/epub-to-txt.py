from functions import epub_to_txt
import sys

filename = sys.argv[1]
text = epub_to_txt(filename)

outfilename = sys.argv[2]
f = open(outfilename, 'wt')
f.write(text)
