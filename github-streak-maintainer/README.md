# GitHub Streak Maintainer

Automatically maintain your GitHub contribution streak by pushing commits when you haven't pushed code in the last 24 hours.

## 📁 Project Structure

```
github-streak-maintainer/
├── github_streak_maintainer.py  # Main script
├── schedule_streak.py           # Windows Task Scheduler helper
├── setup_windows_task.ps1      # Automated Windows setup script
├── streak_log.txt              # File that gets updated for streak
├── requirements.txt            # Python dependencies (none required)
├── .gitignore                  # Git ignore rules
├── GITHUB_STREAK_SETUP.md     # Detailed setup guide
├── QUICK_START.md             # Quick start guide
└── README.md                   # This file
```

## 🚀 Quick Start

1. **Test the script:**
   ```bash
   python github_streak_maintainer.py
   ```

2. **Set up auto-start on boot (Recommended):**
   - Right-click `setup_startup.ps1` → Run with PowerShell
   - Script will run automatically when Windows starts
   - See `STARTUP_SETUP.md` for details

3. **Alternative: Scheduled Task:**
   - Right-click `setup_windows_task.ps1` → Run with PowerShell
   - Runs at a specific time daily

## 📚 Documentation

- **QUICK_START.md** - Get started in 5 minutes
- **GITHUB_STREAK_SETUP.md** - Complete setup guide with troubleshooting

## ⚙️ Configuration

After first run, edit `streak_config.json` (auto-generated):

```json
{
    "hours_threshold": 24,
    "commit_message": "Update streak log",
    "enable_auto_push": true
}
```

## 🔧 Requirements

- Python 3.6+
- Git configured
- GitHub repository with remote origin
- GitHub authentication (SSH key or Personal Access Token)

## 📝 Usage

```bash
# Basic usage
python github_streak_maintainer.py

# Custom repository path
python github_streak_maintainer.py --repo-path /path/to/repo

# Custom hours threshold
python github_streak_maintainer.py --hours 12

# Update file without pushing
python github_streak_maintainer.py --no-push
```

## 🎯 How It Works

1. Checks if you're in a git repository
2. Gets the timestamp of your last commit
3. Calculates hours since last commit
4. If >24 hours (or your threshold), updates `streak_log.txt`
5. Commits and pushes the change automatically

## ⚠️ Important Notes

- Make sure Git is configured (`git config --global user.name` and `user.email`)
- Set up GitHub authentication before using
- The script only pushes if you haven't committed in the threshold period
- Won't create duplicate commits if you've already pushed recently

