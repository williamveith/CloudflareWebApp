from fastapi import Request
from fastapi.responses import FileResponse
from pathlib import Path

FILE_PATH = Path(__file__).parent / "home.html"

async def home_handler(request: Request):
    # Serve the home.html file from the home directory
    return FileResponse(str(FILE_PATH))
