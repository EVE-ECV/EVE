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
echo EVE installs inside this folder only.
echo.
echo It will NOT:
echo.
echo   - Change your Windows settings
echo   - Replace your Python installation
echo   - Affect your other Python projects
echo   - Affect other software such as Aider
echo.
echo You can remove EVE later by deleting this folder.
echo.
echo Estimated installation time:
echo 1 to 3 minutes.
echo.
echo Press any key to begin installing EVE.
pause >nul
cls

echo =====================================================
echo             Installing EVE v0.1 Alpha
echo =====================================================
echo.

echo Installation location:
echo %CD%
echo.

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
echo Add Python to PATH
echo.
pause
exit /b 1
)

python --version
echo.
echo Python detected.
echo.

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
echo Ollama detected.
echo.

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

echo Installation files found.
echo.

echo [4/6] Preparing EVE private folder...
echo.

if not exist .venv (
echo Creating EVE private folder...
python -m venv .venv

```
if errorlevel 1 (
    color 0C
    echo.
    echo ERROR:
    echo Failed to create EVE private folder.
    echo.
    echo Please check your Python installation and try again.
    echo.
    pause
    exit /b 1
)
```

) else (
echo Existing EVE private folder found.
echo Reusing existing folder.
)

echo.
echo Updating EVE environment...
echo.

.venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel >nul

if errorlevel 1 (
color 0C
echo.
echo ERROR:
echo Failed to update the EVE environment.
echo.
echo Your computer has NOT been damaged.
echo.
pause
exit /b 1
)

echo.
echo Installing EVE packages...
echo.
echo This may take several minutes...
echo.

.venv\Scripts\python.exe -m pip install -r requirements.txt

if errorlevel 1 (
color 0C
echo.
echo =====================================================
echo INSTALLATION FAILED
echo =====================================================
echo.
echo EVE could not finish installing.
echo.
echo This may be caused by Windows security settings,
echo antivirus software, internet connection issues,
echo or your organisation's security policy.
echo.
echo Your computer has NOT been damaged.
echo.
echo Please visit:
echo https://evercrew.ai
echo.
echo GitHub:
echo https://github.com/EVE-ECV/EVE
echo.
pause
exit /b 1
)

echo.
echo Python packages installed successfully.
echo.

echo [5/6] Preparing configuration...
echo.

if not exist .env (
if exist .env.example (
copy .env.example .env >nul
echo .env created from .env.example.
) else (
echo WARNING:
echo .env.example not found.
echo Please create .env manually.
)
) else (
echo Existing .env detected.
)

echo.

echo [6/6] Finalising installation...
echo.

echo =====================================================
echo.
echo      INSTALLATION COMPLETED SUCCESSFULLY
echo.
echo =====================================================
echo.
echo Good news!
echo.
echo EVE has been installed successfully.
echo.
echo Your other software has NOT been modified.
echo.
echo EVE is installed inside this folder only.
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
echo [support@evercrew.ai](mailto:support@evercrew.ai)
echo -----------------------------------------------------
echo.

pause
