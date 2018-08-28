import sys
import os
import functions as fn
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QErrorMessage, QLabel
from PyQt5.QtGui import QMovie
from mainwindow import Ui_MainWindow
import concurrent.futures as futures
import logging

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.in_filepath = None
        # self.vocab_filepath = None
        # self.out_filepath = None
        logging.basicConfig(level=logging.DEBUG)
        self.ui = None
        self.ppool = futures.ProcessPoolExecutor(max_workers=1)
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Chinese Vocabulary Extractor')
        self.setUnifiedTitleAndToolBarOnMac(True)

        self.ui.chooseFileButton_2.setEnabled(False)
        self.ui.inputTextEdit_2.setEnabled(False)
        self.ui.chooseFileButton.clicked.connect(self.select_input_file)
        self.ui.chooseFileButton_2.clicked.connect(self.select_vocab_file)
        self.ui.extractButton.clicked.connect(self.extract)
        self.ui.vocabCheckBox.stateChanged.connect(self.on_vocab_checked)
        self.show()

    def on_vocab_checked(self, state):
        # 0 means unchecked, 2 means checked
        if (state == 2):
            self.ui.chooseFileButton_2.setEnabled(True)
            self.ui.inputTextEdit_2.setEnabled(True)
        else:
            self.ui.chooseFileButton_2.setEnabled(False)
            self.ui.inputTextEdit_2.clear()
            self.ui.inputTextEdit_2.setEnabled(False)

    def select_input_file(self):
        name, _ = QFileDialog.getOpenFileName(None,
                'Choose source file (epub or txt')
        self.ui.inputTextEdit.setText(name)

    def select_vocab_file(self):
        name, _ = QFileDialog.getOpenFileName(None,
                'Choose Skritter Vocabulary file (txt)')
        self.ui.inputTextEdit_2.setText(name)

    def input_file_to_text(self):
        name = self.ui.inputTextEdit.toPlainText()
        text = None
        text = fn.source_to_txt(name)
        return text

    def vocab_file_to_set(self):
        name = self.ui.inputTextEdit_2.toPlainText()
        if (os.path.isfile(name)):
            vocab_file = open(name, 'rt')
            lines = vocab_file.readlines()
            return fn.extract_user_vocab(lines)
        else:
            return None

    def extract(self):
        text = self.input_file_to_text()
        user_vocab = None
        if (text is None):
            error = QErrorMessage(self)
            error.showMessage('Please specify valid source file')
            return
        if (self.ui.vocabCheckBox.isChecked()):
            user_vocab = self.vocab_file_to_set()
            if (user_vocab is None):
                error = QErrorMessage(self)
                error.showMessage('Please specify valid User Vocabulary file')
                return

        pair = self.before_extract()
        if pair is None:
            return
        filename = pair[0]
        write_chunks = pair[1]

        # with futures.ProcessPoolExecutor(1) as executor:
        #     vocab_future = executor.submit(extract_worker, text, user_vocab,
        #             filename, write_chunks)
        #     vocab_future.add_done_callback(self.after_extract)
        vocab_future = self.ppool.submit(extract_worker, text, user_vocab,
                filename, write_chunks)
        vocab_future.add_done_callback(self.after_extract)

        logging.debug('returning from extract')

        # movie.stop()
        # loading.hide()
        # status.setText('Done. Amount of words: ' + str(len(vocab)))

    def before_extract(self):
        write_chunks = self.ui.chunksCheckBox.isChecked()
        filename, _ = QFileDialog.getSaveFileName(None, 'save as')
        if (filename == ''):
            error = QErrorMessage(self)
            error.showMessage('Please specify valid source file')
            return None

        # disable ui
        self.ui.chooseFileButton.setEnabled(False)
        self.ui.chooseFileButton_2.setEnabled(False)
        self.ui.extractButton.setEnabled(False)

        # enable extract animation
        load_res = os.path.join(fn.get_base_path_resources(),
                  'resources/load.gif')
        movie = QMovie(load_res)
        loading = self.ui.loadingLabel
        status = self.ui.statusLabel
        loading.setMovie(movie)
        loading.inherits
        loading.setScaledContents(True)
        movie.start()
        loading.show()
        status.setText('extracting')
        status.show()

        logging.debug('returning from before_extract')
        return (filename, write_chunks)


    def after_extract(self, vocab_future):
        amount_words = vocab_future.result();
        self.ui.loadingLabel.clear()
        self.ui.loadingLabel.hide()
        self.ui.statusLabel.setText('Done. Amount of words: {}'
                .format(amount_words))
        # re-enable ui
        self.ui.chooseFileButton.setEnabled(True)
        self.ui.chooseFileButton_2.setEnabled(True)
        self.ui.extractButton.setEnabled(True)
        logging.debug('returning from after_extract')


def extract_worker(text, user_vocab, filename, writeChunks):
    logging.debug('start running extract_worker')
    vocab = fn.extract_vocab(text)
    if (user_vocab is not None):
        vocab = vocab.difference(user_vocab)

    fn.write_vocab_to_file(vocab, filename, writeChunks)
    logging.debug('returning from extract_worker')
    return len(vocab)


def start():
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start()
