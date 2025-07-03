@REM @echo off
CALL .\.venv\Scripts\activate
.\.venv\Scripts\pyinstaller.exe --add-data=.\images\Heart.png:. --icon=.\images\Heart.png --onefile --noconsole Heart.py
deactivate
COPY /B /Y .\dist\Heart.exe %USERPROFILE%\Desktop\
COPY /B /Y .\dist\Heart.exe %USERPROFILE%\OneDrive\Desktop\