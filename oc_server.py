from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET", self.path)
        print(self.headers)

        if self.path == "/abc":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"http://127.0.0.1:8080/")
            return
        
        elif self.path == "/version/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"1.0d")
            return
        
        elif self.path == "/servers":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps({
                "servers": [
                    {
                        "HostName": "Local",
                        "PublicIP": "127.0.0.1",
                        "ServerRegion": 10
                    }
                ]
            }).encode())

            return

        elif self.path.startswith("/auth/st/"):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            account = {
                "Id": "00000000-0000-0000-0000-000000000001",
                "AccountName": "Developer",
                "Token": "DEVTOKEN",
                "RealName": "",
                "Email": "",
                "HasEmail": False,
                "IsActivated": True,
                "IsAdmin": False,
                "IsGuest": False
            }

            self.wfile.write(json.dumps(account).encode())
            return

        elif self.path.startswith("/system/"):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps({
                "HostName": "Local",
                "PublicIP": "127.0.0.1",
                "ServerRegion": 10
            }).encode())

            return

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)

        print(f"POST {self.path}")
        print(body.decode(errors="ignore"))

        self.send_response(200)
        self.end_headers()

HTTPServer(("127.0.0.1",8080), Handler).serve_forever()