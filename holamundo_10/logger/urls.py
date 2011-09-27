from django.conf.urls.defaults import *
from django.views.generic import ListView
from logger.views import Index, uploader
from logger.models import Log

urlpatterns = patterns('logger.views',
    url(r'^$', Index.as_view(), name='logger_index'),
    url(r'^view/$', ListView.as_view(model=Log), name='logger_viewer'),
    url(r'^upload/$', uploader, name='logger_uploader'),
)