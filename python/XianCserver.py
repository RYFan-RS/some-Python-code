#_*_ coding:utf-8 _*_
from SocketServer import TCPServer,ThreadingMixIn,StreamRequestHandler
class Server(ThreadingMixIn,TCPServer):
    pass
class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print '获取的连接来自：',addr
        self.wfile.write('使用thead方式实现多连接')
if __name__=='__name__':
    server = Server(('localhost',1234),Handler)
    server.serve_forever()