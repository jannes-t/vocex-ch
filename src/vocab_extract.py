import click
import functions as f
import os


@click.command()
@click.option('--skritter', default=None,
help='filename of textfile with skritter vocabulary')
@click.option('--split', is_flag=True,
help='split outfile in files with 200 words each')
@click.argument('infile')
@click.argument('outfile')
def extract(infile, outfile, skritter, split):
    if (not os.path.isfile(infile)):
        print('invalid input filename')
        exit()
    text = f.source_to_txt(infile)

    if text is None:
        print('invalid filetype')
        exit()

    user_vocab = None
    if skritter is not None:
        if not os.path.isfile(skritter):
            print('invalid skritter vocab filename')
            exit()
        else:
            user_vocab = f.read_skritter_vocab(skritter)

    text_vocab = f.extract_vocab(text)
    if user_vocab is not None:
        text_vocab = text_vocab.difference(user_vocab)
    f.write_vocab_to_file(text_vocab, outfile, split)


if __name__ == '__main__':
    extract()
