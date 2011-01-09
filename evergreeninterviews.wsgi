import os
import sys
os.environ["DJANGO_SETTINGS_MODULE"] = "evergreeninterviews.settings.local"
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
