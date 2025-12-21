import subprocess
from datetime import datetime
import sys


def run_command(command: list[str]) -> None:
    """
    Run a shell command and exit if it fails.
    """
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        print("ERROR running command:", " ".join(command))
        print(result.stderr.strip())
        sys.exit(1)

    if result.stdout.strip():
        print(result.stdout.strip())


def main():
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    commit_message = f"push by Bhavesh at {timestamp}"

    print("Adding all changes...")
    run_command(["git", "add", "."])

    print("Creating commit...")
    run_command(["git", "commit", "-m", commit_message])

    print("Pushing to main branch...")
    run_command(["git", "push -f", "origin", "main"])

    print("Done. Code pushed successfully.")


if __name__ == "__main__":
    main()
