pyinstaller -y --add-data=./images/Heart.png:. --icon=./images/Heart.png --onedir --noconsole Heart.py
cp -rf ./dist/Heart.app /Users/$USER/Desktop/
