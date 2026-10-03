@echo off
setlocal EnableExtensions

cd /d "%~dp0"

title ARCHIPRO OWNER BUILD

echo.
echo ============================================================
echo              ARCHIPRO OWNER BUILD
echo ============================================================
echo.

if not exist "app\owner.py" (
    echo [ERROR] app\owner.py topilmadi.
    pause
    exit /b 1
)

if not exist "archipro.ico" (
    echo [ERROR] archipro.ico topilmadi.
    pause
    exit /b 1
)

set "PRIVATE_KEY=%LOCALAPPDATA%\ARCHIPRO_UZ_ADMIN\keys\archipro_private.key"

if not exist "%PRIVATE_KEY%" (
    echo [ERROR] PRIVATE KEY topilmadi:
    echo %PRIVATE_KEY%
    echo.
    pause
    exit /b 1
)

echo [PASS] Private key topildi.
echo.

python -m pip install --upgrade pyinstaller >nul

if errorlevel 1 (
    echo [ERROR] PyInstaller tayyorlanmadi.
    pause
    exit /b 1
)

if exist "build_owner" rmdir /s /q "build_owner"
if exist "dist_owner" rmdir /s /q "dist_owner"

echo ARCHIPRO OWNER.exe build qilinmoqda...
echo.

python -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --name "ARCHIPRO OWNER" ^
    --icon "archipro.ico" ^
    --paths "app" ^
    --collect-all PySide6 ^
    --distpath "dist_owner" ^
    --workpath "build_owner" ^
    --specpath "build_owner" ^
    "app\owner.py"

if errorlevel 1 (
    echo.
    echo [ERROR] OWNER build muvaffaqiyatsiz.
    pause
    exit /b 1
)

if not exist "dist_owner\ARCHIPRO OWNER.exe" (
    echo.
    echo [ERROR] ARCHIPRO OWNER.exe topilmadi.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo                    BUILD TAYYOR
echo ============================================================
echo.
echo [PASS] dist_owner\ARCHIPRO OWNER.exe
echo.
echo MUHIM:
echo   - OWNER.exe faqat sizda qoladi.
echo   - Private key EXE ichiga joylanmaydi.
echo   - Mijozga OWNER.exe berilmaydi.
echo.
pause
