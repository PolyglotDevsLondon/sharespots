release: python ./manage.py migrate
web: gunicorn --pythonpath sharespots sharespots.wsgi:application