import sys
import os
import functions as fn
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QErrorMessage, QLabel
from PyQt5.QtGui import QMovie
from mainwindow import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.in_filepath = None
        self.vocab_filepath = None
        self.out_filepath = None
        self.ui = None
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

        # movie = QMovie('resources/load.gif')
        movie = QMovie("load.gif")
        loading = self.ui.loadingLabel
        status = self.ui.statusLabel
        loading.setMovie(movie)
        loading.setScaledContents(True)
        movie.start()
        loading.show()
        status.setText('extracting')
        status.show()

        name, _ = QFileDialog.getSaveFileName(None, 'save as')
        if (name == ''):
            movie.stop()
            loading.hide()
            status.setText('')
            return

        vocab = fn.extract_vocab(text)
        if (user_vocab is not None):
            vocab = vocab.difference(user_vocab)
        f = open(name, 'wt')
        with f:
            for word in vocab:
                f.write(word+'\n')
            f.close()
        movie.stop()
        loading.hide()
        status.setText('Done. Amount of words: ' + str(len(vocab)))


app = QApplication(sys.argv)
main = Main()
sys.exit(app.exec_())

