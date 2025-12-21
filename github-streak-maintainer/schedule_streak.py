"""
Windows Startup/Task Scheduler Helper Script
Run this script automatically on startup or periodically to check and maintain GitHub streak.
Runs silently in the background.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_streak_maintainer():
    """Run the streak maintainer script."""
    script_path = Path(__file__).parent / "github_streak_maintainer.py"
    # Get the repository root (parent directory of github-streak-maintainer folder)
    repo_root = Path(__file__).parent.parent
    
    # Log file for debugging (optional)
    log_file = Path(__file__).parent / "streak_run.log"
    
    try:
        # Run the script and capture output
        result = subprocess.run(
            [sys.executable, str(script_path), "--repo-path", str(repo_root)],
            capture_output=True,
            text=True,
            cwd=str(repo_root)
        )
        
        # Log the result (optional, for debugging)
        with open(log_file, 'a', encoding='utf-8') as f:
            from datetime import datetime
            f.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Run completed\n")
            f.write(result.stdout)
            if result.stderr:
                f.write(f"\nErrors: {result.stderr}\n")
        
        return result.returncode == 0
    except Exception as e:
        # Log errors
        try:
            with open(log_file, 'a', encoding='utf-8') as f:
                from datetime import datetime
                f.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error: {e}\n")
        except:
            pass
        return False

if __name__ == "__main__":
    # Run silently (no console window)
    success = run_streak_maintainer()
    sys.exit(0 if success else 1)

