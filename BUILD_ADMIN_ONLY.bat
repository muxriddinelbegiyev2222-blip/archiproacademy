@echo off
setlocal EnableExtensions

title ARCHIPRO UZ - ADMIN BUILD

cd /d "%~dp0"

echo.
echo ============================================================
echo               ARCHIPRO ADMIN BUILD
echo ============================================================
echo.

where python >nul 2>&1

if errorlevel 1 (
    echo [ERROR] Python topilmadi.
    pause
    exit /b 1
)

python -c "import PySide6" >nul 2>&1

if errorlevel 1 (
    python -m pip install PySide6

    if errorlevel 1 (
        echo [ERROR] PySide6 o'rnatilmadi.
        pause
        exit /b 1
    )
)

python -c "import cryptography" >nul 2>&1

if errorlevel 1 (
    python -m pip install cryptography

    if errorlevel 1 (
        echo [ERROR] cryptography o'rnatilmadi.
        pause
        exit /b 1
    )
)

python -c "import PyInstaller" >nul 2>&1

if errorlevel 1 (
    python -m pip install --upgrade pyinstaller

    if errorlevel 1 (
        echo [ERROR] PyInstaller o'rnatilmadi.
        pause
        exit /b 1
    )
)

if not exist "app\admin.py" (
    echo [ERROR] app\admin.py topilmadi.
    pause
    exit /b 1
)

if not exist "%LOCALAPPDATA%\ARCHIPRO_UZ_ADMIN\keys\archipro_private.key" (
    echo.
    echo [ERROR] PRIVATE KEY TOPILMADI.
    echo.
    echo Avval GENERATE_LICENSE_KEYS.bat ni ishga tushiring.
    echo.
    pause
    exit /b 1
)

if exist "build_admin" (
    rmdir /s /q "build_admin"
)

if exist "dist_admin" (
    rmdir /s /q "dist_admin"
)

if exist "ARCHIPRO_ADMIN_OWNER.spec" (
    del /q "ARCHIPRO_ADMIN_OWNER.spec"
)

echo.
echo ARCHIPRO ADMIN.exe yaratilmoqda...
echo.

python -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --name "ARCHIPRO ADMIN" ^
    --paths "app" ^
    --workpath "build_admin" ^
    --distpath "dist_admin" ^
    --specpath "." ^
    --collect-all PySide6 ^
    "app\admin.py"

if errorlevel 1 (
    echo.
    echo [ERROR] ADMIN BUILD FAILED
    pause
    exit /b 1
)

if not exist "dist_admin\ARCHIPRO ADMIN.exe" (
    echo.
    echo [ERROR] ARCHIPRO ADMIN.exe topilmadi.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo                    ADMIN TAYYOR
echo ============================================================
echo.
echo [PASS]
echo dist_admin\ARCHIPRO ADMIN.exe
echo.
echo MUHIM:
echo Bu EXE mijozga BERILMAYDI.
echo Private key ham mijozga BERILMAYDI.
echo.
echo ============================================================

pause
exit /b 0
