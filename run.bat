@echo off
setlocal enabledelayedexpansion

echo =========================================================
echo            AI LEGAL ADVISOR BACKEND SERVER              
echo =========================================================
echo.

cd /d "%~dp0"

set "PY_CMD="

:: Check if py -3.10 works
py -3.10 --version >nul 2>&1
if %ERRORLEVEL% equ 0 (
    set "PY_CMD=py -3.10"
    goto :FOUND
)

:: Check if py launcher works
py --version >nul 2>&1
if %ERRORLEVEL% equ 0 (
    set "PY_CMD=py"
    goto :FOUND
)

:: Check direct Python 3.10 installation path
if exist "%LOCALAPPDATA%\Programs\Python\Python310\python.exe" (
    set "PY_CMD=%LOCALAPPDATA%\Programs\Python\Python310\python.exe"
    goto :FOUND
)

:: Fallback to python in PATH
python --version >nul 2>&1
if %ERRORLEVEL% equ 0 (
    set "PY_CMD=python"
    goto :FOUND
)

echo [ERROR] Python was not found on your system!
echo Please ensure Python 3.10+ is installed.
pause
exit /b 1

:FOUND
echo [OK] Using Python: %PY_CMD%
echo.

:: Free port 8000 if an old stale process is still holding it
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8000 ^| findstr LISTENING') do (
    echo [INFO] Freeing port 8000 (terminating stale process PID: %%a)...
    taskkill /F /PID %%a >nul 2>&1
)

echo [OK] Verifying installed packages...
%PY_CMD% -m pip install -r requirements.txt --quiet --no-warn-script-location

echo.
echo =========================================================
echo  SERVER READY:
echo  - Interactive Web App : http://127.0.0.1:8000/
echo  - Swagger API Docs    : http://127.0.0.1:8000/docs
echo  - System Health Status: http://127.0.0.1:8000/status
echo =========================================================
echo.
echo Press Ctrl+C in this window anytime to stop the server.
echo.

:: Automatically open browser after 2 seconds in background
start "" cmd /c "timeout /t 2 /nobreak >nul & start http://127.0.0.1:8000/"

%PY_CMD% -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload

pause
