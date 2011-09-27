#Python
from datetime import datetime

#django
from django import forms
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView

#Logger app
from logger.parser import parsear
from logger.models import Log

class Index(TemplateView):
    template_name = 'index.html'


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
    return render_to_response('uploader.html', RequestContext(request, c))
