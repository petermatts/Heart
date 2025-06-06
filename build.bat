@REM @echo off
pyinstaller --add-data=.\images\Heart.png:. --icon=.\images\Heart.png --onefile --noconsole Heart.py
COPY /B /Y .\dist\Heart.exe %USERPROFILE%\Desktop\
COPY /B /Y .\dist\Heart.exe %USERPROFILE%\OneDrive\Desktop\