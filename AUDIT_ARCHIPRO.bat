@echo off
setlocal
chcp 65001 >nul
cd /d "%~dp0"
title ARCHIPRO UZ - FULL SYSTEM AUDIT
set "PYTHON_CMD="
where python >nul 2>nul
if not errorlevel 1 set "PYTHON_CMD=python"
if not defined PYTHON_CMD (
    where py >nul 2>nul
    if not errorlevel 1 set "PYTHON_CMD=py"
)
if not defined PYTHON_CMD (
    echo [ERROR] Python topilmadi.
    pause
    exit /b 1
)
%PYTHON_CMD% "app\tools\full_audit.py"
set "AUDIT_RESULT=%errorlevel%"
pause
exit /b %AUDIT_RESULT%
