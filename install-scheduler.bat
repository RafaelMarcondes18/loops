@echo off
chcp 65001 >nul
:: Registra todos os loops no Windows Task Scheduler
:: Execute como Administrador uma unica vez

setlocal
set "LOOPS_DIR=%~dp0"
set "PYTHON=py -3"

echo Registrando loops no Task Scheduler...
echo.

:: AJI — Pipeline matinal (Seg-Sex 7:17)
schtasks /create /tn "Loops\AJI - Morning Pipeline" ^
  /tr "\"%LOOPS_DIR%run-loop.bat\" aji\morning-pipeline.loop.md" ^
  /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 07:17 ^
  /ru "%USERNAME%" /f
echo [OK] AJI Morning Pipeline

:: AJI — Dual check (Seg-Sex 11:23)
schtasks /create /tn "Loops\AJI - Dual Check" ^
  /tr "\"%LOOPS_DIR%run-loop.bat\" aji\dual-check.loop.md" ^
  /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 11:23 ^
  /ru "%USERNAME%" /f
echo [OK] AJI Dual Check

:: AJI — CPJ Sync (Seg-Sex 8:45)
schtasks /create /tn "Loops\AJI - CPJ Sync" ^
  /tr "\"%LOOPS_DIR%run-loop.bat\" aji\cpj-sync.loop.md" ^
  /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 08:45 ^
  /ru "%USERNAME%" /f
echo [OK] AJI CPJ Sync

:: AM — Relatorio semanal (Segundas 9:21)
schtasks /create /tn "Loops\AM - Weekly Report" ^
  /tr "\"%LOOPS_DIR%run-loop.bat\" am\weekly-report.loop.md" ^
  /sc WEEKLY /d MON /st 09:21 ^
  /ru "%USERNAME%" /f
echo [OK] AM Weekly Report

:: AM — PROJUDI Monitor (Seg-Sex 10:43)
schtasks /create /tn "Loops\AM - PROJUDI Monitor" ^
  /tr "\"%LOOPS_DIR%run-loop.bat\" am\projudi-monitor.loop.md" ^
  /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 10:43 ^
  /ru "%USERNAME%" /f
echo [OK] AM PROJUDI Monitor

:: Iudex — Deploy Health (Seg-Sex 8:37)
schtasks /create /tn "Loops\Iudex - Deploy Health" ^
  /tr "\"%LOOPS_DIR%run-loop.bat\" iudex\deploy-health.loop.md" ^
  /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 08:37 ^
  /ru "%USERNAME%" /f
echo [OK] Iudex Deploy Health

:: Seguranca — Security Review (Sextas 14:51)
schtasks /create /tn "Loops\Seguranca - Security Review" ^
  /tr "\"%LOOPS_DIR%run-loop.bat\" seguranca\security-review.loop.md" ^
  /sc WEEKLY /d FRI /st 14:51 ^
  /ru "%USERNAME%" /f
echo [OK] Security Review

:: n8n — Health Check (Quartas 9:11)
schtasks /create /tn "Loops\n8n - Health Check" ^
  /tr "\"%LOOPS_DIR%run-loop.bat\" n8n\health-check.loop.md" ^
  /sc WEEKLY /d WED /st 09:11 ^
  /ru "%USERNAME%" /f
echo [OK] n8n Health Check

:: AM — Lead Follow-up (Seg-Sex 8:00 — verifica CRM e gera follow-ups)
schtasks /create /tn "Loops\AM - Lead Follow-up" ^
  /tr "\"%LOOPS_DIR%run-loop.bat\" am\lead-followup.loop.md" ^
  /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 08:00 ^
  /ru "%USERNAME%" /f
echo [OK] AM Lead Follow-up

:: AM — Lead Generation (Segundas 9:00 — gera 15 leads da semana)
schtasks /create /tn "Loops\AM - Lead Generation" ^
  /tr "\"%LOOPS_DIR%run-loop.bat\" am\lead-generation.loop.md" ^
  /sc WEEKLY /d MON /st 09:00 ^
  /ru "%USERNAME%" /f
echo [OK] AM Lead Generation

echo.
echo Todos os loops registrados. Verifique em: Agendador de Tarefas ^> Loops
pause
