# Lesson 5

Led by [Tristan](https://github.com/TrimHall)!

- [Lesson 5](#lesson-5)
  - [Overview](#overview)
  - [Test Driven Development](#test-driven-development)
    - [Writing passing code](#writing-passing-code)

## Overview

The main goal of Lesson 5 is to upgrade our endpoints to be more useful by accepting natural data.

Currently, when we create new bands, we have to make a request to add each band member,
then an extra one to create the band.

That's an awful lot of noise! We can do much better.

## Test Driven Development

_Test Driven Development_ is the idea that we can write tests that describe _what_
we want our code to do before we even think about _how_ to do it.

If you wanted to build a calculator, you could define some tests for it before you write even a single line of code:

- 55 plus 89 should be 144
- 3 times 3 should be 9
- Square root 225 should be 15

With Python, as with many programming languages, we can write such tests as code.

Take a look at `AlbumTests.test_create_album` in `albums/tests.py`.

We can run that test (and any others we might have) with `python manage.py test`.
Right now, it's failing where it checks the artist — but the goal is to get it to pass!

### Writing passing code

Now that we have a test which is failing, we only have one job:
write code to make it pass!
