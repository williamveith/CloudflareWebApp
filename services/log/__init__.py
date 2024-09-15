from starlette.websockets import WebSocket
import subprocess
import asyncio

async def log_handler(websocket: WebSocket):
    await websocket.accept()
    command = ["docker", "logs", "-f", "wireguard"]
    process = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while True:
        line = await process.stdout.readline()
        if not line:
            break
        await websocket.send_text(line.decode('utf-8'))
    await websocket.close()