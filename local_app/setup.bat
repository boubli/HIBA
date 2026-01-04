@echo off
echo.
echo ==================================================
echo          HIBA Local - One-Click Setup
echo ==================================================
echo.

echo [1/3] Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies.
    echo Make sure Python 3.10+ is installed.
    pause
    exit /b 1
)

echo.
echo [2/3] Downloading HIBA model (4.5 GB)...
echo This may take a few minutes depending on your internet speed.
python download_model.py
if errorlevel 1 (
    echo.
    echo ERROR: Failed to download model.
    pause
    exit /b 1
)

echo.
echo [3/3] Setup complete! Starting HIBA...
echo.
python app.py

pause
