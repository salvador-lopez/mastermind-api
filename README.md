# Mastermind API

This is an approach to Django 2.0+ API project in DDD implemented with Hexagonal Architecture.

## Features
- Python 3.6
- Django 2.0+
- Sqlite3
- DDD
- Hexagonal Architecture

## How to install

```bash
$ git clone https://github.com/salvador-lopez/mastermind-api.git
$ python3 manage.py makemigrations games
$ python3 manage.py migrate
$ python3 manage.py loaddata game_code_pegs
$ python3 manage.py runserver
```

## API DOC
[Postman API DOC](https://documenter.getpostman.com/view/602699/mastermindapi/7LjDkB1)

## REQUIREMENTS
- Python 3.6

## TODO:
- Use [Pipenv](https://github.com/kennethreitz/pipenv) - the officially recommended Python packaging tool from Python.org.
- Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org).
- Some API doc like [Swagger](https://swagger.io/swagger-ui/)
- Create a users system with board and codemaker user roles.
