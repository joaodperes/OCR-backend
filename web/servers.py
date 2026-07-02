import json


def handle(handler):

    handler.send_response(200)
    handler.send_header("Content-Type", "application/json")
    handler.end_headers()

    handler.wfile.write(json.dumps({
        "servers": [
            {
                "HostName": "Local",
                "PublicIP": "127.0.0.1",
                "ServerRegion": 10
            }
        ]
    }).encode())