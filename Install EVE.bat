@echo off
title Install EVE - Evercrew Local AI Operating System
color 0A

echo =====================================================
echo  EVE v0.1 Alpha - Installer
echo  Evercrew Local AI Operating System for SMEs
echo =====================================================
echo.
echo Welcome boss!
echo This installer will prepare EVE on your Windows computer.
echo.

echo [1/5] Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
echo.
echo ERROR: Python is not installed or not added to PATH.
echo.
echo Please install Python first:
echo https://www.python.org/downloads/
echo.
echo IMPORTANT:
echo During installation, tick "Add Python to PATH".
echo.
pause
exit /b 1
)

python --version
echo Python check passed.
echo.

echo [2/5] Checking Ollama...
ollama --version >nul 2>&1
if errorlevel 1 (
echo.
echo ERROR: Ollama is not installed or not available.
echo.
echo Please install Ollama first:
echo https://ollama.com/download
echo.
pause
exit /b 1
)

ollama --version
echo Ollama check passed.
echo.

echo [3/5] Checking requirements.txt...
if not exist requirements.txt (
echo.
echo ERROR: requirements.txt not found.
echo.
echo Please make sure you are running this file inside the EVE folder.
echo.
pause
exit /b 1
)

echo requirements.txt found.
echo.

echo [4/5] Preparing Python...

python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
python -m pip install --upgrade wheel

echo.
echo Installing EVE packages...
python -m pip install -r requirements.txt

if errorlevel 1 (
echo.
echo ERROR: Python package installation failed.
echo.
echo Please check your internet connection and try again.
echo.
pause
exit /b 1
)

echo Python packages installed successfully.
echo.

echo [5/5] Creating .env file if needed...
if not exist .env (
if exist .env.example (
copy .env.example .env >nul
echo .env file created from .env.example.
) else (
echo WARNING: .env.example not found.
echo Please create .env manually before starting EVE.
)
) else (
echo .env already exists. No changes made.
)

echo.
echo =====================================================
echo  Installation completed!
echo =====================================================
echo.
echo Next steps:
echo 1. Open the .env file and add your Telegram Bot Token.
echo 2. Check data\employees.json and update employee details.
echo 3. Download the AI model if not done yet:
echo    ollama pull llama3.2:3b
echo 4. Double-click Start EVE.bat to run EVE.
echo.
echo Support: [support@evercrew.ai](mailto:support@evercrew.ai)
echo Website: https://evercrew.ai
echo.
pause
