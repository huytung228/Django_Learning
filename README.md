# Django Basic Flow
## Start new project
django-admin startproject name [directory]
## Create new apps
python manage.py startapp [name]
## Add new apps nam to setting.py in:
INSTALLED_APPS = []
## Add urls of new apps to urls.py in base app with 'include'
## Create views in views.py at child apps
## Add views to paths
## Start server
python manage.py rumserver
## Create database from models
python manage.py makemigrations
python manage.py migrate
