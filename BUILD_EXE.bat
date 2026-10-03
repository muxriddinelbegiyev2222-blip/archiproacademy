@echo off
setlocal EnableExtensions EnableDelayedExpansion

title ARCHIPRO UZ - EXE BUILD

cd /d "%~dp0"

echo.
echo ============================================================
echo              ARCHIPRO UZ - EXE BUILD SYSTEM
echo ============================================================
echo.

REM ============================================================
REM PYTHON CHECK
REM ============================================================

where python >nul 2>&1

if errorlevel 1 (
    echo [ERROR] Python topilmadi.
    echo.
    echo Python o'rnatilganini tekshiring.
    pause
    exit /b 1
)

echo [OK] Python topildi.

python --version

echo.

REM ============================================================
REM PIP CHECK
REM ============================================================

python -m pip --version >nul 2>&1

if errorlevel 1 (
    echo [ERROR] pip topilmadi.
    pause
    exit /b 1
)

echo [OK] pip ishlayapti.

echo.

REM ============================================================
REM PYSIDE6 CHECK
REM ============================================================

python -c "import PySide6" >nul 2>&1

if errorlevel 1 (
    echo [INFO] PySide6 topilmadi.
    echo [INFO] PySide6 o'rnatilmoqda...
    echo.

    python -m pip install PySide6

    if errorlevel 1 (
        echo.
        echo [ERROR] PySide6 o'rnatilmadi.
        pause
        exit /b 1
    )
)

echo [OK] PySide6 tayyor.

echo.

REM ============================================================
REM PYINSTALLER CHECK
REM ============================================================

python -c "import PyInstaller" >nul 2>&1

if errorlevel 1 (
    echo [INFO] PyInstaller topilmadi.
    echo [INFO] PyInstaller o'rnatilmoqda...
    echo.

    python -m pip install --upgrade pyinstaller

    if errorlevel 1 (
        echo.
        echo [ERROR] PyInstaller o'rnatilmadi.
        pause
        exit /b 1
    )
)

echo [OK] PyInstaller tayyor.

echo.

REM ============================================================
REM PROJECT CHECK
REM ============================================================

if not exist "app\main.py" (
    echo [ERROR] app\main.py topilmadi.
    pause
    exit /b 1
)

if not exist "app\admin.py" (
    echo [ERROR] app\admin.py topilmadi.
    pause
    exit /b 1
)

echo [OK] main.py topildi.
echo [OK] admin.py topildi.

echo.

REM ============================================================
REM CLEAN OLD BUILD
REM ============================================================

echo Eski build fayllari tozalanmoqda...

if exist "build" (
    rmdir /s /q "build"
)

if exist "dist" (
    rmdir /s /q "dist"
)

if exist "ARCHIPRO_UZ.spec" (
    del /q "ARCHIPRO_UZ.spec"
)

if exist "ARCHIPRO_ADMIN.spec" (
    del /q "ARCHIPRO_ADMIN.spec"
)

echo [OK] Eski build tozalandi.

echo.

REM ============================================================
REM BUILD MAIN APP
REM ============================================================

echo ============================================================
echo 1 / 2 - ARCHIPRO UZ.exe YARATILMOQDA
echo ============================================================
echo.

python -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --name "ARCHIPRO UZ" ^
    --paths "app" ^
    --collect-all PySide6 ^
    "app\main.py"

if errorlevel 1 (
    echo.
    echo ============================================================
    echo [ERROR] ARCHIPRO UZ.exe BUILD FAILED
    echo ============================================================
    echo.
    pause
    exit /b 1
)

echo.
echo [OK] ARCHIPRO UZ.exe yaratildi.

echo.

REM ============================================================
REM BUILD ADMIN APP
REM ============================================================

echo ============================================================
echo 2 / 2 - ARCHIPRO ADMIN.exe YARATILMOQDA
echo ============================================================
echo.

python -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --name "ARCHIPRO ADMIN" ^
    --paths "app" ^
    --collect-all PySide6 ^
    "app\admin.py"

if errorlevel 1 (
    echo.
    echo ============================================================
    echo [ERROR] ARCHIPRO ADMIN.exe BUILD FAILED
    echo ============================================================
    echo.
    pause
    exit /b 1
)

echo.
echo [OK] ARCHIPRO ADMIN.exe yaratildi.

echo.

REM ============================================================
REM RESULT CHECK
REM ============================================================

set MAIN_OK=0
set ADMIN_OK=0

if exist "dist\ARCHIPRO UZ.exe" (
    set MAIN_OK=1
)

if exist "dist\ARCHIPRO ADMIN.exe" (
    set ADMIN_OK=1
)

echo ============================================================
echo                     BUILD RESULT
echo ============================================================
echo.

if "!MAIN_OK!"=="1" (
    echo [PASS] dist\ARCHIPRO UZ.exe
) else (
    echo [FAIL] dist\ARCHIPRO UZ.exe
)

if "!ADMIN_OK!"=="1" (
    echo [PASS] dist\ARCHIPRO ADMIN.exe
) else (
    echo [FAIL] dist\ARCHIPRO ADMIN.exe
)

echo.

if "!MAIN_OK!"=="1" if "!ADMIN_OK!"=="1" (
    echo ============================================================
    echo ARCHIPRO UZ BUILD MUVAFFAQIYATLI YAKUNLANDI
    echo ============================================================
    echo.
    echo Tayyor EXE fayllar:
    echo.
    echo dist\ARCHIPRO UZ.exe
    echo dist\ARCHIPRO ADMIN.exe
    echo.
    echo MUHIM:
    echo ARCHIPRO ADMIN.exe mijozga berilmaydi.
    echo Bu faqat dastur egasi/test uchun.
    echo.
    pause
    exit /b 0
)

echo ============================================================
echo ARCHIPRO UZ BUILD XATO BILAN YAKUNLANDI
echo ============================================================
echo.

pause
exit /b 1
