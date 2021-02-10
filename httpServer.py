import SimpleHTTPServer
import SocketServer
import socket

PORT = 8080
HOST = socket.gethostname()
IP = socket.gethostbyname(HOST)


Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer((IP, PORT), Handler)

print "Serving at port", PORT
print "Victim Username", HOST
print "Victim IP", IP
httpd.serve_forever()