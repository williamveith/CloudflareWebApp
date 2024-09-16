import subprocess
from pathlib import Path
from fastapi import Request

async def update_handler(request: Request):
    # Define the path to the local repository (update this path to the actual local path)
    repo_path = Path("git@github.com:williamveith/CloudflareWebApp.git") # Replace with the path where you want your repo

    # Try to pull changes from the repository
    try:
        # Attempt to pull the latest changes
        print("Attempting to pull latest changes...")
        pull_result = subprocess.run(
            ["git", "-C", str(repo_path), "pull", "origin", "main"],  # Runs pull in the specified directory
            check=True,
            capture_output=True,
            text=True
        )
        print(pull_result.stdout)
    except subprocess.CalledProcessError:
        # If pull fails, attempt to clone the repository
        try:
            print("Pull failed, attempting to clone the repository...")
            clone_result = subprocess.run(
                ["git", "clone", "git@github.com:williamveith/CloudflareWebApp.git", str(repo_path)],  # Clones into the specified path
                check=True,
                capture_output=True,
                text=True
            )
            print(clone_result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error cloning repository: {e.stderr}")