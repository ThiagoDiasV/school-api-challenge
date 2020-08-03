[![codecov](https://codecov.io/gh/ThiagoDiasV/school-api-challenge/branch/master/graph/badge.svg)](https://codecov.io/gh/ThiagoDiasV/school-api-challenge) [![Build Status](https://travis-ci.com/ThiagoDiasV/school-api-challenge.svg?branch=master)](https://travis-ci.com/ThiagoDiasV/school-api-challenge)

# School API Challenge

## Install and run

### Using Dockerfile and docker-compose

First you need to init a daemon with dockerd, so run dockerd:

    $ dockerd

OR

    $ sudo dockerd

And then with Docker and docker-compose, run:

    $ docker-compose up --build

This command above will: 
- Create and migrate database 
- Run unit tests
- Run server

Now you will be able to navigate through the School API at localhost:8000.

### Using local Python 3.8

Prefer to create a Python virtual environment and then

    (venv) $  pip install -r requirements.txt

After installing requirements run:

    (venv) $ python manage.py migrate
    (venv) $ python manage.py runserver

The API will be available at localhost:8000

## Run the tests

You can cover School API with unit tests running:

### Using Docker

    $ docker-compose exec web pytest

### Using Python 3.8

    (venv) $ pytest

# Rest API

The Rest API is described below

## Endpoints

    /estudantes/
    /estudantes/{id}/
    /materias-escolares/
    /materias-escolares/{id}/
    /estudantes-materias/
    /estudantes-materias/{id}/
    /estudantes-aprovacao/
    /estudantes-aprovacao/{id}/

## API documentation endpoints

In these endpoints it's possible to user two UI's to interate with School API

    /openapi/swagger/
    /openapi/redoc/
