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
    goto failed
)
if not exist "tools\check_license_signature.py" (
    echo [XATO] tools\\check_license_signature.py mavjud emas.
    echo Faylni GitHub'dan yuklab tools papkasiga saqlang.
    echo Yoki ikki faylli yangi tekshiruv ZIP paketini ishlating.
    goto failed
)
python -c "import cryptography" >nul 2>&1
if errorlevel 1 (
    echo [XATO] cryptography o'rnatilmagan.
    echo Quyidagi buyruqni bajaring: python -m pip install cryptography
    goto failed
)
if not "%~1"=="" (
    python tools\check_license_signature.py "%~1"
) else (
    python tools\check_license_signature.py
)
if errorlevel 1 goto failed
echo.
echo [OK] Diagnostika bajarildi. Ekrandagi moslik natijasini yuboring.
echo.
pause
exit /b 0

:failed
echo.
echo [XATO] Tekshiruv oxirigacha bajarilmadi. Hech qanday kalit o'zgartirilmadi.
echo Shu oynaning rasm yoki matnini yuboring.
echo.
pause
exit /b 1
