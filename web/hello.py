def application(environ, start_response):
    params = [param for param in environ['QUERY_STRING'].split('&')] 
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['\n'.join(params).encode()]
