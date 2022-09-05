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

#### Deploy to Heroku with Docker:
* Config:
  * SECRET_KEY: `heroku config:set SECRET_KEY="<scretKey>" -a <herokuAppName>`
    * **scretKey**, can be generate in: https://djecrety.ir/
  * `heroku stack:set container -a <herokuAppName>`
  * `heroku push heroku main:main`

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
