@echo off
setlocal

title ARCHIPRO UZ - FULL SYSTEM AUDIT

echo.
echo ============================================================
echo              ARCHIPRO UZ - FULL SYSTEM AUDIT
echo ============================================================
echo.

cd /d "%~dp0"

set PYTHON_CMD=

where python >nul 2>nul
if %errorlevel%==0 (
    set PYTHON_CMD=python
)

if not defined PYTHON_CMD (
    where py >nul 2>nul
    if %errorlevel%==0 (
        set PYTHON_CMD=py
    )
)

if not defined PYTHON_CMD (
    echo [ERROR] Python topilmadi.
    echo.
    echo Python o'rnatilgan bo'lsa ham PATH ga ulanmagan bo'lishi mumkin.
    echo.
    pause
    exit /b 1
)

echo [OK] Python topildi: %PYTHON_CMD%
echo.

if not exist "app\tools\project_audit.py" (
    echo [ERROR] app\tools\project_audit.py topilmadi.
    echo.
    pause
    exit /b 1
)

if not exist "app\tools\database_audit.py" (
    echo [ERROR] app\tools\database_audit.py topilmadi.
    echo.
    pause
    exit /b 1
)

if not exist "app\tools\runtime_smoke_test.py" (
    echo [ERROR] app\tools\runtime_smoke_test.py topilmadi.
    echo.
    pause
    exit /b 1
)

echo ============================================================
echo 1 / 3 - PROJECT AUDIT
echo ============================================================
echo.

%PYTHON_CMD% "app\tools\project_audit.py"

set PROJECT_RESULT=%errorlevel%

echo.
echo.
echo ============================================================
echo 2 / 3 - DATABASE AUDIT
echo ============================================================
echo.

%PYTHON_CMD% "app\tools\database_audit.py"

set DATABASE_RESULT=%errorlevel%

echo.
echo.
echo ============================================================
echo 3 / 3 - RUNTIME SMOKE TEST
echo ============================================================
echo.

%PYTHON_CMD% "app\tools\runtime_smoke_test.py"

set RUNTIME_RESULT=%errorlevel%

echo.
echo.
echo ============================================================
echo                   FINAL AUDIT RESULT
echo ============================================================
echo.

echo Project audit exit code : %PROJECT_RESULT%
echo Database audit exit code: %DATABASE_RESULT%
echo Runtime test exit code  : %RUNTIME_RESULT%
echo.

if "%PROJECT_RESULT%"=="0" (
    echo [PASS] PROJECT AUDIT
) else (
    echo [FAIL] PROJECT AUDIT
)

if "%DATABASE_RESULT%"=="0" (
    echo [PASS] DATABASE AUDIT
) else (
    echo [FAIL] DATABASE AUDIT
)

if "%RUNTIME_RESULT%"=="0" (
    echo [PASS] RUNTIME SMOKE TEST
) else (
    echo [FAIL] RUNTIME SMOKE TEST
)

echo.

if "%PROJECT_RESULT%"=="0" if "%DATABASE_RESULT%"=="0" if "%RUNTIME_RESULT%"=="0" (
    echo ============================================================
    echo ARCHIPRO UZ FULL AUDIT MUVAFFAQIYATLI YAKUNLANDI
    echo KRITIK XATO TOPILMADI
    echo ============================================================
    echo.
    pause
    exit /b 0
)

echo ============================================================
echo ARCHIPRO UZ FULL AUDIT XATOLAR BILAN YAKUNLANDI
echo YUQORIDAGI ERROR VA WARNING QATORLARINI TEKSHIRING
echo ============================================================
echo.

pause
exit /b 1
