
from wsgiref.simple_server import make_server

def simpleweb(environ, start_fn):
    start_fn('200 OK', [('Content-Type', 'text/plain')])
    return ["Hello World!\n"]


httpd = make_server (
    'ip-172-31-27-43', # The host name
    9091, # A port number where to wait for the request
    simpleweb # The application object name, in this case a function
)
print "serving on port 9091..."

httpd.serve_forever()
