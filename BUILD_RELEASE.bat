@echo off
setlocal EnableExtensions EnableDelayedExpansion

title ARCHIPRO UZ - RELEASE BUILD

cd /d "%~dp0"

echo.
echo ============================================================
echo              ARCHIPRO UZ - RELEASE BUILD
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
REM VERSION
REM ============================================================

set "APP_VERSION="

for /f "delims=" %%V in ('python -c "import sys; sys.path.insert(0, r'app'); import version; print(version.APP_VERSION)"') do (
    set "APP_VERSION=%%V"
)

if not defined APP_VERSION (
    echo [ERROR] app\version.py dan versiya olinmadi.
    pause
    exit /b 1
)

echo [OK] ARCHIPRO UZ v%APP_VERSION%
echo.

REM ============================================================
REM ICON
REM ============================================================

if not exist "archipro.ico" (
    echo [ERROR] archipro.ico topilmadi.
    echo.
    echo Fayl repository root papkasida bo'lishi kerak.
    pause
    exit /b 1
)

echo [OK] archipro.ico topildi.
echo.

REM ============================================================
REM PACKAGES
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

echo [OK] Build paketlari tayyor.
echo.

REM ============================================================
REM PROJECT CHECK
REM ============================================================

if not exist "app\main.py" (
    echo [ERROR] app\main.py topilmadi.
    pause
    exit /b 1
)

if not exist "ARCHIPRO_UZ.iss" (
    echo [ERROR] ARCHIPRO_UZ.iss topilmadi.
    pause
    exit /b 1
)

echo [OK] Project fayllari tayyor.
echo.

REM ============================================================
REM RELEASE PREFLIGHT
REM ============================================================

echo ============================================================
echo              RELEASE PREFLIGHT TEKSHIRUVI
echo ============================================================
echo.

python "app\tools\content_guard.py"

if errorlevel 1 (
    echo.
    echo [ERROR] CONTENT GUARD FAILED
    pause
    exit /b 1
)

python "app\tools\project_audit.py"

if errorlevel 1 (
    echo.
    echo [ERROR] PROJECT AUDIT FAILED
    pause
    exit /b 1
)

python "app\tools\database_audit.py"

if errorlevel 1 (
    echo.
    echo [ERROR] DATABASE AUDIT FAILED
    pause
    exit /b 1
)

python "app\tools\runtime_smoke_test.py"

if errorlevel 1 (
    echo.
    echo [ERROR] RUNTIME SMOKE TEST FAILED
    pause
    exit /b 1
)

python "app\tools\customer_features_smoke_test.py"

if errorlevel 1 (
    echo.
    echo [ERROR] CUSTOMER FEATURES SMOKE TEST FAILED
    pause
    exit /b 1
)

echo.
echo [PASS] Release preflight muvaffaqiyatli.
echo.

REM ============================================================
REM CLEAN OLD CLIENT BUILD
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
mkdir "release\installer"

echo [OK] Eski release tozalandi.
echo.

REM ============================================================
REM BUILD CLIENT EXE
REM ============================================================

echo ============================================================
echo          ARCHIPRO UZ.exe YARATILMOQDA
echo ============================================================
echo.

python -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --name "ARCHIPRO UZ" ^
    --icon "archipro.ico" ^
    --paths "app" ^
    --workpath "build_client" ^
    --distpath "dist_client" ^
    --specpath "." ^
    --collect-all PySide6 ^
    --collect-submodules courses ^
    --collect-submodules licensing ^
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

echo [OK] ARCHIPRO UZ.exe tayyor.
echo.

REM ============================================================
REM SECURITY CHECK
REM ============================================================

if exist "release\ARCHIPRO_UZ_CLIENT\ARCHIPRO ADMIN.exe" (
    echo [ERROR] ADMIN.exe CLIENT paketiga tushib qolgan.
    pause
    exit /b 1
)

if exist "release\ARCHIPRO_UZ_CLIENT\ARCHIPRO OWNER.exe" (
    echo [ERROR] OWNER.exe CLIENT paketiga tushib qolgan.
    pause
    exit /b 1
)

if exist "release\ARCHIPRO_UZ_CLIENT\archipro_private.key" (
    echo [ERROR] PRIVATE KEY CLIENT paketiga tushib qolgan.
    pause
    exit /b 1
)

dir /b "release\ARCHIPRO_UZ_CLIENT\*.archiprolic" >nul 2>&1
if not errorlevel 1 (
    echo [ERROR] LICENSE fayli CLIENT paketiga tushib qolgan.
    pause
    exit /b 1
)

dir /b "release\ARCHIPRO_UZ_CLIENT\*.archiprobackup" >nul 2>&1
if not errorlevel 1 (
    echo [ERROR] BACKUP fayli CLIENT paketiga tushib qolgan.
    pause
    exit /b 1
)

echo [OK] CLIENT security check PASS.
echo.

REM ============================================================
REM FIND INNO SETUP
REM ============================================================

set "ISCC="

where ISCC.exe >nul 2>&1

if not errorlevel 1 (
    for /f "delims=" %%I in ('where ISCC.exe') do (
        if not defined ISCC set "ISCC=%%I"
    )
)

if not defined ISCC (
    if exist "%ProgramFiles(x86)%\Inno Setup 6\ISCC.exe" (
        set "ISCC=%ProgramFiles(x86)%\Inno Setup 6\ISCC.exe"
    )
)

if not defined ISCC (
    if exist "%ProgramFiles%\Inno Setup 6\ISCC.exe" (
        set "ISCC=%ProgramFiles%\Inno Setup 6\ISCC.exe"
    )
)

REM ============================================================
REM INSTALLER
REM ============================================================

if not defined ISCC (
    echo ============================================================
    echo CLIENT EXE TAYYOR
    echo ============================================================
    echo.
    echo [PASS] release\ARCHIPRO_UZ_CLIENT\ARCHIPRO UZ.exe
    echo.
    echo [INFO] Inno Setup topilmadi.
    echo Installer yaratish uchun Inno Setup o'rnatilishi kerak.
    echo.
    echo Inno Setup o'rnatilgach BUILD_RELEASE.bat ni
    echo yana ishga tushiring.
    echo.
    pause
    exit /b 0
)

echo ============================================================
echo        ARCHIPRO UZ INSTALLER YARATILMOQDA
echo ============================================================
echo.

echo Inno Setup:
echo %ISCC%
echo.

"%ISCC%" ^
    /DMyAppVersion=%APP_VERSION% ^
    "ARCHIPRO_UZ.iss"

if errorlevel 1 (
    echo.
    echo [ERROR] INSTALLER BUILD FAILED
    pause
    exit /b 1
)

REM ============================================================
REM FINAL CHECK
REM ============================================================

set "INSTALLER_FILE=release\installer\ARCHIPRO UZ Setup v%APP_VERSION%.exe"

if not exist "%INSTALLER_FILE%" (
    echo.
    echo [ERROR] Installer fayli topilmadi:
    echo %INSTALLER_FILE%
    pause
    exit /b 1
)

echo.
echo ============================================================
echo               RELEASE MUVAFFAQIYATLI
echo ============================================================
echo.
echo ARCHIPRO UZ VERSION:
echo v%APP_VERSION%
echo.
echo CLIENT EXE:
echo release\ARCHIPRO_UZ_CLIENT\ARCHIPRO UZ.exe
echo.
echo MIJOZGA BERILADIGAN INSTALLER:
echo %INSTALLER_FILE%
echo.
echo CLIENT paketida:
echo   - ARCHIPRO ADMIN.exe YO'Q
echo   - private key YO'Q
echo.
echo ============================================================

pause
exit /b 0
