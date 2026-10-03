@echo off
cd /d "%~dp0"

title ARCHIPRO UZ - CONTENT GUARD

echo.
echo ============================================================
echo ARCHIPRO UZ - CONTENT HIMOYA TEKSHIRUVI
echo ============================================================
echo.

python app\tools\content_guard.py

echo.
pause
