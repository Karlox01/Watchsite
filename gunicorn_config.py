# gunicorn_config.py

# Number of worker processes
workers = 4

# Address and port to bind to (0.0.0.0 means bind to all available network interfaces)
bind = "0.0.0.0:8000"

# Specify the path to your Django project's WSGI application
wsgi_app = "watchsite.wsgi:application"