# poetry_book
A project started with Poetry and developed with Django Rest Framework, Docker, CI / CD

#### Tools
* Poetry
* Black

#### App's
* python 
* pytest 
* factory-boy 
* Django 
* djangorestframework
* Faker
* pytest-django
* django-extensions 
* .env
* docker
* docker-compose
* Heroku


### Quick Start
#### Poetry
* `poetry install` 
* `poetry run manage.py migrate`
* `poetry run manage.py runserver` 
#### Docker Compose
* `docker-compose up -d --build` 
* `docker-compose exec web python manage.py migrate`
#### Test
* `docker-compose exec web python manage.py test`
