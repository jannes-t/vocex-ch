rm -rf dist/qtmain dist/qtmain.app
pipenv run pyinstaller --onefile --windowed \
    --add-data jieba/:jieba \
    --add-data src/resources/:resources --noconfirm \
    --hidden-import PyQt5.sip src/qtmain.py 
cp -f Info.plist dist/qtmain.app/Contents/Info.plist
