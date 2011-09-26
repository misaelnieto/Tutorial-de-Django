from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'holamundo.views.home', name='home'),
    # url(r'^holamundo/', include('holamundo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^upload/', 'logger.views.uploader'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'logger.views.hola', name='home'),
)
