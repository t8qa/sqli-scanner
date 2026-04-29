@echo off
title sqli-scanner
color 0a


if exist "sqli-scanner.py" (

    python sqli-scanner.py %*
) else (
    echo [X] Error: sqli-scanner.py not found in current directory!
    echo Current directory: %cd%
    echo.
    echo Please place sqli-scanner.py in this folder or specify full path
    pause
    exit /b 1
)

echo.
echo [*] Scan finished
pause