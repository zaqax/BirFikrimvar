"""
WSGI config for birfikrimvar project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birfikrimvar.settings')

application = get_wsgi_application()