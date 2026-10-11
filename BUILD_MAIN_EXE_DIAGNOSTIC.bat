@echo off
setlocal EnableExtensions
cd /d "%~dp0"
title ARCHIPRO UZ - ASOSIY DASTUR EXE TEKSHIRUVI

echo.
echo =========================================================
echo  ARCHIPRO UZ - 680 DARSLI ASOSIY DASTURNI EXE QILISH
echo =========================================================
echo Bu MASTER yoki ADMIN emas. Bu ASOSIY O'QUV DASTURI.
echo Xatolar build_logs papkasida saqlanadi.
echo Mavjud OWNER / ADMIN va amaldagi EXE o'chirilmaydi.
echo.

if not exist "tools\diagnose_client_build.py" (
  echo [ERROR] Yangi GitHub ZIP to'liq yuklanmagan.
  echo tools\diagnose_client_build.py fayli mavjud emas.
  goto failed
)
where python >nul 2>&1
if errorlevel 1 (
  echo [ERROR] Python PATH ichida topilmadi.
  echo Python 3.12 x64 o'rnatilganini tekshiring.
  goto failed
)
python "tools\diagnose_client_build.py"
if errorlevel 1 goto failed

echo.
echo =========================================================
echo [PASS] 680 DARSLI ASOSIY ARCHIPRO UZ.exe TAYYOR.
echo Dist papkalarida EXE mavjud. Dasturga kiring va sinang.
echo =========================================================
echo.
pause
exit /b 0

:failed
echo.
echo =========================================================
echo [FAILED] BUILD XATO BILAN TO'XTADI
echo build_logs papkasidagi CLIENT_EXE_BUILD_...log
echo faylining OXIRGI 30 QATORINI menga yuboring.
echo .pkg fayl yakuniy EXE emas.
echo =========================================================
echo.
pause
exit /b 1
