"""
WSGI config for django_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.core.wsgi import get_wsgi_application
import socketio

from socketio_app.views import sio
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.settings')


django_app = get_wsgi_application()
application = socketio.WSGIApp(sio, django_app)
