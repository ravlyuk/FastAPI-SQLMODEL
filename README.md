# FastAPI Simple Blog

## About project:

Simple Blog with components:

- posts
- likes/dislikes
- statistic
- activity
- users
- auth JWT token

Important! The docker image will not be created if it contains invalid code by the Flake8 validator.

### Used libs:

- fastapi
- fastapi-users-db-sqlmodel
- alembic

Steps to run project on dev's machine:
------------------------------

1) Use python 3.11
2) clone repo
3) `python3 -m venv .venv`
4) `. ./.venv/bin/activate`
5) `pip install -U pip && pip install -r requirements.txt`
6) `pip install make`
7) `make init` init migration, ONLY for first run
8) `make migrate`
9) `make upgrade`
10) `fab run`

### Test API:

http://0.0.0.0:8004/docs

or use postman collection `postman_collection.json`