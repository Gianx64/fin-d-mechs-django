## TODO:
- Agenda para showappointments
- Implementar correos
- Poner diseño de fondo

Instalar Python + pip
https://youtu.be/rHux0gMZ3Eg

En cmd:
```
pip install pipenv
```

Crear proyectpo Django:
```
pipenv install django
```
```
pipenv shell
```
```
django-admin startproject (foldername) .
```

Crear migraciones:
```
python manage.py makemigrations
```
```
python manage.py migrate
```

Correr proyecto:
```
python manage.py runserver
```

Crear usuario administrador:
```
python manage.py createsuperuser
```

Crear app:
```
python manage.py startapp playground
```
(añadir 'playground' INSTALLED_APPS en settings.py)

1. models.py
    - Crear class Name(models.Model)
2. admin.py (para que salga en el panel de Administración)
    - from .models import Name
    - Registrar admin.site.register(Name)