# PowerShell script to set up Windows Task Scheduler for GitHub Streak Maintainer
# Run this script as Administrator

$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Split-Path -Parent $scriptPath  # Go up one level to repository root
$pythonPath = (Get-Command python).Source
$scheduleScript = Join-Path $scriptPath "schedule_streak.py"

Write-Host "Setting up Windows Task Scheduler for GitHub Streak Maintainer..." -ForegroundColor Green
Write-Host "Script path: $scriptPath" -ForegroundColor Yellow
Write-Host "Repository root: $repoRoot" -ForegroundColor Yellow
Write-Host "Python path: $pythonPath" -ForegroundColor Yellow

# Prompt for schedule time
$timeInput = Read-Host "Enter time to run daily (HH:MM format, e.g., 18:00 for 6 PM)"
try {
    $time = [DateTime]::ParseExact($timeInput, "HH:mm", $null)
} catch {
    Write-Host "Invalid time format. Using default: 18:00" -ForegroundColor Yellow
    $time = [DateTime]::ParseExact("18:00", "HH:mm", $null)
}

# Create scheduled task action
$action = New-ScheduledTaskAction -Execute $pythonPath -Argument "`"$scheduleScript`"" -WorkingDirectory $repoRoot

# Create trigger (daily at specified time)
$trigger = New-ScheduledTaskTrigger -Daily -At $time

# Create task settings
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

# Register the task
try {
    Register-ScheduledTask -TaskName "GitHub Streak Maintainer" `
        -Action $action `
        -Trigger $trigger `
        -Settings $settings `
        -Description "Automatically maintains GitHub contribution streak by pushing commits if no commits were made in the last 24 hours" `
        -Force
    
    Write-Host "`n✅ Task scheduled successfully!" -ForegroundColor Green
    Write-Host "Task will run daily at $($time.ToString('HH:mm'))" -ForegroundColor Cyan
    Write-Host "`nTo view the task: Task Scheduler → Task Scheduler Library → GitHub Streak Maintainer" -ForegroundColor Yellow
    Write-Host "To test: Right-click the task → Run" -ForegroundColor Yellow
} catch {
    Write-Host "`n❌ Error creating task: $_" -ForegroundColor Red
    Write-Host "Make sure you're running PowerShell as Administrator" -ForegroundColor Yellow
}

