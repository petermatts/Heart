source ./.venv/bin/activate
./.venv/bin/pyinstaller -y --add-data=./images/Heart.png:. --icon=./images/Heart.png --onedir --noconsole Heart.py
deactivate
cp -rf ./dist/Heart.app /Users/$USER/Desktop/
