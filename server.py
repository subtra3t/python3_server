import http.server # In Python 2 this module was known as SimpleHTTPServer
import socketserver



PORT = 8000 
HANDLER = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), HANDLER) as httpd:
	print("serving at port", PORT)
	httpd.serve_forever()