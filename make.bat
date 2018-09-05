pipenv run pyinstaller --onefile --windowed --add-data jieba/;jieba --add-data src/resources/;resources -icon=icon.ico --noconfirm --hidden-import PyQt5.sip src/qtmain.py
