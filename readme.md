# Django App

Django is a framework for creating web servers using Python.

Its principles lie in Models, Templates, and Views.

Django handles the management of the database as well as serving data.

## Initial steps

1. Install python
2. Ensure that `python --version` is `3.*.*` — if not, add an alias: `alias python=python3` and check again.
3. Install `pipenv`: `python -m pip install pipenv`
4. Make a new repository which will have your django app in it
5. Inside your repo, install `django` in a virtual environment: `pipenv install django`. This will create two files: `Pipfile` and `Pipfile.lock`. Commit them as your initial first commit.
6. Add a `readme.md`!

## Starting your Django api

1. Start up a pipenv shell with `pipenv shell`
2. Create your django app with `django-admin startproject api .`. This will create `manage.py` and a new folder `api` filled with python scripts as the starter for your django app. Commit the new files.
