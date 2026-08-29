@echo off
REM Launch Cursor with GPU disabled — workaround for notebook scroll freezes on Windows.
REM Close all Cursor windows first, then double-click this file or run it from a terminal.

set CURSOR_EXE=%LOCALAPPDATA%\Programs\cursor\Cursor.exe
if not exist "%CURSOR_EXE%" (
  echo Cursor.exe not found at "%CURSOR_EXE%"
  exit /b 1
)

start "" "%CURSOR_EXE%" --disable-gpu "%~dp0"
echo Started Cursor with --disable-gpu for this workspace.
