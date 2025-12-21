# GitHub Streak Maintainer - Setup Guide

This project helps you maintain your GitHub contribution streak by automatically pushing a commit if you haven't pushed any code in the last 24 hours.

## Features

- ✅ Automatically checks if you've committed in the last 24 hours
- ✅ Updates a log file and pushes to GitHub if needed
- ✅ Configurable threshold (default: 24 hours)
- ✅ Works with any git repository
- ✅ Cross-platform (Windows, macOS, Linux)

## Prerequisites

1. **Python 3.6+** installed on your system
2. **Git** installed and configured
3. A **GitHub repository** set up with remote origin

## Initial Setup

### 1. Configure Git (if not already done)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 2. Set up GitHub Authentication

You have two options:

#### Option A: SSH Key (Recommended)
1. Generate an SSH key if you don't have one:
   ```bash
   ssh-keygen -t ed25519 -C "your.email@example.com"
   ```
2. Add the SSH key to your GitHub account:
   - Copy the public key: `cat ~/.ssh/id_ed25519.pub`
   - Go to GitHub → Settings → SSH and GPG keys → New SSH key
   - Paste your key and save

#### Option B: Personal Access Token
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate a new token with `repo` scope
3. When pushing, use the token as your password:
   ```bash
   git remote set-url origin https://YOUR_TOKEN@github.com/username/repo.git
   ```

### 3. Ensure Your Repository Has a Remote

```bash
git remote -v
```

If no remote exists, add one:
```bash
git remote add origin https://github.com/username/your-repo.git
```

## Usage

### Manual Run

Simply run the script from your repository directory:

```bash
python github_streak_maintainer.py
```

### Command Line Options

```bash
# Use a different repository path
python github_streak_maintainer.py --repo-path /path/to/repo

# Use a different file name
python github_streak_maintainer.py --streak-file my_log.txt

# Change the hours threshold (e.g., check every 12 hours)
python github_streak_maintainer.py --hours 12

# Update file but don't push (useful for testing)
python github_streak_maintainer.py --no-push
```

## Automated Scheduling

### Windows Task Scheduler

1. Open **Task Scheduler** (search for it in Windows)
2. Click **Create Basic Task**
3. Name it: "GitHub Streak Maintainer"
4. Set trigger: **Daily** at a convenient time (e.g., 6:00 PM)
5. Action: **Start a program**
6. Program: `pythonw.exe` (or full path to Python)
7. Arguments: `"C:\path\to\schedule_streak.py"`
8. Start in: `C:\path\to\your\repository`
9. Check **Run whether user is logged on or not**
10. Save and test

**Alternative PowerShell Script** (create `schedule_task.ps1`):

```powershell
$action = New-ScheduledTaskAction -Execute "pythonw.exe" -Argument "C:\path\to\schedule_streak.py" -WorkingDirectory "C:\path\to\your\repository"
$trigger = New-ScheduledTaskTrigger -Daily -At 6pm
Register-ScheduledTask -TaskName "GitHub Streak Maintainer" -Action $action -Trigger $trigger -Description "Maintains GitHub streak"
```

### macOS/Linux (Cron)

Add to your crontab (`crontab -e`):

```bash
# Run every day at 6 PM
0 18 * * * cd /path/to/your/repo && /usr/bin/python3 github_streak_maintainer.py >> /tmp/streak.log 2>&1

# Or run every 12 hours
0 */12 * * * cd /path/to/your/repo && /usr/bin/python3 github_streak_maintainer.py >> /tmp/streak.log 2>&1
```

## Configuration

The script creates a `streak_config.json` file automatically. You can edit it:

```json
{
    "hours_threshold": 24,
    "commit_message": "Update streak log",
    "enable_auto_push": true
}
```

## How It Works

1. **Check Git Repository**: Verifies you're in a git repository
2. **Check Last Commit**: Gets the timestamp of your last commit
3. **Compare Time**: Calculates hours since last commit
4. **Update if Needed**: If >24 hours (or your threshold), updates `streak_log.txt`
5. **Commit & Push**: Automatically commits and pushes the change

## Troubleshooting

### "Not a git repository" Error
- Make sure you're running the script from your repository directory
- Or use `--repo-path` to specify the repository path

### "Authentication failed" Error
- Check your SSH key or Personal Access Token setup
- For SSH: Test with `ssh -T git@github.com`
- For HTTPS: Make sure your token is correct

### "No commits found" Error
- This is normal for a new repository
- The script will create an initial commit

### Script runs but doesn't push
- Check if `enable_auto_push` is `true` in `streak_config.json`
- Verify your remote is set correctly: `git remote -v`
- Check your branch name (script tries `main` and `master`)

## Notes

- The script only pushes if you haven't committed in the last 24 hours
- It won't create duplicate commits if you've already pushed today
- The `streak_log.txt` file tracks when streak updates were made
- You can safely delete `streak_log.txt` if you want to start fresh

## License

Free to use and modify for personal projects.

