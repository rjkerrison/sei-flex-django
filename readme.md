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

## Running your Django api

You can run your Django app with `python manage.py runserver`.
The first time you do this, you will receive a warning like below:

> _You have 18 unapplied migration(s).
> Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
> Run 'python manage.py migrate' to apply them._

This is your first intro to _migrations_.

### What's a _migration_?

Whenever you work with databases in Django, it checks that the database schema matches the model schemas.
It can determine whether the database needs to be "migrated" — which means having its schema updated.

Other platforms such as _Ruby on Rails_ use the same philosophy to ensure that server code and database are compatible.

Do as you're told by the message, and run

```sh
python manage.py migrate
```

This should tell you that 18 migrations have run "OK."

```sh
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

### Where's the database?

We didn't create a database! Previously, we've run mongodb, but here we didn't do any such thing.

By default, Django is using a file-based database called _sqlite_.
It has created your database in a file at `db.sqlite3`.
This is less than ideal — there's no way that reading and writing to a single file is going to be fast enough on a production environment with multiple users.

We'll fix this soon.

### Seeing the result

Once you've run the migrations, you can run

> python manage.py runserver

again. This time, it'll allow you to view you Django app in the browser, by default at http://localhost:8000/.

## The admin app

Django comes with a whole admin user section to the site pre-built. To log in we first need to create a user, which we can do like so:

```
python manage.py createsuperuser
```

This will run through the setting up a super user, a user that has access to the admin section of the site, and one that can make changes to the database contents.

You can choose anything here, but we would recommend the following:

```
Username: admin
Email: admin@ga.co
Password: admin
Password (again): admin
Bypass password validation and create user anyway? [y/N]: y
```

You should now be able to log in to the admin section of the site by navigating to http://localhost:8000/admin/

![Django Admin Dashboard](https://media.git.generalassemb.ly/user/15120/files/5e7fa380-c8e5-11e9-83e2-1db09ddad88a)

Here you can add new users, and groups: collections of users that have the same permissions.

We'll be looking at this again later in the module, but for now, let's log out.

[Next: lesson-2](./lesson-2.md)
