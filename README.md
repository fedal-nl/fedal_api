# Project documentation <!-- omit in toc -->
This is the main API that will be used for all the backend applications. It is a Django project that uses Django Rest Framework for the API endpoints. PostgreSQL is used as the database and Redis for caching.
---


## Table of contents

- [Getting started](#getting-started)

---

# Getting started
Clone the application from the repository and create the .env file in the root directory. The .env file should contain the following variables:

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
    ADMIN_PASSWORD
    USER_OMAR_PASSWORD

run the following command to start the application:

    docker-compose up

> NOTE: `docker-compose.yml` port numbers and container names are changeable.

