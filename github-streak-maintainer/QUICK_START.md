# Quick Start Guide - GitHub Streak Maintainer

## 🚀 Quick Setup (5 minutes)

### Step 1: Test the Script Manually

```bash
# Navigate to the github-streak-maintainer folder
cd C:\Users\bhave\OneDrive\Desktop\AIML-learning-tracker\github-streak-maintainer

# Run the script (it will automatically detect the parent directory as repo root)
python github_streak_maintainer.py

# Or run from repository root with explicit path
cd C:\Users\bhave\OneDrive\Desktop\AIML-learning-tracker
python github-streak-maintainer\github_streak_maintainer.py
```

**Expected Output:**
- If you've committed recently: "✅ Recent commit found. No streak update needed."
- If it's been >24 hours: The script will update `streak_log.txt` and push to GitHub

### Step 2: Set Up Automated Scheduling (Windows)

**Option A: Using PowerShell Script (Easiest)**
1. Right-click `setup_windows_task.ps1` → **Run with PowerShell**
2. Enter the time you want it to run daily (e.g., `18:00` for 6 PM)
3. Done! ✅

**Option B: Manual Task Scheduler Setup**
1. Open **Task Scheduler**
2. Create Basic Task → Name: "GitHub Streak Maintainer"
3. Trigger: Daily at your preferred time
4. Action: Start a program
   - Program: `pythonw.exe` (or full path to Python)
   - Arguments: `"C:\Users\bhave\OneDrive\Desktop\AIML-learning-tracker\github-streak-maintainer\schedule_streak.py"`
   - Start in: `C:\Users\bhave\OneDrive\Desktop\AIML-learning-tracker`
5. Save and test by right-clicking → Run

### Step 3: Verify GitHub Authentication

Make sure you can push to GitHub:

```bash
# Test SSH (if using SSH)
ssh -T git@github.com

# Or test HTTPS push
git push origin main
```

If authentication fails, see `GITHUB_STREAK_SETUP.md` for detailed setup.

## 📝 Customization

Edit `streak_config.json` (created automatically after first run):

```json
{
    "hours_threshold": 24,        // Check every X hours
    "commit_message": "Update streak log",  // Custom commit message
    "enable_auto_push": true      // Set to false to only update file
}
```

## 🔍 Troubleshooting

**"Not a git repository"**
- Run the script from your repository directory
- Or use: `python github_streak_maintainer.py --repo-path "C:\path\to\repo"`

**"Authentication failed"**
- Set up SSH key or Personal Access Token (see `GITHUB_STREAK_SETUP.md`)

**Script runs but doesn't push**
- Check `streak_config.json` → `enable_auto_push` should be `true`
- Verify remote: `git remote -v`

## 📚 More Information

See `GITHUB_STREAK_SETUP.md` for detailed documentation.

