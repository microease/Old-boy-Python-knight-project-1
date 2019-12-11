import socketserver
# tcp协议的server端就不需要导入socket
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        while True:
            conn.send(b'hello')
            print(conn.recv(1024))

server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)
server.serve_forever()