@echo off
REM Launch Cursor with extensions disabled — use only to test if an extension blocks scrolling.
REM Close all Cursor windows first.

set CURSOR_EXE=%LOCALAPPDATA%\Programs\cursor\Cursor.exe
if not exist "%CURSOR_EXE%" (
  echo Cursor.exe not found at "%CURSOR_EXE%"
  exit /b 1
)

start "" "%CURSOR_EXE%" --disable-extensions --disable-gpu "%~dp0"
echo Started Cursor with --disable-extensions and --disable-gpu.
