from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Enable CORS
        self.end_headers()

        with open('marks.json') as f:
            marks_data = json.load(f)

        query = parse_qs(self.path.split('?', 1)[-1])
        names = query.get('name', [])

        marks = [marks_data.get(name, 0) for name in names]  # Default 0 if not found

        response = {"marks": marks}
        self.wfile.write(json.dumps(response).encode())
