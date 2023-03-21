# FastAPI Simple Blog

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