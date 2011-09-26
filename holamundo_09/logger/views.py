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
    
    resp = StringIO()
    fp = open(joinpath(dirname(__file__),'error_log-20110904'), 'r')
    log = [parsear(z) for z in fp.readlines()]
    fp.close()
    c = Context({
        'log': log,
    })
    return HttpResponse(t.render(c))

############
#Formulario

from datetime import datetime
from django import forms
from django.core.context_processors import csrf
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from logger.models import Log

class UploaderForm(forms.Form):
    logfile = forms.FileField(required=True)

def uploader(request):
    if request.method == 'POST':
        #Si ya mandaron el formulario entonces necesitaremos un formulario
        #"atado" a POST y FILES
        form = UploaderForm(request.POST, request.FILES)
        if form.is_valid(): 
            file_data = form['logfile']
            for line in file_data.value().readlines():
                p = parsear(line)
                if len(p) == 3:
                    fecha, tipo, mensaje = p
                    fecha = datetime.strptime(fecha, '%a %b %d %H:%M:%S %Y')
                    l = Log(fecha = fecha, tipo = tipo, mensaje = mensaje)
                    l.save()
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        #Esto ocurre si acaban de visitar la pagina.
        form = UploaderForm() # Un formulario "desatado" o "unbound"

    #CSRF
    c = {'form': form}
    c.update(csrf(request))
    return render_to_response('uploader.html', c)
