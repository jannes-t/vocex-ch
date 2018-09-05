rm -rf dist/qtmain dist/qtmain.app
pipenv run pyinstaller --onefile --windowed \
    --add-data jieba/:jieba \
    --add-data src/resources/:resources --noconfirm \
    --name Hanzi-extract \
    --icon icon.icns \
    --hidden-import PyQt5.sip src/qtmain.py 
cp -f Info2.plist dist/Hanzi-extract.app/Contents/Info.plist
