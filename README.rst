Django Naqsh
============

.. image:: https://travis-ci.com/mazdakb/django-naqsh.svg?branch=master
    :target: https://travis-ci.com/mazdakb/django-naqsh
    :alt: Build Status

.. image:: https://readthedocs.org/projects/django-naqsh/badge/?version=latest
    :target: http://django-naqsh.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://pyup.io/repos/github/mazdakb/django-naqsh/shield.svg
    :target: https://pyup.io/repos/github/mazdakb/django-naqsh/
    :alt: Updates

.. image:: https://www.codetriage.com/mazdakb/django-naqsh/badges/users.svg
    :target: https://www.codetriage.com/mazdakb/django-naqsh
    :alt: Code Helpers Badge

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
    :alt: Code style: black

Powered by Cookiecutter_, Django Naqsh is a bootstrapping tool for creating
production-ready Django web services quickly.

This project is a fork of `django-naqsh`_ that is intended to be used as a REST API backend.
Unnecessary modules for a REST API and codes are removed and custom User model is more developed.

* Documentation: https://django-naqsh.readthedocs.io/en/latest/
* See Troubleshooting_ for common errors and obstacles
* If you have problems with Django Naqsh, please open issues_ don't send
  emails to the maintainers.

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _django-naqsh: https://github.com/mazdakb/django-naqsh
.. _Troubleshooting: https://django-naqsh.readthedocs.io/en/latest/troubleshooting.html
.. _issues: https://github.com/mazdakb/django-naqsh/issues/new

Features
---------

* For Django 2.2
* Works with Python 3.7
* Renders Django projects with 100% starting test coverage
* 12-Factor_ based settings via django-environ_
* Secure by default with SSL enabled.
* Optimized development and production settings
* Comes with custom user model with secure token authentication and email validation for RESTful API
* Send emails via Anymail_ (using Mailgun_ by default, but switchable)
* Media storage using Amazon S3, Google Cloud Storage or Minio_
* Docker support using docker-compose_ for development and production (using Traefik_ with LetsEncrypt_ support)
* Procfile_ for deploying to Heroku
* Run tests with unittest or pytest
* Customizable PostgreSQL version

Optional Integrations
---------------------

*These features can be enabled during initial project setup.*

* Serve static files from Amazon S3, Google Cloud Storage, Minio_ or Whitenoise_
* Configuration for Celery_ and Flower_ (the latter in Docker setup only)
* Integration with MailHog_ for local email testing
* Integration with Sentry_ for error logging

.. _django-environ: https://github.com/joke2k/django-environ
.. _12-Factor: http://12factor.net/
.. _Procfile: https://devcenter.heroku.com/articles/procfile
.. _Mailgun: http://www.mailgun.com/
.. _Minio: https://min.io/
.. _Whitenoise: https://whitenoise.readthedocs.io/
.. _Celery: http://www.celeryproject.org/
.. _Flower: https://github.com/mher/flower
.. _Anymail: https://github.com/anymail/django-anymail
.. _MailHog: https://github.com/mailhog/MailHog
.. _Sentry: https://sentry.io/welcome/
.. _docker-compose: https://github.com/docker/compose
.. _Traefik: https://traefik.io/
.. _LetsEncrypt: https://letsencrypt.org/

Constraints
-----------

