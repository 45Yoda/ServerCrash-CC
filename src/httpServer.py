import http.server
import socketserver

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('localhost',8002),Handler) as httpd:
    httpd.serve_forever()

