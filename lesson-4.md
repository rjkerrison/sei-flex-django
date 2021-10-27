# Lesson 4

Led by [Tristan](https://github.com/TrimHall)!

- [Lesson 4](#lesson-4)
  - [Overview](#overview)
  - [SQL Intro: A Murder Mystery](#sql-intro-a-murder-mystery)
    - [Finding the killer](#finding-the-killer)
    - [Finding the true culprit](#finding-the-true-culprit)
  - [Using Postgresql in Django](#using-postgresql-in-django)
    - [Local Postgresql](#local-postgresql)
      - [Create a database](#create-a-database)
      - [Django configuration](#django-configuration)
  - [Full deploy](#full-deploy)
    - [Dependenices](#dependenices)
    - [Configuration](#configuration)
    - [Heroku deploy for the code](#heroku-deploy-for-the-code)
    - [Adding postgres](#adding-postgres)
    - [Syncing databases](#syncing-databases)
    - [Finally: deploying](#finally-deploying)
  - [Example](#example)

## Overview

The main goal of Lesson 4 is to replace our crumby _db.sqlite3_ file with a real-life database.

As a bonus, let's get our API available in the cloud.

## SQL Intro: A Murder Mystery

As an intro to SQL, we'll go through the [KnightLab SQL Mystery](https://mystery.knightlab.com/).

Start with what you know, investigate further by looking up table schemas.

Make notes of pertinent details along the way.

1. Find murders on the given date
2. Use addresses to find people
3. Use people to find interviews
4. Use interviews to find clues
5. Investigate those clues with other tables
6. As you get deeper, use `join` to keep contextual information available

### Finding the killer

There's a fair few steps to this, but one of the big clues was in finding a gym checkin.

```SQL
select ci.*, p.name from get_fit_now_check_in ci
join get_fit_now_member m on ci.membership_id = m.id
join person p on p.id = m.person_id
where ci.check_in_date = '20180109'
```

### Finding the true culprit

The first step for finding the true culprit is to check the interview.

```SQL
select i.* from interview i
join person p on p.id = i.person_id
where p.name = 'Jeremy Bowers';
```

It's possible to be a little more precise with this, as we're given enough info, but this works out too.

```SQL
select g.name, d.hair_color, d.car_model, d.car_make
from (
    select p.id, p.name, p.license_id, count(f.date) as event_count
    from person p
    join facebook_event_checkin f on f.person_id = p.id
    where f.date between '20171201' and '20171231'
    group by p.id
) g
join drivers_license d on d.id = g.license_id
where g.event_count >= 3;
```

## Using Postgresql in Django

We have two reasonable options when using Django and a database.

1. Local
2. Cloud

Local is great for development, although it sucks in production.
Let's get started with it.

### Local Postgresql

First, we need a postgresql client.

```sh
brew install postgresql
```

Congratulations, this is the 1000th brew instalation of the course.

To start postgresql, run

```sh
brew services start postgresql
```

If this looks familiar, it's because we did the same thing to start the mongodb service.

When you've got this working, you can check your postgres config with `pg_config`.
It should return what looks like a lot of environment variables (which is exactly what it is).

#### Create a database

We need to create a database – so far, we've only installed a client.

```sh
createdb ga-tunes
```

It's weirdly easy. See [Postgresql Documentation 1.3 Creating a Database](https://www.postgresql.org/docs/14/tutorial-createdb.html) for more.

#### Django configuration

To get us ready to use postgresql,
you have to install the Python postgresql package, which is called `psycopg2`.

```sh
pipenv install psycopg2
```

There's a few further steps to get Django to use our postgresql database.

1. `settings.py` needs to point to the postgresql host

   ```py
   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.postgresql_psycopg2",
           "NAME": "ga-tunes",
           "HOST": "localhost",
           "PORT": 5432,
       }
   }
   ```

2. Run the migrations: your new database knows nothing of your schemas so far.

   ```sh
   python manage.py migrate
   ```

   This is one of the reasons migrations are so useful.
   Creating new local databases that mirror production is very simple.
   Perfect for when you're onboarding new developers to your team.

3. Recreate superusers. They don't exist in your new database.

   ```sh
   python manage.py createsuperuser
   ```

4. Go ahead and `python manage.py runserver`.

Now you'll have to recreate all the albums etc via Postman or via the Admin site.

You can also access the database using `psql`.
You can then query the database using SQL.

```sh
sh-3.2$ psql ga-tunes
psql (14.0)
Type "help" for help.

ga-tunes=# select * from albums_album
ga-tunes-# ;
 id | title | cover_image | artist_id
----+-------+-------------+-----------
(0 rows)

ga-tunes=#
```

There are some handy things you can do like viewing all tables with the `\dt` command.

```sh
ga-tunes=# \dt
                  List of relations
 Schema |            Name            | Type  | Owner
--------+----------------------------+-------+-------
 public | albums_album               | table | rjk
 public | artists_artist             | table | rjk
 public | artists_artist_members     | table | rjk
 public | artists_member             | table | rjk
 public | auth_group                 | table | rjk
 public | auth_group_permissions     | table | rjk
 public | auth_permission            | table | rjk
 public | auth_user                  | table | rjk
 public | auth_user_groups           | table | rjk
 public | auth_user_user_permissions | table | rjk
 public | django_admin_log           | table | rjk
 public | django_content_type        | table | rjk
 public | django_migrations          | table | rjk
 public | django_session             | table | rjk
(14 rows)
```

Find out more about this kind of thing on the
[postgresql tutorial's show tables](https://www.postgresqltutorial.com/postgresql-show-tables/) explainer.

## Full deploy

Let's take a look at how to put our backend online.

### Dependenices

Throughout these steps, there's going to be a few python packages we'll need.
Let's install them all now!

```sh
pipenv install pytz dj_database_url gunicorn whitenoise
```

### Configuration

Before we deploy, we need to have a few settings ready in our `settings.py`:

```py
# Location where django collect all static files
STATIC_ROOT = os.path.join(BASE_DIR, "static")

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES["default"].update(db_from_env)
```

and you'll likely need to `import dj_database_url` and `import os` at the top of the file if you haven't already.

You also need to change the `ALLOWED_HOSTS` to include your app, e.g.

```py
ALLOWED_HOSTS = [
    "afternoon-forest-14959.herokuapp.com",
    "0.0.0.0",
]
```

Django also doesn't support production fileserving,
so to cover this, we have some whitenoise settings to add.

```py
MIDDLEWARE = [
    ...,
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### Heroku deploy for the code

If you haven't already, you'll need to set up Heroku.

1. Sign up for an account at [heroku.com](https://heroku.com)
2. Install the heroku CLI
   ```sh
   brew install heroku/brew/heroku
   ```
3. Login on the CLI
   ```sh
   heroku login
   ```
   and follow the instructions.

With all that done, you're ready to deploy.

```sh
heroku create <your-app-name>
```

will create the app for you.
If you don't provide a name, heroku will give it a random one.

You can view your heroku apps from the command line with `heroku apps` or by going to the [Heroku dashboard](https://dashboard.heroku.com/).

### Adding postgres

We're going to create the postgresql addon,
and then grab the newly created database URL from the config.

```sh
heroku addons:create heroku-postgresql:hobby-dev
heroku config -s | grep DATABASE_URL
```

Keep that URL handy.

Or run

```sh
heroku pg:info
```

the last line should tell you your postgresql addon name,
e.g. `postgresql-pointy-43826`.

### Syncing databases

To push your local databases to your heroku postgres, run e.g.

```sh
PGUSER= PGPASSWORD= heroku pg:push postgres://localhost/ga-tunes postgresql-pointy-43826
```

Remember to use your own app name in the end.

### Finally: deploying

With all that done, we're one step away.

Create the Procfile as we have here, i.e.

```
web:  gunicorn api.wsgi
```

The `Procfile` tells Heroku what to run once we've deployed.

Now to deploy, simply run

```sh
git push heroku main:main
```

Git is your deployment tool!

Run `heroku open` to view the deployed site!

## Example

An example is available at [https://afternoon-forest-14959.herokuapp.com/admin/](https://afternoon-forest-14959.herokuapp.com/admin/) etc.
