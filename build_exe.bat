@echo off
REM Builds dist\MyceliumBase.exe. Needs Python 3 on PATH.
python -m pip install --upgrade -r requirements.txt
python -m PyInstaller --noconfirm --onefile --windowed --name MyceliumBase --add-data "index.html;." launch.py
echo.
echo Done. Your game is at dist\MyceliumBase.exe
pause
