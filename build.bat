@echo off
pyinstaller --add-data=.\images\Heart.png:. --icon=.\images\Heart.png --onefile --noconsole Heart.py
copy .\dist\Heart.exe %USERPROFILE%\Desktop