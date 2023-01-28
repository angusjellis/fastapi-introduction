# Example of a FastAPI application

## What is this repository?

This repository shows an example of a FastAPI CRUD API with JWT authentication.

Users can register, and then login, generating a JWT.

SSO is probably far simpler to implement than this!


## Commands

### Database commands

#### Spinning up the database

``` bash
docker compose up -d
```

#### Bringing database up to date

``` bash
alembic upgrade head
```

### Downgrading database to older version

``` bash
alembic downgrade <revision id>
```

### Generating a new migration file

``` bash
alembic revision --autogenerate -m <"message">
```

## Credit

Inspired by the code within [this repository](https://github.com/wpcodevo/python_fastapi).

It spins up an API with JWT auth, and gives you a way to set up users with usernames and passwords, hashing their passwords, etc.

It also allows you to verify users via email.

This original example serves as the inspiration for everything else in this repository.

