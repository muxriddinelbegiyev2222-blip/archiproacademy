@echo off
setlocal EnableExtensions

cd /d "%~dp0"

title ARCHIPRO OWNER BUILD

echo.
echo ============================================================
echo              ARCHIPRO OWNER BUILD
echo ============================================================
echo.

set "ROOT=%CD%"
set "ICON=%ROOT%\archipro.ico"
set "OWNER_FILE=%ROOT%\app\owner.py"
set "PRIVATE_KEY=%LOCALAPPDATA%\ARCHIPRO_UZ_ADMIN\keys\archipro_private.key"

if not exist "%OWNER_FILE%" (
    echo [ERROR] app\owner.py topilmadi.
    echo.
    pause
    exit /b 1
)

if not exist "%ICON%" (
    echo [ERROR] archipro.ico topilmadi.
    echo.
    echo Qidirilgan joy:
    echo %ICON%
    echo.
    pause
    exit /b 1
)

if not exist "%PRIVATE_KEY%" (
    echo [ERROR] PRIVATE KEY topilmadi.
    echo.
    echo Qidirilgan joy:
    echo %PRIVATE_KEY%
    echo.
    pause
    exit /b 1
)

echo [PASS] owner.py topildi.
echo [PASS] archipro.ico topildi.
echo [PASS] Private key topildi.
echo.

python -m pip install --upgrade pyinstaller

if errorlevel 1 (
    echo.
    echo [ERROR] PyInstaller tayyorlanmadi.
    pause
    exit /b 1
)

if exist "%ROOT%\build_owner" (
    rmdir /s /q "%ROOT%\build_owner"
)

if exist "%ROOT%\dist_owner" (
    rmdir /s /q "%ROOT%\dist_owner"
)

echo.
echo ARCHIPRO OWNER.exe build qilinmoqda...
echo.

python -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --name "ARCHIPRO OWNER" ^
    --icon "%ICON%" ^
    --paths "%ROOT%\app" ^
    --collect-all PySide6 ^
    --distpath "%ROOT%\dist_owner" ^
    --workpath "%ROOT%\build_owner" ^
    "%OWNER_FILE%"

if errorlevel 1 (
    echo.
    echo ============================================================
    echo [ERROR] OWNER build muvaffaqiyatsiz.
    echo ============================================================
    echo.
    pause
    exit /b 1
)

if not exist "%ROOT%\dist_owner\ARCHIPRO OWNER.exe" (
    echo.
    echo [ERROR] ARCHIPRO OWNER.exe topilmadi.
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo                  OWNER BUILD TAYYOR
echo ============================================================
echo.
echo [PASS]
echo %ROOT%\dist_owner\ARCHIPRO OWNER.exe
echo.
echo MUHIM:
echo   - OWNER.exe faqat sizda qoladi.
echo   - Private key EXE ichiga joylanmaydi.
echo   - Mijozga OWNER.exe berilmaydi.
echo.
pause
