@echo off
setlocal

title Start EVE - Evercrew Local AI Operating System
color 0B

echo =====================================================
echo.
echo            Starting EVE v0.1 Alpha
echo      Evercrew Local AI Operating System
echo.
echo =====================================================
echo.

echo [1/4] Checking EVE installation...
echo.

if not exist .venv (
color 0C
echo ERROR:
echo.
echo EVE has not been installed yet.
echo.
echo Please run:
echo.
echo     Install EVE.bat
echo.
pause
exit /b 1
)

if not exist app\main.py (
color 0C
echo ERROR:
echo.
echo EVE application file was not found.
echo.
echo Please make sure you are running this file
echo inside the EVE folder.
echo.
pause
exit /b 1
)

echo EVE installation found.
echo.

echo [2/4] Checking Ollama...
echo.

ollama --version >nul 2>&1

if errorlevel 1 (
color 0C
echo ERROR:
echo.
echo Ollama is not installed.
echo.
echo Please download Ollama:
echo https://ollama.com/download
echo.
pause
exit /b 1
)

echo Ollama detected.
echo.

echo Checking AI model...
echo.

ollama list | findstr /I "llama3.2:3b" >nul

if errorlevel 1 (
color 0C
echo ERROR:
echo.
echo The required AI model was not found.
echo.
echo Please open Command Prompt and run:
echo.
echo     ollama pull llama3.2:3b
echo.
echo After the download finishes,
echo run Start EVE.bat again.
echo.
pause
exit /b 1
)

echo AI model detected.
echo.

echo [3/4] Checking configuration...
echo.

if not exist .env (
color 0C
echo ERROR:
echo.
echo The .env file was not found.
echo.
echo Please run Install EVE.bat again.
echo.
pause
exit /b 1
)

echo Configuration file found.
echo.

echo [4/4] Starting EVE...
echo.

echo =====================================================
echo.
echo EVE is now starting.
echo.
echo Do NOT close this window while EVE is running.
echo.
echo To stop EVE, press CTRL + C in this window.
echo.
echo =====================================================
echo.

.venv\Scripts\python.exe -m app.main

echo.
echo =====================================================
echo.
echo EVE has stopped.
echo.
echo If EVE stopped unexpectedly,
echo please read the messages above.
echo.
echo Help:
echo https://github.com/EVE-ECV/EVE
echo.
echo =====================================================
echo.

pause
