# 📘 Poetry API Book
An API developed with Django Rest Framework, from Backend Python course from EBAC.

This project can be found at: https://poetry-api-book.herokuapp.com/

## 📑 Prerequisites

```
Python 3.9.5
Poetry 1.1.14
Docker && Docker Compose
```

## 💻 Quickstart

1. Clone this project

   ```shell
   $ git clone git@github.com:brunomcr/poetry_api_book.git
   $ cd poetry_api_book/
   ```

2. Install dependencies:

   ```shell 
   $ poetry install
   ```

3. Create a structure in the database

   ```shell
   $ poetry run manage.py migrate
   ```
   
4. Run local dev server:

   ```shell
   $ poetry run python manage.py runserver
   ```
   
5. Run docker dev server environment:

   ```shell
   $ docker-compose up -d --build 
   $ docker-compose exec web python manage.py migrate
   ```

6. Run tests inside of docker:

   ```shell
   $ docker-compose exec web python manage.py test
   ```

## ⚙️Deploy to Heroku with Docker:

Config.:
```shell
  SECRET_KEY:
    $ heroku config:set SECRET_KEY="<scretKey>" -a <herokuAppName>
    <scretKey> can be generate in: https://djecrety.ir/

  HEROKU_API_KEY heroku auth:
    $ heroku stack:set container -a <herokuAppName>
    $ heroku push heroku main:main
```
