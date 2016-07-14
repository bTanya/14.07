from twisted.plugins import twisted_socks
from twisted.web import  server,resource
from twisted.internet import  reactor

class Simple(resource.Resource):
    isLeaf = True

    def render_GET(self,req):
       return "Hello"

site = server.Site(Simple())
reactor.listenTCP(9000,site)
reactor.run()