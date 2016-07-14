import falcon
from wsgiref.simple_server import make_server

class Resours():

    def on_get(self,req,res):
        res.body = '{"message":"test"}'
        res.status = falcon.HTTP_200
        req.stream

api = falcon.API()
r = Resours()
api.add_route('/',r)

serv = make_server('',8080,api)
serv.serve_forever()