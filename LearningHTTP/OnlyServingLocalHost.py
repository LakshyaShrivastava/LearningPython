import sys
from http import server


HandlerClass = server.SimpleHTTPRequestHandler
ServerClass = server.HTTPServer
Protocol = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 80

server_address = ('127.0.0.1', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print("Serving HTTP on", sa[0], "port",sa[1], "...")
httpd.serve_forever()
