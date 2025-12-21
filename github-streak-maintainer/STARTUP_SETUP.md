# Startup Setup Guide - Auto-Run on Boot

This guide will help you set up the GitHub Streak Maintainer to run automatically when your laptop starts.

## 🚀 Quick Setup (Recommended)

### Method 1: Automatic Setup Script (Easiest)

1. **Right-click** `setup_startup.ps1` → **Run with PowerShell**
2. If prompted, allow script execution
3. Follow the prompts
4. Done! ✅

The script will:
- Create a startup shortcut
- Run automatically when Windows starts
- Check and push to GitHub if needed

### Method 2: Manual Setup

1. Press `Win + R` to open Run dialog
2. Type: `shell:startup` and press Enter
3. This opens your Startup folder
4. Create a shortcut:
   - Right-click in the folder → New → Shortcut
   - Target: `wscript.exe "C:\Users\bhave\OneDrive\Desktop\AIML-learning-tracker\github-streak-maintainer\startup_streak.vbs"`
   - Name: `GitHub Streak Maintainer`
   - Click Finish

## 🔄 How It Works

1. **On Windows Startup**: The VBS script runs automatically
2. **Silent Execution**: Runs in background (no console window)
3. **Check Streak**: Checks if you've committed in last 24 hours
4. **Auto-Push**: If needed, updates file and pushes to GitHub
5. **Logging**: Creates `streak_run.log` for debugging

## ⚙️ Configuration

After first run, edit `streak_config.json` in repository root:

```json
{
    "hours_threshold": 24,
    "commit_message": "Update streak log",
    "enable_auto_push": true
}
```

## 📋 Verify Setup

1. **Check Startup Folder**:
   - Press `Win + R` → `shell:startup`
   - You should see "GitHub Streak Maintainer" shortcut

2. **Test Run**:
   ```powershell
   cd github-streak-maintainer
   python schedule_streak.py
   ```

3. **Check Log File**:
   - Open `github-streak-maintainer/streak_run.log`
   - Should show recent run timestamps

## 🛑 Disable Auto-Start

**Option 1**: Delete the shortcut
- Press `Win + R` → `shell:startup`
- Delete "GitHub Streak Maintainer" shortcut

**Option 2**: PowerShell command
```powershell
Remove-Item "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\GitHub Streak Maintainer.lnk"
```

## 🔍 Troubleshooting

### Script doesn't run on startup
- Check if shortcut exists in Startup folder
- Verify Python is installed and in PATH
- Check `streak_run.log` for errors

### No commits being pushed
- Verify GitHub authentication (SSH key or Personal Access Token)
- Check `streak_config.json` → `enable_auto_push` is `true`
- Verify git remote: `git remote -v`

### Want to see output
- Edit `startup_streak.vbs`
- Change `0` to `1` in the last parameter to show console window

## 📝 Notes

- Script runs **once** when Windows starts
- It checks if commit is needed and pushes if >24 hours since last commit
- Runs silently in background (no popups)
- Logs are saved to `streak_run.log` for debugging
- Works even if you're not logged in (if configured properly)

## ✅ Status Check

After setup, restart your computer and verify:
1. Script runs automatically
2. Check `streak_run.log` for execution
3. Verify GitHub for new commits (if threshold exceeded)

