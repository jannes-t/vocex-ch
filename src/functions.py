import regex
import re
import epub_conversion
import jieba

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
    jieba.load_userdict('resources/simpl-dict.txt')
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

def write_vocab_to_file(vocab, filename):
    f = open(filename, 'wt')
    with f:
        for word in vocab:
            f.write(word+'\n')
        f.close()
