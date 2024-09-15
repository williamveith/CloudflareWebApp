from fastapi import APIRouter, HTTPException
import subprocess
import subprocess
from pathlib import Path

# Initialize the router (optional if integrating with a larger app structure)
router = APIRouter()

# Define the path to the local repository
repo_path = Path("git@github.com:williamveith/CloudflareWebApp.git")  # Update this with the correct path to your local repository

# Check if the .git directory exists using pathlib
if (repo_path / ".git").is_dir():
    # Run git pull if the repository already exists
    try:
        print("Repository found, pulling latest changes...")
        pull_result = subprocess.run(
            ["git", "pull", "origin", "main"],
            cwd=repo_path,
            check=True,
            capture_output=True,
            text=True
        )
        print(pull_result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error pulling repository: {e.stderr}")
else:
    # Run git clone if the repository does not exist
    try:
        print("Repository not found, cloning...")
        clone_result = subprocess.run(
            ["git", "clone", "git@github.com:williamveith/CloudflareWebApp.git", str(repo_path)],
            check=True,
            capture_output=True,
            text=True
        )
        print(clone_result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e.stderr}")


# Update handler function
async def update_handler():
    """
    Pulls the latest code from the GitHub repository and rebuilds the Docker containers.
    """
    try:
        ["git", "clone", "git@github.com:williamveith/CloudflareWebApp.git"]
        ["git", "pull", "origin", "main"]
        pull_command = ["git", "pull", "origin", "main"]
        pull_result = subprocess.run(pull_command, capture_output=True, text=True)
        
        if pull_result.returncode != 0:
            raise Exception(f"Git pull failed: {pull_result.stderr}")

        compose_command = ["docker-compose", "up", "--build", "-d"]
        compose_result = subprocess.run(compose_command, capture_output=True, text=True)
        
        if compose_result.returncode != 0:
            raise Exception(f"Docker Compose build failed: {compose_result.stderr}")

        return {"message": "Update successful", "git_output": pull_result.stdout, "compose_output": compose_result.stdout}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
