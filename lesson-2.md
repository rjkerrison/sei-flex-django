# Lesson 2: Django "apps"

Now let's run

```sh
django-admin startapp albums
```

This will start us up an _app_, a small self-contained unit of models and logic that work together.
A less confusing term would be a _module_.

They can be ported and reused in different projects.

## Using an "app"/module

In order to use the app in our project, we have to reference it.

For this, we make a change to `settings.py` so that `albums` is counted among its `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "albums",
]
```

## Creating a model

Right now, `albums` is useless.
Take a look at the models and views: there's nothing there.

Let's add a model.

```python
class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    cover_image = models.CharField(max_length=200)
```

We have some fields, all of them strings!

What do we do now? Same thing we do every time,

```sh
python manage.py runserver
```

And guess what?
