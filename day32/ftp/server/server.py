import json
import struct
import socketserver
import operate_handler
class MyFTP(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        length = conn.recv(4)
        length = struct.unpack('i',length)[0]
        opertate = (conn.recv(length)).decode('utf-8')
        opertate_dic = json.loads(opertate)
        opt = opertate_dic['operate']
        usr = opertate_dic['user']
        print(opt,usr)
        getattr(operate_handler,opt)(conn,usr)

socketserver.TCPServer.allow_reuse_address = True
server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),MyFTP)
server.serve_forever()