"""
GitHub Streak Maintainer
Automatically pushes a commit to GitHub if no commits were made in the last 24 hours.
This helps maintain your GitHub contribution streak.
"""

import os
import subprocess
import json
from datetime import datetime, timedelta
from pathlib import Path
import sys

# Fix Windows console encoding for emoji support
if sys.platform == 'win32':
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except:
        pass  # Fallback if encoding change fails

class GitHubStreakMaintainer:
    def __init__(self, repo_path=None, streak_file="streak_log.txt"):
        """
        Initialize the GitHub Streak Maintainer.
        
        Args:
            repo_path: Path to the git repository (defaults to current directory)
            streak_file: Name of the file to update for streak maintenance
        """
        self.repo_path = Path(repo_path) if repo_path else Path.cwd()
        self.streak_file = self.repo_path / streak_file
        self.config_file = self.repo_path / "streak_config.json"
        
    def load_config(self):
        """Load configuration from JSON file."""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Warning: Invalid config file. Using defaults.")
        
        return {
            "hours_threshold": 24,
            "commit_message": "Update streak log",
            "enable_auto_push": True
        }
    
    def save_config(self, config):
        """Save configuration to JSON file."""
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=4)
    
    def check_git_repo(self):
        """Check if current directory is a git repository."""
        try:
            result = subprocess.run(
                ['git', 'rev-parse', '--git-dir'],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def get_last_commit_time(self):
        """Get the timestamp of the last commit."""
        try:
            result = subprocess.run(
                ['git', 'log', '-1', '--format=%ct'],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            if result.stdout.strip():
                timestamp = int(result.stdout.strip())
                return datetime.fromtimestamp(timestamp)
            return None
        except subprocess.CalledProcessError:
            return None
    
    def check_remote_commits(self):
        """Check if there are unpushed commits or fetch latest from remote."""
        try:
            # Fetch latest from remote
            subprocess.run(
                ['git', 'fetch', 'origin'],
                cwd=self.repo_path,
                capture_output=True,
                check=True
            )
            
            # Check if local is behind remote
            result = subprocess.run(
                ['git', 'rev-list', '--count', 'HEAD..origin/main'],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )
            
            # Try master branch if main doesn't exist
            if result.returncode != 0:
                result = subprocess.run(
                    ['git', 'rev-list', '--count', 'HEAD..origin/master'],
                    cwd=self.repo_path,
                    capture_output=True,
                    text=True
                )
            
            return result.returncode == 0 and int(result.stdout.strip()) > 0
        except:
            return False
    
    def needs_streak_update(self, hours_threshold=24):
        """
        Check if a streak update is needed.
        Returns True if last commit was more than threshold hours ago.
        """
        last_commit = self.get_last_commit_time()
        
        if last_commit is None:
            print("No commits found. Creating initial streak log.")
            return True
        
        time_diff = datetime.now() - last_commit
        hours_since_last_commit = time_diff.total_seconds() / 3600
        
        print(f"Last commit: {last_commit.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Hours since last commit: {hours_since_last_commit:.2f}")
        
        if hours_since_last_commit >= hours_threshold:
            print(f"[!] No commits in the last {hours_threshold} hours. Streak update needed!")
            return True
        else:
            print(f"[OK] Recent commit found. No streak update needed.")
            return False
    
    def update_streak_file(self):
        """Update the streak log file with current timestamp."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        if self.streak_file.exists():
            with open(self.streak_file, 'r') as f:
                content = f.read()
        else:
            content = ""
        
        new_entry = f"\nStreak maintained: {timestamp}\n"
        content += new_entry
        
        with open(self.streak_file, 'w') as f:
            f.write(content)
        
        print(f"[OK] Updated {self.streak_file.name}")
        return True
    
    def commit_and_push(self, commit_message="Update streak log"):
        """Commit and push changes to GitHub."""
        try:
            # Add the streak file
            subprocess.run(
                ['git', 'add', str(self.streak_file)],
                cwd=self.repo_path,
                check=True
            )
            print(f"[OK] Added {self.streak_file.name} to staging")
            
            # Commit
            subprocess.run(
                ['git', 'commit', '-m', commit_message],
                cwd=self.repo_path,
                check=True
            )
            print(f"[OK] Committed changes: {commit_message}")
            
            # Push to remote
            # Try main branch first, then master
            branches = ['main', 'master']
            pushed = False
            
            for branch in branches:
                try:
                    result = subprocess.run(
                        ['git', 'push', 'origin', branch],
                        cwd=self.repo_path,
                        capture_output=True,
                        text=True,
                        check=True
                    )
                    print(f"[OK] Pushed to origin/{branch}")
                    pushed = True
                    break
                except subprocess.CalledProcessError:
                    continue
            
            if not pushed:
                # Try to push current branch
                result = subprocess.run(
                    ['git', 'branch', '--show-current'],
                    cwd=self.repo_path,
                    capture_output=True,
                    text=True
                )
                current_branch = result.stdout.strip()
                if current_branch:
                    subprocess.run(
                        ['git', 'push', 'origin', current_branch],
                        cwd=self.repo_path,
                        check=True
                    )
                    print(f"[OK] Pushed to origin/{current_branch}")
            
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Error during git operations: {e}")
            print("Make sure you have:")
            print("  1. Git configured (git config --global user.name and user.email)")
            print("  2. Remote repository set up (git remote add origin <url>)")
            print("  3. Authentication configured (SSH key or Personal Access Token)")
            return False
    
    def run(self):
        """Main execution method."""
        print("=" * 60)
        print("GitHub Streak Maintainer")
        print("=" * 60)
        
        # Check if git repo exists
        if not self.check_git_repo():
            print("[ERROR] Error: Not a git repository!")
            print(f"   Current directory: {self.repo_path}")
            print("   Please run this script from a git repository directory.")
            return False
        
        # Load configuration
        config = self.load_config()
        hours_threshold = config.get("hours_threshold", 24)
        commit_message = config.get("commit_message", "Update streak log")
        auto_push = config.get("enable_auto_push", True)
        
        # Check if streak update is needed
        if not self.needs_streak_update(hours_threshold):
            return True
        
        # Update streak file
        self.update_streak_file()
        
        # Commit and push if enabled
        if auto_push:
            success = self.commit_and_push(commit_message)
            if success:
                print("\n[SUCCESS] Streak maintained successfully!")
            return success
        else:
            print("\n[!] Auto-push is disabled. Please commit and push manually.")
            print(f"   File updated: {self.streak_file}")
            return True


def main():
    """Entry point for the script."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Maintain GitHub streak by auto-pushing commits"
    )
    parser.add_argument(
        '--repo-path',
        type=str,
        help='Path to git repository (default: current directory)'
    )
    parser.add_argument(
        '--streak-file',
        type=str,
        default='streak_log.txt',
        help='Name of the file to update (default: streak_log.txt)'
    )
    parser.add_argument(
        '--hours',
        type=int,
        default=24,
        help='Hours threshold for checking commits (default: 24)'
    )
    parser.add_argument(
        '--no-push',
        action='store_true',
        help='Update file but do not push to GitHub'
    )
    
    args = parser.parse_args()
    
    maintainer = GitHubStreakMaintainer(
        repo_path=args.repo_path,
        streak_file=args.streak_file
    )
    
    # Update config if hours specified
    if args.hours != 24:
        config = maintainer.load_config()
        config['hours_threshold'] = args.hours
        maintainer.save_config(config)
    
    # Update config if no-push specified
    if args.no_push:
        config = maintainer.load_config()
        config['enable_auto_push'] = False
        maintainer.save_config(config)
    
    success = maintainer.run()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

