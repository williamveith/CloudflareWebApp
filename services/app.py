from fastapi import FastAPI, WebSocket
import uvicorn
from routes import route_definitions
import importlib

app = FastAPI()

def import_handler(handler_path):
    module_name, function_name = handler_path.rsplit('.', 1)
    module = importlib.import_module(module_name)
    return getattr(module, function_name)

for path, handler_ref in route_definitions.items():
    handler = import_handler(handler_ref)
    match path:
        case "/ws/logs":
            app.websocket_route(path)(handler)
        case _:
            app.get(path)(handler)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
