from fairwork_server.settings import *
import dj_database_url


DEBUG = True
TIME_ZONE = 'America/Los_Angeles' # or your timezone
MINIMUM_WAGE_PER_HOUR = 10

ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1", ".herokuapp.com"]

EMAIL_HOST = '' # email server so you can send notifications from the platform, e.g., SendGrid
EMAIL_HOST_USER = '' # username
EMAIL_HOST_PASSWORD = '' # password
EMAIL_PORT = 587
EMAIL_USE_TLS = True

ADMIN_NAME = "UT Information Retrieval and Crowdsourcing Lab"
ADMIN_EMAIL = "anubrata@utexas.edu"
ADMINS = [(ADMIN_NAME, ADMIN_EMAIL), ]

WORKER_IRB_TEMPLATE = 'placeholder-irb-worker.html' # for your IRB agreement
REQUESTER_IRB_TEMPLATE = 'placeholder-irb-requester.html' # for your IRB agreement

HOSTNAME = 'https://fairwork-ut.herokuapp.com' # used as the hostname in emails sent by the system, since Django management commands do not know the server's hostname

# Activate Django-Heroku.
django_heroku.settings(locals())
