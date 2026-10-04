@echo off
setlocal

cd /d "%~dp0"

title ARCHIPRO UZ - DEBUG

echo.
echo ================================================
echo ARCHIPRO UZ DEBUG MODE
echo ================================================
echo.
echo Dastur ochiladi.
echo Litsenziya yo'q bo'lsa avval AKTIVATSIYA oynasi chiqadi.
echo Litsenziya haqiqiy bo'lsa LOGIN oynasi chiqadi.
echo Agar xato bo'lsa, shu qora oynada yoziladi.
echo.

python app\main.py

echo.
echo ================================================
echo DASTUR TO'XTADI
echo ================================================
echo.

pause
