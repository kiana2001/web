"""
WSGI config for TravelAgency project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os, sys

path = '/home/kioriaTravel/TravelAgencySite'
if path not in sys.path:
   sys.path.insert(0, path)
      
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TravelAgencySite.settings')

application = get_wsgi_application()
