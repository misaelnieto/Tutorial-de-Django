# Create your views here.
from django.http import HttpResponse

def hola(response):
    return HttpResponse('Hola Mundo')


