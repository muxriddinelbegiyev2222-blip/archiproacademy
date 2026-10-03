@echo off
setlocal EnableExtensions

title ARCHIPRO UZ - CLEAN TEST RESET

echo.
echo ============================================================
echo           ARCHIPRO UZ - CLEAN TEST RESET
echo ============================================================
echo.
echo Bu faqat TEST uchun.
echo.
echo ARCHIPRO UZ lokal ma'lumotlari backup qilinadi:
echo - database
echo - login/user
echo - progress
echo - license
echo.
echo ADMIN private key O'CHIRILMAYDI.
echo.

pause

set "APPDATA_DIR=%LOCALAPPDATA%\ARCHIPRO_UZ"
set "BACKUP_ROOT=%LOCALAPPDATA%\ARCHIPRO_UZ_TEST_BACKUPS"

if not exist "%APPDATA_DIR%" (
    echo.
    echo [INFO] ARCHIPRO_UZ lokal data topilmadi.
    echo Dastur allaqachon toza holatda.
    echo.
    pause
    exit /b 0
)

if not exist "%BACKUP_ROOT%" (
    mkdir "%BACKUP_ROOT%"
)

for /f %%I in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd_HHmmss"') do (
    set "STAMP=%%I"
)

set "BACKUP_DIR=%BACKUP_ROOT%\ARCHIPRO_UZ_%STAMP%"

echo.
echo Backup yaratilmoqda...
echo.
echo FROM:
echo %APPDATA_DIR%
echo.
echo TO:
echo %BACKUP_DIR%
echo.

move "%APPDATA_DIR%" "%BACKUP_DIR%" >nul

if errorlevel 1 (
    echo.
    echo [ERROR] Backup qilishda xato yuz berdi.
    echo.
    echo ARCHIPRO UZ dasturi yopiq ekanini tekshiring.
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo                     RESET TAYYOR
echo ============================================================
echo.
echo [PASS] Eski ma'lumotlar backup qilindi.
echo.
echo Backup:
echo %BACKUP_DIR%
echo.
echo Endi ARCHIPRO UZ ni oching.
echo Aktivatsiya oynasi chiqishi kerak.
echo.
echo MUHIM:
echo ARCHIPRO_UZ_ADMIN papkasi va PRIVATE KEY saqlanib qoldi.
echo.
pause

exit /b 0
