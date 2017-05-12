#_*_ coding:utf-8 _*_
from twisted.web.resource import Resource
from twisted.web import server
from twisted.web import static
from twisted.internet import reactor
PORT = 1235
########################################################################
class ReStructured(Resource):
    """"""

    #----------------------------------------------------------------------
    def __init__(self,filename,*a):
        """Constructor"""
        self.rst = open(filename).read()
    def render(self, request):
        return self.rst
resource = static.File('C:\Users\hide on bush\Desktop\python\/')
resource.processors = {'.html' : ReStructured}
resource.indexNames = ['index.html']
reactor.listenTCP(
    PORT,
    server.Site( resource )
    ) 
reactor.run()
        
    
    
