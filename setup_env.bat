@echo off

:: Get the directory of the script
set "DIR=%~dp0"

:: Add the project's root directory to the Python path
set "PYTHONPATH=%DIR%;%PYTHONPATH%"

:: Display the updated Python path (optional)
echo PYTHONPATH is now set to: %PYTHONPATH%