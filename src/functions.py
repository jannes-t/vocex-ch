import regex
import os
import re
import epub_conversion
import jieba
import sys
import logging

def source_to_txt(filename):
    """ convert .txt or .epub to one string """
    if re.search('.epub', filename, flags=re.IGNORECASE) is not None:
        return epub_to_txt(filename)
    elif re.search('.txt', filename, flags=re.IGNORECASE) is not None:
        f = open(filename)
        with f:
            text = f.read()
            f.close()
        return text
    else:
        return None

def epub_to_txt(filename):
    """ convert epub specified by filename to one string """
    book = epub_conversion.utils.open_book(filename)
    lines =  epub_conversion.utils.convert_epub_to_lines(book)
    # text = epub_conversion.utils.convert_lines_to_text(lines,'')
    text2 = ''
    for line in lines:
        text2+=line
    return text2

def extract_vocab(text):
    """ convert string of text to set of chinese vocab """
    # load user dict - determine correct path for resources
    base_path = get_base_path_resources()
    logging.debug('Base path of resource folder: {}'.format(base_path))
    dictpath = os.path.join(base_path, 'resources/simpl-dict.txt')
    logging.debug('Is path to dictionary correct: {}'
            .format(os.path.isfile(dictpath)))
    logging.debug('Current wd: {}'.format(os.getcwd()))

    jieba.load_userdict(dictpath)
    # jieba.initialize('resources/simpl-dict.txt')

    seg_list = jieba.cut(text, cut_all=False)
    vocab = list()
    for word in seg_list:
        vocab.append(word)

    pattern = regex.compile(r'\p{IsHan}', re.UNICODE)
    vocab_set = set()
    for word in vocab:
        isChinese = True
        for character in word:
            if (pattern.match(character) is None):
                isChinese = False
        if isChinese:
            vocab_set.add(word)
    return vocab_set

def extract_user_vocab(lines):
    vocab = set()
    for line in lines:
        vocab.add(line.split('\t')[0])
    return vocab

def read_skritter_vocab(filename):
    f = open(filename)
    lines = f.readlines()
    return extract_user_vocab(lines)

def write_vocab_to_file(vocab, filename, split = False):
    stripped = filename_strip_txt_ext(filename)
    if split:
        write_vocab_to_file_split(vocab, stripped)
    else:
        write_vocab_to_file_single(vocab, stripped)

def write_vocab_to_file_single(vocab, filename):
    f = open('{}.txt'.format(filename), 'wt')
    with f:
        for word in vocab:
            f.write('{}\n'.format(word))
        f.close()

def write_vocab_to_file_split(vocab, filename):
    set_of_sets = set()
    counter = 0
    subset = set()
    for word in vocab:
        subset.add(word)
        counter += 1
        if counter == 200:
            set_of_sets.add(frozenset(subset))
            subset.clear()
            counter = 0
    for i, s in enumerate(set_of_sets):
        write_vocab_to_file(s, '{}{}'.format(filename, i))

def get_base_path_resources():
    """ get base path of folder containing resources """
    # if bundled as folder or onefile with pyinstaller
    base_path = None
    if getattr( sys, 'frozen', False ) :
        # running in a bundle
        base_path = sys._MEIPASS
    else :
        # running live
        base_path = os.path.abspath(os.path.dirname(__file__))
    return base_path

# def filename_without_extension(filename):
#     return os.path.splittext(filename)[0]

def filename_strip_txt_ext(filename):
    pattern = re.compile(r'\.txt$', re.IGNORECASE)
    return re.sub(pattern, '', filename)

