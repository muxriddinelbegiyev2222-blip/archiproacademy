@echo off
setlocal EnableExtensions
cd /d "%~dp0"
title ARCHIPRO UZ - CLIENT EXE ONLY

echo.
echo =============================================================
echo     ARCHIPRO UZ - MAIN LEARNING APPLICATION BUILD
echo =============================================================
echo This builds the 680-lesson customer application, NOT ADMIN or OWNER.
echo.

if not exist "app\tools\build_client.py" goto source_missing
if not exist "app\main.py" goto source_missing
if not exist "app\tools\verify_built_exe.py" goto source_missing
if not exist "archipro.ico" goto icon_missing

where python >nul 2>&1
if errorlevel 1 goto python_missing

python -c "import PySide6, cryptography, PyInstaller" >nul 2>&1
if errorlevel 1 (
  echo [INFO] Installing required Python packages...
  python -m pip install -r requirements.txt pyinstaller
  if errorlevel 1 goto dependencies_failed
)

echo.
echo [1/4] Verify lesson and quiz totals...
python "app\tools\content_guard.py"
if errorlevel 1 goto content_failed

echo.
echo [2/4] Run the complete release audit...
python "app\tools\full_audit.py"
if errorlevel 1 goto audit_failed

echo.
echo [3/4] Build ARCHIPRO UZ.exe (the full 680-lesson application)...
python "app\tools\build_client.py" --workpath "build_client" --distpath "dist_client" --specpath "."
if errorlevel 1 goto package_failed
if not exist "dist_client\ARCHIPRO UZ.exe" goto exe_missing

echo.
echo [4/4] Verify the actual Windows executable and all 680 lessons...
python "app\tools\verify_built_exe.py" "dist_client\ARCHIPRO UZ.exe"
if errorlevel 1 goto verify_failed

echo.
echo =============================================================
echo [PASS] ARCHIPRO UZ CUSTOMER APPLICATION IS READY
echo dist_client\ARCHIPRO UZ.exe
echo =============================================================
echo Do not deliver the program before testing activation on Windows.
echo ADMIN.exe, OWNER.exe, and the private key are NOT included.
echo.
pause
exit /b 0

:source_missing
echo [ERROR] Application source or build scripts are missing.
goto failed
:icon_missing
echo [ERROR] archipro.ico is missing from the project root.
goto failed
:python_missing
echo [ERROR] Python is missing from PATH.
goto failed
:dependencies_failed
echo [ERROR] Required Python dependencies could not be installed.
goto failed
:content_failed
echo [ERROR] Lesson content check failed. Client EXE was NOT built.
goto failed
:audit_failed
echo [ERROR] Release audit failed. See the latest audit_logs folder.
goto failed
:package_failed
echo [ERROR] PyInstaller build failed. Check the last error above.
echo A .pkg file in build_client is an intermediate file, NOT the final EXE.
goto failed
:exe_missing
echo [ERROR] PyInstaller returned without dist_client\ARCHIPRO UZ.exe.
goto failed
:verify_failed
echo [ERROR] EXE was built but its embedded lessons failed verification.
goto failed
:failed
echo.
echo Build was NOT successful. Please capture the last 20 error lines.
echo.
pause
exit /b 1
