@echo off
setlocal EnableExtensions
cd /d "%~dp0"
title ARCHIPRO UZ - LITSENZIYA IMZOSI TEKSHIRUVI
echo.
echo ================================================================
echo ARCHIPRO UZ - MAXFIY KALITNI OSHKOR QILMASDAN IMZO TEKSHIRUVI
echo ================================================================
echo.
echo Bu tekshiruv kalitlarni O'ZGARTIRMAYDI.
echo Private keyni HECH KIMGA yubormang.
echo.

where python >nul 2>&1
if errorlevel 1 (
    echo [XATO] Python topilmadi. Python 3.12 x64 kerak.
    goto finished
)
if not exist "tools\check_license_signature.py" (
    echo [XATO] Dastur fayli topilmadi. GitHub ZIPni to'liq chiqaring.
    goto finished
)
python -c "import cryptography" >nul 2>&1
if errorlevel 1 (
    echo [XATO] cryptography o'rnatilmagan.
    echo Quyidagi buyruqni bajaring: python -m pip install cryptography
    goto finished
)
if not "%~1"=="" (
    python tools\check_license_signature.py "%~1"
) else (
    python tools\check_license_signature.py
)
:finished
echo.
echo Imzo mosligi tekshirildi. Shu oynaning rasm yoki matnini yuboring.
echo.
pause
exit /b 0
