"""
WSGI config for bookmanager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/home/ubuntu/.virtualenvs/py3_django/lib/python3.6/site-packages')
print(sys.path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookmanager.settings")

application = get_wsgi_application()
