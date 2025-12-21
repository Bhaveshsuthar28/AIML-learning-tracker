# How It Works - GitHub Streak Maintainer

## 🔄 Complete Workflow

### Step-by-Step Process

```
1. Windows Starts
   ↓
2. startup_streak.vbs runs automatically
   ↓
3. Calls schedule_streak.py silently
   ↓
4. schedule_streak.py calls github_streak_maintainer.py
   ↓
5. Checks last commit time
   ↓
6. Calculates hours since last commit
   ↓
7. Decision Point:
   ├─ If < 24 hours → Do nothing ✅
   └─ If ≥ 24 hours → Update & Push 🚀
```

## 📋 Detailed Explanation

### 1. **Windows Startup Trigger**

When your laptop starts:
- Windows looks in the Startup folder
- Finds "GitHub Streak Maintainer" shortcut
- Runs `startup_streak.vbs` automatically
- Runs silently (no window appears)

**File:** `startup_streak.vbs`
```vbscript
- Runs pythonw.exe (Python without console window)
- Executes schedule_streak.py
- Runs in background (hidden)
```

### 2. **Schedule Script Execution**

**File:** `schedule_streak.py`

What it does:
- Gets the repository root path (parent directory)
- Calls the main script with correct paths
- Logs execution to `streak_run.log`
- Handles errors gracefully

### 3. **Main Script Logic**

**File:** `github_streak_maintainer.py`

#### Step 1: Check Git Repository
```python
- Verifies you're in a git repository
- Checks if git is configured
```

#### Step 2: Get Last Commit Time
```python
- Runs: git log -1 --format=%ct
- Gets timestamp of last commit
- Converts to datetime object
```

#### Step 3: Calculate Time Difference
```python
current_time = datetime.now()
time_diff = current_time - last_commit_time
hours_since = time_diff.total_seconds() / 3600
```

#### Step 4: Decision Logic

**IF hours_since < 24:**
```
✅ Recent commit found
→ Do nothing
→ Exit successfully
```

**IF hours_since ≥ 24:**
```
⚠️ No commits in last 24 hours
→ Update streak_log.txt
→ Add file to git
→ Commit with message
→ Push to GitHub
```

### 4. **File Update Process**

When update is needed:

**File:** `streak_log.txt`
```
Before:
GitHub Streak Maintenance Log
=============================
Initialized: 2024-01-01 00:00:00

After:
GitHub Streak Maintenance Log
=============================
Initialized: 2024-01-01 00:00:00

Streak maintained: 2025-12-21 18:00:00
```

### 5. **Git Operations**

When pushing is needed:

```bash
# 1. Add file to staging
git add streak_log.txt

# 2. Commit with message
git commit -m "Update streak log"

# 3. Push to remote
git push origin main  # or master
```

## ⏰ Timing Example

### Scenario 1: Recent Commit
```
Last commit: 2025-12-21 14:00:00
Current time: 2025-12-21 16:00:00
Hours since: 2 hours

Result: ✅ No action needed (recent commit found)
```

### Scenario 2: Old Commit
```
Last commit: 2025-12-20 10:00:00
Current time: 2025-12-21 18:00:00
Hours since: 32 hours

Result: 🚀 Update file and push to GitHub
```

## 🔍 Configuration

**File:** `streak_config.json` (created after first run)

```json
{
    "hours_threshold": 24,        // How many hours to wait
    "commit_message": "Update streak log",  // Commit message
    "enable_auto_push": true      // Auto-push enabled
}
```

**Customization:**
- Change `hours_threshold` to check more/less frequently
- Change `commit_message` for custom commit messages
- Set `enable_auto_push` to `false` to only update file (no push)

## 📊 Logging

**File:** `streak_run.log`

Every execution is logged:
```
[2025-12-21 18:00:00] Run completed
============================================================
GitHub Streak Maintainer
============================================================
Last commit: 2025-12-21 14:29:46
Hours since last commit: 2.43
[OK] Recent commit found. No streak update needed.
```

## 🎯 Key Features

### 1. **Automatic Execution**
- Runs when Windows starts
- No manual intervention needed
- Runs silently in background

### 2. **Smart Detection**
- Only pushes if >24 hours since last commit
- Won't create duplicate commits
- Respects your actual commits

### 3. **Error Handling**
- Checks if git repository exists
- Verifies git configuration
- Handles authentication errors
- Logs all errors

### 4. **Silent Operation**
- No popups or windows
- Runs in background
- Uses `pythonw.exe` (no console)

## 🔄 Complete Example Flow

### Day 1 (Monday 9 AM)
```
You commit code manually
→ Last commit: Monday 9:00 AM
```

### Day 2 (Tuesday 8 AM - Laptop Starts)
```
Windows starts
→ startup_streak.vbs runs
→ Checks last commit: Monday 9:00 AM
→ Hours since: 23 hours
→ Result: ✅ No action (still < 24 hours)
```

### Day 2 (Tuesday 10 AM - Laptop Starts Again)
```
Windows starts
→ startup_streak.vbs runs
→ Checks last commit: Monday 9:00 AM
→ Hours since: 25 hours
→ Result: 🚀 Update needed!
→ Updates streak_log.txt
→ Commits: "Update streak log"
→ Pushes to GitHub
→ New commit appears on GitHub ✅
```

### Day 3 (Wednesday - You Commit Manually)
```
You commit code at 2 PM
→ Last commit: Wednesday 2:00 PM
```

### Day 4 (Thursday 8 AM - Laptop Starts)
```
Windows starts
→ Checks last commit: Wednesday 2:00 PM
→ Hours since: 18 hours
→ Result: ✅ No action (recent commit found)
```

## 🛠️ Technical Details

### Files Involved

1. **startup_streak.vbs**
   - Windows startup script
   - Runs `pythonw.exe` silently
   - Located in Startup folder

2. **schedule_streak.py**
   - Wrapper script
   - Handles paths and logging
   - Calls main script

3. **github_streak_maintainer.py**
   - Main logic
   - Git operations
   - Decision making

4. **streak_log.txt**
   - File that gets updated
   - Tracks streak maintenance
   - Committed to repository

5. **streak_config.json**
   - Configuration file
   - Created automatically
   - Customizable settings

6. **streak_run.log**
   - Execution log
   - Debugging information
   - Timestamp of each run

## ❓ Common Questions

### Q: Will it push every time I start my laptop?
**A:** No! Only if it's been >24 hours since your last commit.

### Q: What if I commit manually?
**A:** The script detects your manual commits and won't push unnecessarily.

### Q: Does it run continuously?
**A:** No, it runs once when Windows starts, then exits.

### Q: Can I see what it's doing?
**A:** Yes! Check `streak_run.log` for execution details.

### Q: What if I'm offline?
**A:** The script will try to push, but will fail gracefully if offline. It will try again on next startup.

### Q: Will it interfere with my normal commits?
**A:** No! It only updates `streak_log.txt` and pushes that specific file.

## 🎓 Summary

**Simple Explanation:**
1. When Windows starts → Script runs automatically
2. Checks: "Did I commit in last 24 hours?"
3. If YES → Do nothing ✅
4. If NO → Update file and push to GitHub 🚀
5. Runs silently → No interruptions
6. Logs everything → Check `streak_run.log`

**Result:** Your GitHub streak is maintained automatically! 🎉

