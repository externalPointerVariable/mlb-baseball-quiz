import os
import sys

# Add the current directory to the Python path
sys.path.append(os.path.dirname(__file__))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mlb.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
