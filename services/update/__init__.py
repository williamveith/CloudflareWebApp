from fastapi import APIRouter, HTTPException
import subprocess

# Initialize the router (optional if integrating with a larger app structure)
router = APIRouter()

# Update handler function
async def update_handler():
    """
    Pulls the latest code from the GitHub repository and rebuilds the Docker containers.
    """
    try:
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
