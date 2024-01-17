# Project documentation
This is an API that will be used as a backend application. It's built using Django RestFramework with PostgreSQL as Database.
It is called the `Fedal` API. The name Fedal comes from the name of the two greatest tennis players, Federer and Nadal.

## Table of contents

- [Getting started](#getting-started)
  - [Components & Settings](#components)
  - [Environment variables](#environment-variables)
  - [Development environment](#development)
  - [Production environment](#production)
  - [Requirements](#requirements)
  - [Pre-commit hooks](#pre-commit-hooks)
  - [Handy Docker Commands](#handy-docker-commands)

# Getting started

## Components & Settings

The application exists of several component services required for the API to run.
- Django Rest Framework
- PostgreSQL
- PGAdmin
- Redis
- Redis-commander
- Celery (Celery-beat, Flower)
- nginx (only on production)

The components are defined in the docker-compose files of dev or pro.

The default Django settings file setting is `api.settings` (set in `manage.py`, `wsgi.py`, `asgi.py`, and `celery.py`).

This can be overriden by setting the `DJANGO_SETTINGS_MODULE` environment variable, for instance, if you'd like to use your own local settings file, use:

    export DJANGO_SETTINGS_MODULE=api.local_settings

> NOTE: When testing, make sure you use `api.test_settings` in order for it to work properly and to avoid calling any third party API's unnecessarily.

[top](#table-of-contents)

## Environment variables

Before running the application, the .env file has to be created in the root directory of the project. The below variable are expected to be set:

 POSTGRES_USER
 POSTGRES_PASSWORD
 POSTGRES_HOST
 POSTGRES_PORT
 POSTGRES_DB
 PGADMIN_DEFAULT_EMAIL
 PGADMIN_DEFAULT_PASSWORD
 PGADMIN_LISTEN_PORT
 ENVIRONMENT
 SECRET_KEY

[top](#table-of-contents)

## Development environment

To run the application on the development environment using docker-compose-dev.yml. The below command will install the application and images, setup the containers and local netowrk.
    docker-compose -f docker-compose-dev.yml --build up

[top](#table-of-contents)

## Production environment

To run the application on the production environment using docker-compose-pro.yml. The below command will build and run the application and images, setup the containers and local netowrk.
    docker-compose -f docker-compose-pro.yml --build --remove-orphans -d up

[top](#table-of-contents)

## Requirements
The requirements.txt file contains all the required packages to be installed.

## Pre-commit hooks
Consider [installing pre-commit](https://pre-commit.com/#installation), which will format your code according to our style guide with every commit. 🤓

[top](#table-of-contents)

## Handy Docker Commands

Tail logs with:

    docker logs -f CONTAINERNAME

Start a bash shell in the Django container with:

    docker exec -it CONTAINERNAME bash

Create a superuser with:

    docker exec -it CONTAINERNAME python ./manage.py createsuperuser

Start a Django IDE shell with:

    docker exec -it CONTAINERNAME python ./manage.py shell

Run the Django migrate command with:

    docker exec -it CONTAINERNAME python ./manage.py migrate

Run the Django collectstatic command with:

    docker exec -it CONTAINERNAME python ./manage.py collectstatic --no-input

Start a postgresql shell from within the postgresql container:

    docker exec -it CONTAINERNAME psql -U USER DB
