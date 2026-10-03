@echo off
title ARCHIPRO UZ - PROJECT AUDIT

echo.
echo ============================================================
echo                ARCHIPRO UZ - PROJECT AUDIT
echo ============================================================
echo.

cd /d "%~dp0"

if not exist "app\tools\project_audit.py" (
    echo [ERROR] app\tools\project_audit.py topilmadi.
    echo.
    echo Avval 213-bosqichdagi audit faylini yarating.
    echo.
    pause
    exit /b 1
)

echo Python tekshirilmoqda...
echo.

where python >nul 2>nul

if %errorlevel%==0 (
    echo [OK] python topildi.
    echo.
    python "app\tools\project_audit.py"

    set AUDIT_RESULT=%errorlevel%

    echo.
    echo ============================================================
    echo.

    if "%AUDIT_RESULT%"=="0" (
        echo AUDIT MUVAFFAQIYATLI YAKUNLANDI.
        echo Kritik xato topilmadi.
    ) else (
        echo AUDIT XATOLAR BILAN YAKUNLANDI.
        echo Yuqoridagi ERROR qatorlarini tekshiring.
    )

    echo.
    pause
    exit /b %AUDIT_RESULT%
)

where py >nul 2>nul

if %errorlevel%==0 (
    echo [OK] Python launcher topildi.
    echo.
    py "app\tools\project_audit.py"

    set AUDIT_RESULT=%errorlevel%

    echo.
    echo ============================================================
    echo.

    if "%AUDIT_RESULT%"=="0" (
        echo AUDIT MUVAFFAQIYATLI YAKUNLANDI.
        echo Kritik xato topilmadi.
    ) else (
        echo AUDIT XATOLAR BILAN YAKUNLANDI.
        echo Yuqoridagi ERROR qatorlarini tekshiring.
    )

    echo.
    pause
    exit /b %AUDIT_RESULT%
)

echo.
echo [ERROR] Python topilmadi.
echo.
echo Python o'rnatilgan bo'lsa ham PATH ga ulanmagan bo'lishi mumkin.
echo.
echo Windows Start menyudan:
echo Python
echo yoki
echo IDLE
echo deb qidirib tekshiring.
echo.

pause
exit /b 1
