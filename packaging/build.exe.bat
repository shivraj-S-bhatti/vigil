@echo off
python -m pip install --upgrade pip
pip install -r requirements.txt pyinstaller
pyinstaller --noconfirm --onefile --name VIGIL-Logwatch src\main.py ^
  --add-data "assets;assets"
echo EXE at dist\VIGIL-Logwatch.exe
