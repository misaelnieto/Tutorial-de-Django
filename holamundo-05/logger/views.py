from os.path import join as joinpath, dirname
from StringIO import StringIO

from django.http import HttpResponse

from parser import parsear

def parser_view(response) :
    resp = StringIO()
    fp = open(joinpath(dirname(__file__),'error_log-20110904'), 'r')
    for line in fp.readlines():
        resp.writelines('|'.join(parsear(line)) + '\n')
        
    hresp = HttpResponse(resp.getvalue())
    hresp['Content-Type'] = 'text/plain'
    return hresp

from django.template import Context, loader

def hola(response):
    t = loader.get_template('hola.html')
    c = Context({
        'mensaje': u'Hola mundo',
    })
    return HttpResponse(t.render(c))

