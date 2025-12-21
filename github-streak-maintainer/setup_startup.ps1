# PowerShell script to set up Windows Startup for GitHub Streak Maintainer
# This will run the script automatically when Windows starts
# Run this script as Administrator

$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Split-Path -Parent $scriptPath
$vbsScript = Join-Path $scriptPath "startup_streak.vbs"
$startupFolder = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"
$startupShortcut = Join-Path $startupFolder "GitHub Streak Maintainer.lnk"

Write-Host "Setting up Windows Startup for GitHub Streak Maintainer..." -ForegroundColor Green
Write-Host "Script path: $scriptPath" -ForegroundColor Yellow
Write-Host "Repository root: $repoRoot" -ForegroundColor Yellow
Write-Host "Startup folder: $startupFolder" -ForegroundColor Yellow

# Create shortcut in startup folder
try {
    $WshShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut($startupShortcut)
    $Shortcut.TargetPath = "wscript.exe"
    $Shortcut.Arguments = "`"$vbsScript`""
    $Shortcut.WorkingDirectory = $repoRoot
    $Shortcut.Description = "Automatically maintains GitHub contribution streak"
    $Shortcut.Save()
    
    Write-Host "`n[SUCCESS] Startup shortcut created successfully!" -ForegroundColor Green
    Write-Host "The script will run automatically when Windows starts." -ForegroundColor Cyan
    Write-Host "`nShortcut location: $startupShortcut" -ForegroundColor Yellow
    Write-Host "`nTo disable: Delete the shortcut from Startup folder" -ForegroundColor Yellow
    Write-Host "Or run: Remove-Item `"$startupShortcut`"" -ForegroundColor Yellow
    
    # Test run
    $testRun = Read-Host "`nDo you want to test run the script now? (Y/N)"
    if ($testRun -eq "Y" -or $testRun -eq "y") {
        Write-Host "`nRunning test..." -ForegroundColor Cyan
        & wscript.exe "$vbsScript"
        Write-Host "Test completed. Check if it worked correctly." -ForegroundColor Green
    }
} catch {
    Write-Host "`n[ERROR] Error creating startup shortcut: $_" -ForegroundColor Red
    Write-Host "Make sure you have write permissions to the Startup folder." -ForegroundColor Yellow
}

