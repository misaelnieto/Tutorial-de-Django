import os
import sys

path = '/opt/djangoapps'
if path not in sys.path:
    sys.path.append(path)
path = '/opt/djangoapps/holamundo'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'holamundo.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
