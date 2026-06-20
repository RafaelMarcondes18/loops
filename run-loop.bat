@echo off
chcp 65001 >nul
:: Universal Loop Runner — wrapper para Task Scheduler
:: Uso: run-loop.bat <arquivo.loop.md> [--provider X] [--model Y]
::
:: Exemplos:
::   run-loop.bat aji\morning-pipeline.loop.md
::   run-loop.bat am\weekly-report.loop.md --provider openai

setlocal
set "LOOPS_DIR=%~dp0"
set "LOOP_FILE=%~1"
shift

if "%LOOP_FILE%"=="" (
    echo ERRO: especifique o arquivo .loop.md
    echo Uso: run-loop.bat ^<arquivo.loop.md^> [opcoes]
    exit /b 1
)

py -3 "%LOOPS_DIR%runner.py" "%LOOPS_DIR%%LOOP_FILE%" %*
