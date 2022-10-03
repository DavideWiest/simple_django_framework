"""
WSGI config for personal_website2 project.

It exposes the WSGI callable as a module-level variable named application.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application
import sys

sys.path.append("{{ project_path }}")
sys.path.append("{{ project_path.replace(project_branch_name + '/', '') }}")

os.environ.setdefault("DJANGO_SETTINGS_MODULE","{{ project_name }}.settings")

application = get_wsgi_application()