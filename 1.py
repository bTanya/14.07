from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from wsgiref.simple_server import make_server


"""def app(env,start_res):
    req = Request(env)
    res = Response("", mimetype ='text/html')
    print(req.args)
    print (req.form)
    print (req.path)
    return res(env,start_res)


@Request.application
def app(req):
    print (req.path)
    return Response('')
    """
def form(req,**v):
    print (v)
    return Response(v.values())
route = {
    'form': form,
    'form1': form
}
@Request.application
def app(req):

    url_map =Map([Rule('/',endpoint='index'),
                  Rule('/form',endpoint='form'),
                  Rule('/form/<id>', endpoint='form1')])
    urls = url_map.bind_to_environ(req.environ)
    return urls.dispatch(lambda e,v: route[e](req,**v))


serv = make_server('localhost',8080,app)
serv.serve_forever()