* Only maintained 3rd party libraries are used.
* Uses PostgreSQL everywhere (9.4 - 11.3)
* Environment variables for configuration (This won't work with Apache/mod_wsgi).

pyup
~~~~~~~~~~~~~~~~~~

.. image:: https://pyup.io/static/images/logo.png
   :name: pyup
   :align: center
   :alt: pyup
   :target: https://pyup.io/

Pyup brings you automated security and dependency updates used by Google and other organizations. Free for open source projects!

Usage
------

Let's pretend you want to create a Django project called "redditclone". Rather than using ``startproject``
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter_ to do all the work.

First, get Cookiecutter. Trust me, it's awesome::

    $ pip install "cookiecutter>=1.4.0"

Now run it against this repo::

    $ cookiecutter https://github.com/mazdakb/django-naqsh

You'll be prompted for some values. Provide them, then a Django project will be created for you.

**Warning**: After this point, change 'Mazdak Badakhshan', 'mazdakb', etc to your own information.

Answer the prompts with your own desired options_. For example::

    Cloning into 'django-naqsh'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.
    project_name [Project Name]: Reddit Clone
    project_slug [reddit_clone]: reddit
    author_name [Mazdak Badakhshan]: Mazdak Badakhshan
    email [you@example.com]: geraneum@example.com
    description [Behold My Awesome Project!]: A reddit clone.
    domain_name [example.com]: myreddit.example.com
    version [0.1.0]: 0.0.1
    timezone [UTC]: Europe/Berlin
    use_whitenoise [n]: n
    use_celery [n]: y
    use_mailhog [n]: n
    use_sentry [n]: y
    use_pycharm [n]: y
    windows [n]: n
    use_docker [n]: n
    use_heroku [n]: y
    use_compressor [n]: y
    Select postgresql_version:
    1 - 11.5
    2 - 10.10
    3 - 9.6
    4 - 9.5
    5 - 9.4
    Choose from 1, 2, 3, 4, 5 [1]: 1
    Select cloud_provider:
    1 - AWS
    2 - GCP
    3 - None
    Choose from 1, 2, 3 [1]: 1
    Select open_source_license:
    1 - MIT
    2 - BSD
    3 - GPLv3
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]: 1
    use_grappelli [y]: y
    use_cors_package [y]: y
    keep_local_envs_in_vcs [y]: y
    debug[n]: n

Enter the project and take a look around::

    $ cd reddit/
    $ ls

Create a git repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first awesome commit"
    $ git remote add origin git@github.com:mazdakb/redditclone.git
    $ git push -u origin master

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?

For local development, see the following:

* `Developing locally`_
* `Developing locally using docker`_

.. _options: http://django-naqsh.readthedocs.io/en/latest/project-generation-options.html
.. _`Developing locally`: http://django-naqsh.readthedocs.io/en/latest/developing-locally.html
.. _`Developing locally using docker`: http://django-naqsh.readthedocs.io/en/latest/developing-locally-docker.html

Community
-----------

* Have questions? **Before you ask questions anywhere else**, please post your question on `Stack Overflow`_ under *django-naqsh* or *cookiecutter-django* tags. We check there periodically for questions.
* If you think you found a bug or want to request a feature, please open an issue_.

.. _`Stack Overflow`: http://stackoverflow.com/questions/tagged/django-naqsh
.. _`issue`: https://github.com/mazdakb/django-naqsh/issues

For pyup.io Users
-----------------

If you are using `pyup.io`_ to keep your dependencies updated and secure, use the code *cookiecutter* during checkout to get 15% off every month.

.. _`pyup.io`: https://pyup.io

"Your Stuff"
-------------

Scattered throughout the project are places marked with "your stuff". This is where third-party libraries are to be integrated with your project.

Releases
--------

Need a stable release? You can find them at https://github.com/mazdakb/django-naqsh/releases


Not Exactly What You Want?
---------------------------

This is what I want. *It might not be what you want.* Don't worry, you have options:

Fork This
~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this to create your own version.
Once you have your fork working, let me know and I'll add it to a '*Similar Cookiecutter Templates*' list here.
It's up to you whether or not to rename your fork.

If you do rename your fork, I encourage you to submit it to the following places:

* cookiecutter_ so it gets listed in the README as a template.
* The cookiecutter grid_ on Django Packages.

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _grid: https://www.djangopackages.com/grids/g/cookiecutters/

Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~

We accept pull requests if they're small, atomic, and make our own project development
experience better.

Articles
---------

You may find some materials refered in the `cookiecutter-django's articles`_.

.. _`cookiecutter-django's articles`: https://github.com/pydanny/cookiecutter-django#articles

Code of Conduct
---------------

Everyone interacting in the Cookiecutter project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.


.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/
