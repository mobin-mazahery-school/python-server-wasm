import os
import json
import time
import requests
from http.server import SimpleHTTPRequestHandler, HTTPServer


class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        with open("/public/app/statu.txt", "a") as f:
            f.write(time.strftime('%X %x %Z') + "\n")

        with open("/public/app/statu.txt", "r") as f:
            data = {
                "message": f.read()
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))


if __name__ == "__main__":
    host = os.environ.get('HOST', '127.0.0.1')

    # Get the PORT environment variable if it's present; otherwise, default to 8000
    port = int(os.environ.get('PORT', 80))

    server = HTTPServer((host, port), CustomHandler)
    print(f"Starting server on http://{host}:{port}")
    server.serve_forever()
