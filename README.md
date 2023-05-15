# Django weather app

## Overview
This is backend service, which can help you to track the weather in different cities

## Stack

+ Python 3.10
+ Django 4.2
+ PostgreSQL
+ Docker
  
## Preparation

You need to have: 
+ PostgreSQL account
+ Python 3.10 +

Create a postgres server database

## Install & Run

### Run with Docker

**Copy repository**
```shell
git clone https://github.com/YaArtem333/Django-weather-app.git
```

**Change database parameters**

1) Open file weatherapp/settings.py
2) Find DATABASES dict and set parameters:
   ```python
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'weathdb', # Enter the name of your database instead of 'weathdb'
        'USER': 'postgres', #Enter your username instead of 'postgres'
        'PASSWORD': 'password', # Enter your password instead of 'password'
        'HOST': 'db',
        'PORT': '5432'
        }
    }
    ```

**Change docker-compose file**

Open ***docker-compose.yml*** file and set parameters:
```yml
    POSTGRES_USER: user # Your username
    POSTGRES_PASSWORD: password # Your password
    POSTGRES_DB: weathdb # The name of your database
```

**Create and run docker container**
```shell
docker-compose up
```
The service is available on 127.0.0.1:8000

### Run on your computer ###

**Copy repository**
```shell
git clone https://github.com/YaArtem333/Django-weather-app.git
```

**Install libraries**
```shell
pip install django
```
```shell
pip install psycopg2
```
```shell
pip install requests
```

**Change database parameters**

1) Open file weatherapp/settings.py
2) Find DATABASES dict and set parameters:
   ```python
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'weathdb', # Enter the name of your database instead of 'weathdb'
        'USER': 'postgres', #Enter your username instead of 'postgres'
        'PASSWORD': 'password', # Enter your password instead of 'password'
        'HOST': 'db', # Enter 'localhost' instead of 'db'
        'PORT': '5432'
        }
    }
    ```

**Run your server with database**

**Make migrations**

Go to the folder with ***manage.py*** file and write commands
```shell
python manage.py makemigrations
```
```shell
python manage.py migrate
```

**Run app**

Go to the folder with ***manage.py*** file and write command
```shell
python manage.py runserver
```

The service is available
