Install Python + pip

Django course for begginners: https://youtu.be/rHux0gMZ3Eg

cmd:
```
pip install pipenv
```

Create Django proyect:
```
pipenv install django
```
```
pipenv shell
```
```
django-admin startproject (foldername) .
```

Create migrations:
```
python manage.py makemigrations
```
```
python manage.py migrate
```

Run proyect:
```
python manage.py runserver
```

Create superuser (admin panel):
```
python manage.py createsuperuser
```

Create app:
```
python manage.py startapp appname
```
(add 'appname' in INSTALLED_APPS on settings.py)