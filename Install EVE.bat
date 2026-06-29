@echo off
setlocal

title Install EVE - Evercrew Local AI Operating System
color 0A

echo =====================================================
echo.
echo             EVE v0.1 Alpha Installer
echo      Evercrew Local AI Operating System
echo.
echo =====================================================
echo.
echo Welcome!
echo.
echo This installer will prepare EVE on your Windows computer.
echo.
echo =====================================================
echo BEFORE WE BEGIN
echo =====================================================
echo.
echo EVE will be installed inside its own private folder.
echo.
echo It will NOT:
echo.
echo   - Change your Windows settings
echo   - Replace your Python installation
echo   - Affect your other Python projects
echo   - Affect software such as Aider
echo.
echo EVE uses its own private Python environment
echo called ".venv", which keeps everything separate
echo from the rest of your computer.
echo.
echo This means you can remove the EVE folder later
echo without affecting your other software.
echo.
echo During installation you may see technical messages.
echo.
echo This is normal.
echo If the installer finishes with:
echo.
echo     INSTALLATION COMPLETED SUCCESSFULLY
echo.
echo then EVE has been installed correctly.
echo.
echo Press any key to begin installation...
pause >nul
cls

:: ----------------------------------------------------
:: STEP 1 - CHECK PYTHON
:: ----------------------------------------------------

echo [1/6] Checking Python...
echo.

python --version >nul 2>&1

if errorlevel 1 (
    color 0C
    echo ERROR:
    echo Python is not installed.
    echo.
    echo Please download Python:
    echo https://www.python.org/downloads/
    echo.
    echo IMPORTANT:
    echo During installation, tick:
    echo [✓] Add Python to PATH
    echo.
    pause
    exit /b 1
)

python --version
echo.
echo ✓ Python detected.
echo.

:: ----------------------------------------------------
:: STEP 2 - CHECK OLLAMA
:: ----------------------------------------------------

echo [2/6] Checking Ollama...
echo.

ollama --version >nul 2>&1

if errorlevel 1 (
    color 0C
    echo ERROR:
    echo Ollama is not installed.
    echo.
    echo Please download Ollama:
    echo https://ollama.com/download
    echo.
    pause
    exit /b 1
)

ollama --version
echo.
echo ✓ Ollama detected.
echo.

:: ----------------------------------------------------
:: STEP 3 - CHECK REQUIREMENTS
:: ----------------------------------------------------

echo [3/6] Checking installation files...
echo.

if not exist requirements.txt (
    color 0C
    echo ERROR:
    echo requirements.txt not found.
    echo.
    echo Please make sure you are running this installer
    echo inside the EVE folder.
    echo.
    pause
    exit /b 1
)

echo ✓ Installation files found.
echo.

:: ----------------------------------------------------
:: STEP 4 - CREATE VIRTUAL ENVIRONMENT
:: ----------------------------------------------------

echo [4/6] Preparing isolated Python environment...
echo.

if not exist .venv (

    echo Creating virtual environment...
    python -m venv .venv

    if errorlevel 1 (
        color 0C
        echo.
        echo ERROR:
        echo Failed to create Python virtual environment.
        echo.
        pause
        exit /b 1
    )

) else (

    echo Existing virtual environment found.
    echo Reusing existing environment.

)

echo.

call .venv\Scripts\activate.bat

echo Updating pip...

python -m pip install --upgrade pip setuptools wheel >nul

echo.
echo Installing EVE packages...
echo.
echo This may take several minutes...
echo.

pip install -r requirements.txt

if errorlevel 1 (
    color 0C
    echo.
    echo ERROR:
    echo Failed to install EVE packages.
    echo.
    echo Please check your internet connection
    echo and try again.
    echo.
    pause
    exit /b 1
)

echo.
echo ✓ Python packages installed successfully.
echo.

:: ----------------------------------------------------
:: STEP 5 - CREATE ENV FILE
:: ----------------------------------------------------

echo [5/6] Preparing configuration...
echo.

if not exist .env (

    if exist .env.example (

        copy .env.example .env >nul
        echo ✓ .env created from .env.example

    ) else (

        echo.
        echo WARNING:
        echo .env.example not found.
        echo Please create .env manually.

    )

) else (

    echo ✓ Existing .env detected.

)

echo.

:: ----------------------------------------------------
:: STEP 6 - FINISH
:: ----------------------------------------------------

echo [6/6] Finalising installation...
echo.

echo =====================================================
echo.
echo           INSTALLATION COMPLETED SUCCESSFULLY
echo.
echo =====================================================
echo.

echo Next Steps
echo ----------
echo.
echo 1. Open the .env file.
echo.
echo 2. Paste your Telegram Bot Token.
echo.
echo 3. Open:
echo    data\employees.json
echo.
echo    Replace the sample employees with your own.
echo.
echo 4. If you have not downloaded the AI model yet:
echo.
echo    ollama pull llama3.2:3b
echo.
echo 5. Double-click:
echo.
echo    Start EVE.bat
echo.
echo to start EVE.
echo.

echo -----------------------------------------------------
echo Need help?
echo.
echo Website:
echo https://evercrew.ai
echo.
echo GitHub:
echo https://github.com/EVE-ECV/EVE
echo.
echo Email:
echo support@evercrew.ai
echo -----------------------------------------------------
echo.

pause@echo off
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
