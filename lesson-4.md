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

## Overview

The main goal of Lesson 4 is to replace our crumby _db.sqlite3_ file with a real-life database.

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
