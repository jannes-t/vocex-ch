pipenv run pyinstaller --onefile --windowed --add-data jieba/;jieba --add-data src/resources/;resources --noconfirm --hidden-import PyQt5.sip src/qtmain.py
