@echo off
setlocal EnableExtensions EnableDelayedExpansion

title ARCHIPRO UZ - CLIENT RELEASE BUILD

cd /d "%~dp0"

echo.
echo ============================================================
echo          ARCHIPRO UZ - CLIENT RELEASE BUILD
echo ============================================================
echo.

REM ============================================================
REM PYTHON
REM ============================================================

where python >nul 2>&1

if errorlevel 1 (
    echo [ERROR] Python topilmadi.
    pause
    exit /b 1
)

echo [OK] Python topildi.
python --version
echo.

REM ============================================================
REM REQUIRED PACKAGES
REM ============================================================

python -c "import PySide6" >nul 2>&1

if errorlevel 1 (
    echo [INFO] PySide6 o'rnatilmoqda...
    python -m pip install PySide6

    if errorlevel 1 (
        echo [ERROR] PySide6 o'rnatilmadi.
        pause
        exit /b 1
    )
)

python -c "import cryptography" >nul 2>&1

if errorlevel 1 (
    echo [INFO] cryptography o'rnatilmoqda...
    python -m pip install cryptography

    if errorlevel 1 (
        echo [ERROR] cryptography o'rnatilmadi.
        pause
        exit /b 1
    )
)

python -c "import PyInstaller" >nul 2>&1

if errorlevel 1 (
    echo [INFO] PyInstaller o'rnatilmoqda...
    python -m pip install --upgrade pyinstaller

    if errorlevel 1 (
        echo [ERROR] PyInstaller o'rnatilmadi.
        pause
        exit /b 1
    )
)

echo [OK] Kerakli paketlar tayyor.
echo.

REM ============================================================
REM PROJECT CHECK
REM ============================================================

if not exist "app\main.py" (
    echo [ERROR] app\main.py topilmadi.
    pause
    exit /b 1
)

echo [OK] app\main.py topildi.
echo.

REM ============================================================
REM CLEAN
REM ============================================================

if exist "build_client" (
    rmdir /s /q "build_client"
)

if exist "dist_client" (
    rmdir /s /q "dist_client"
)

if exist "release" (
    rmdir /s /q "release"
)

if exist "ARCHIPRO_UZ_CLIENT.spec" (
    del /q "ARCHIPRO_UZ_CLIENT.spec"
)

mkdir "release"
mkdir "release\ARCHIPRO_UZ_CLIENT"

echo [OK] Eski CLIENT build tozalandi.
echo.

REM ============================================================
REM BUILD CLIENT
REM ============================================================

echo ============================================================
echo              ARCHIPRO UZ.exe YARATILMOQDA
echo ============================================================
echo.

python -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --name "ARCHIPRO UZ" ^
    --paths "app" ^
    --workpath "build_client" ^
    --distpath "dist_client" ^
    --specpath "." ^
    --collect-all PySide6 ^
    "app\main.py"

if errorlevel 1 (
    echo.
    echo [ERROR] CLIENT BUILD FAILED
    pause
    exit /b 1
)

if not exist "dist_client\ARCHIPRO UZ.exe" (
    echo.
    echo [ERROR] ARCHIPRO UZ.exe topilmadi.
    pause
    exit /b 1
)

copy /Y ^
    "dist_client\ARCHIPRO UZ.exe" ^
    "release\ARCHIPRO_UZ_CLIENT\ARCHIPRO UZ.exe" ^
    >nul

REM ============================================================
REM SECURITY CHECK
REM ============================================================

if exist "release\ARCHIPRO_UZ_CLIENT\ARCHIPRO ADMIN.exe" (
    echo [ERROR] ADMIN fayli CLIENT paketiga tushib qolgan.
    pause
    exit /b 1
)

if exist "release\ARCHIPRO_UZ_CLIENT\archipro_private.key" (
    echo [ERROR] PRIVATE KEY CLIENT paketiga tushib qolgan.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo                    RELEASE TAYYOR
echo ============================================================
echo.
echo [PASS] CLIENT EXE:
echo release\ARCHIPRO_UZ_CLIENT\ARCHIPRO UZ.exe
echo.
echo CLIENT paketida:
echo   - ARCHIPRO ADMIN.exe YO'Q
echo   - private key YO'Q
echo.
echo Mijozga faqat:
echo release\ARCHIPRO_UZ_CLIENT
echo papkasidagi fayl beriladi.
echo.
echo ============================================================

pause
exit /b 0
