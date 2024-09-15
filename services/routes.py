route_definitions = {
    "/": "home.home_handler",        # Home route
    "/ws/logs": "log.log_handler",   # WebSocket route for logs
    "/update": "update_handler",     # Update route to pull and rebuild the Docker containers
}
