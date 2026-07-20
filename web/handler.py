from http.server import BaseHTTPRequestHandler

from web import auth
from web import servers
from web import system

from transport.router import router

import json

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        print(self.path)

        if self.path == "/abc":

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"http://127.0.0.1:8080/")
            return

        if self.path == "/version/":

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"1.0d")
            return

        if self.path == "/servers":

            return servers.handle(self)

        if self.path.startswith("/auth/st/"):

            return auth.handle(self)

        if self.path.startswith("/system/"):

            return system.handle(self)

        self.send_response(404)
        self.end_headers()

    def do_POST(self):

        length = int(self.headers.get("Content-Length", 0))

        body = self.rfile.read(length)

        try:
            payload = json.loads(body.decode())
        except Exception:
            payload = {}

        result = router.dispatch(

            payload.get("opcode"),

            payload
        )

        self.send_response(200)

        self.send_header("Content-Type", "application/json")

        self.end_headers()

        self.wfile.write(

            json.dumps(result).encode()

        )