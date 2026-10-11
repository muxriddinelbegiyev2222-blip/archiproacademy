@echo off
setlocal EnableExtensions
cd /d "%~dp0"
title ARCHIPRO UZ - BUILD ALL THREE WINDOWS APPLICATIONS

echo.
echo =============================================================
echo   BUILD ALL: CUSTOMER APPLICATION, ADMIN, AND OWNER
echo =============================================================
echo This script builds each program separately.
echo No private signing key is ever included in the customer EXE.
echo.

if not exist "BUILD_CLIENT_ONLY.bat" goto missing_script
if not exist "BUILD_ADMIN_ONLY.bat" goto missing_script
if not exist "BUILD_OWNER_ONLY.bat" goto missing_script

echo.
echo [1/3] BUILD CUSTOMER - FULL 680 LESSON APPLICATION
call "BUILD_CLIENT_ONLY.bat"
if errorlevel 1 goto failed_client
if not exist "dist_client\ARCHIPRO UZ.exe" goto failed_client

echo.
echo [2/3] BUILD ADMIN - PRO CUSTOMER LICENSE GENERATOR
call "BUILD_ADMIN_ONLY.bat"
if errorlevel 1 goto failed_admin
if not exist "dist_admin\ARCHIPRO ADMIN.exe" goto failed_admin

echo.
echo [3/3] BUILD OWNER - PERSONAL MASTER LICENSE GENERATOR
call "BUILD_OWNER_ONLY.bat"
if errorlevel 1 goto failed_owner
if not exist "dist_owner\ARCHIPRO OWNER.exe" goto failed_owner

echo.
echo =============================================================
echo [PASS] ALL THREE EXECUTABLES WERE BUILT
echo.
echo 1. dist_client\ARCHIPRO UZ.exe   - Customer learning app
echo 2. dist_admin\ARCHIPRO ADMIN.exe - Your PRO license generator
echo 3. dist_owner\ARCHIPRO OWNER.exe - Your MASTER generator
echo =============================================================
echo WARNING: Never give ADMIN.exe, OWNER.exe, or private key to buyers.
echo The customer EXE should be tested with a valid customer license.
echo.
pause
exit /b 0

:missing_script
echo [ERROR] One or more build scripts are missing.
goto failed
:failed_client
echo [ERROR] CLIENT BUILD FAILED. No complete three-app release.
goto failed
:failed_admin
echo [ERROR] ADMIN BUILD FAILED. Customer EXE may already be ready.
goto failed
:failed_owner
echo [ERROR] OWNER BUILD FAILED. Earlier EXEs may already be ready.
goto failed
:failed
echo.
echo Capture the error output above; do not use intermediate .pkg files.
echo.
pause
exit /b 1
