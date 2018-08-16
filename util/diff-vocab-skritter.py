import sys

vocab_list_filename = sys.argv[1]
vocab_skritter_filename = sys.argv[2]

vocab_list_file = open(vocab_list_filename, 'rt')
vocab_skritter_file = open(vocab_skritter_filename, 'rt')

vocab_list = vocab_list_file.readlines()
vocab_set = set()
for line in vocab_list:
    vocab_set.add(line.strip('\n'))

vocab_skritter = vocab_skritter_file.readlines()
skritter_set = set()
for line in vocab_skritter:
    skritter_set.add(line.split('\t')[0])

for x in vocab_set.difference(skritter_set):
    print(x)

