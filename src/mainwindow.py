# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 446)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.inputTextEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.inputTextEdit.setGeometry(QtCore.QRect(90, 70, 301, 51))
        self.inputTextEdit.setObjectName("inputTextEdit")
        self.inputLabel = QtWidgets.QLabel(self.centralWidget)
        self.inputLabel.setGeometry(QtCore.QRect(120, 40, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.inputLabel.setFont(font)
        self.inputLabel.setObjectName("inputLabel")
        self.extractButton = QtWidgets.QPushButton(self.centralWidget)
        self.extractButton.setGeometry(QtCore.QRect(80, 310, 151, 61))
        self.extractButton.setObjectName("extractButton")
        self.chooseFileButton = QtWidgets.QPushButton(self.centralWidget)
        self.chooseFileButton.setGeometry(QtCore.QRect(400, 80, 111, 41))
        self.chooseFileButton.setObjectName("chooseFileButton")
        self.loadingLabel = QtWidgets.QLabel(self.centralWidget)
        self.loadingLabel.setGeometry(QtCore.QRect(260, 330, 21, 21))
        self.loadingLabel.setText("")
        self.loadingLabel.setObjectName("loadingLabel")
        self.statusLabel = QtWidgets.QLabel(self.centralWidget)
        self.statusLabel.setGeometry(QtCore.QRect(330, 330, 231, 16))
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        self.chunksCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.chunksCheckBox.setGeometry(QtCore.QRect(90, 140, 171, 20))
        self.chunksCheckBox.setObjectName("chunksCheckBox")
        self.vocabCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.vocabCheckBox.setGeometry(QtCore.QRect(90, 170, 241, 20))
        self.vocabCheckBox.setObjectName("vocabCheckBox")
        self.inputTextEdit_2 = QtWidgets.QTextEdit(self.centralWidget)
        self.inputTextEdit_2.setEnabled(True)
        self.inputTextEdit_2.setGeometry(QtCore.QRect(90, 240, 301, 51))
        self.inputTextEdit_2.setReadOnly(False)
        self.inputTextEdit_2.setObjectName("inputTextEdit_2")
        self.inputLabel_2 = QtWidgets.QLabel(self.centralWidget)
        self.inputLabel_2.setGeometry(QtCore.QRect(120, 210, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.inputLabel_2.setFont(font)
        self.inputLabel_2.setObjectName("inputLabel_2")
        self.chooseFileButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.chooseFileButton_2.setGeometry(QtCore.QRect(400, 250, 111, 41))
        self.chooseFileButton_2.setObjectName("chooseFileButton_2")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 615, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuChineseVocabExtractor = QtWidgets.QMenu(self.menuBar)
        self.menuChineseVocabExtractor.setObjectName("menuChineseVocabExtractor")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.menuBar.addAction(self.menuChineseVocabExtractor.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inputLabel.setText(_translate("MainWindow", "Input filepath (.epub or .txt):"))
        self.extractButton.setText(_translate("MainWindow", "Extract vocabulary"))
        self.chooseFileButton.setText(_translate("MainWindow", "choose file"))
        self.chunksCheckBox.setText(_translate("MainWindow", "split in 200 word chunks"))
        self.vocabCheckBox.setText(_translate("MainWindow", "check against vocabulary (.txt file)"))
        self.inputLabel_2.setText(_translate("MainWindow", "Vocabulary filepath (.txt):"))
        self.chooseFileButton_2.setText(_translate("MainWindow", "choose file"))
        self.menuChineseVocabExtractor.setTitle(_translate("MainWindow", "ChineseVocabExtractor"))

