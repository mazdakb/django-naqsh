Django Naqsh
=======================

.. image:: https://travis-ci.com/mazdakb/django-naqsh.svg?branch=master
    :target: https://travis-ci.com/mazdakb/django-naqsh

.. image:: https://readthedocs.org/projects/django-naqsh/badge/?version=latest
    :target: http://django-naqsh.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


Powered by Cookiecutter_, Django Naqsh is a bootstrapping tool for creating
production-ready Django web services quickly.

* Documentation: https://django-naqsh.readthedocs.io/en/latest/
* See Troubleshooting_ for common errors and obstacles
* If you have problems with Django Naqsh, please open issues_ don't send
  emails to the maintainers.
* Need quick professional paid support? Contact `support@cookiecutter.io`_.
  This includes configuring your servers, fixing bugs, reviewing your code and
  everything in between.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

.. _Troubleshooting: https://django-naqsh.readthedocs.io/en/latest/troubleshooting.html

.. _issues: https://github.com/mazdakb/django-naqsh/issues/new
.. _support@cookiecutter.io: support@cookiecutter.io

Features
---------

* For Django 2.0
* Python 3.6 compatible
* 12-Factor_ based settings via django-environ_
* Secure by default. We believe in SSL.
* Optimized development and production settings
* Comes with custom accounts app ready to go
* Send emails via Anymail_ (using Mailgun_ by default, but switchable)
* Media storage using Amazon S3
* Docker support using docker-compose_ for development and production (using Caddy_ with LetsEncrypt_ support)
* Procfile_ for deploying to Heroku
* Run tests with unittest or py.test
* Customizable PostgreSQL version


Optional Integrations
---------------------

*These features can be enabled during initial project setup.*

* Serve static files from Amazon S3 or Whitenoise_
* Configuration for Celery_
* Integration with MailHog_ for local email testing
* Integration with Sentry_ for error logging

.. _django-environ: https://github.com/joke2k/django-environ
.. _12-Factor: http://12factor.net/
.. _Procfile: https://devcenter.heroku.com/articles/procfile
.. _Mailgun: http://www.mailgun.com/
.. _Whitenoise: https://whitenoise.readthedocs.io/
.. _Celery: http://www.celeryproject.org/
.. _Anymail: https://github.com/anymail/django-anymail
.. _MailHog: https://github.com/mailhog/MailHog
.. _Sentry: https://sentry.io/welcome/
.. _docker-compose: https://github.com/docker/compose
.. _PythonAnywhere: https://www.pythonanywhere.com/
.. _Caddy: https://caddyserver.com/
.. _LetsEncrypt: https://letsencrypt.org/

Constraints
-----------

* Only maintained 3rd party libraries are used.
* Uses PostgreSQL everywhere (9.2+)
* Environment variables for configuration (This won't work with Apache/mod_wsgi except on AWS ELB).

Support this Project!
----------------------

This project is run by volunteers. Please support them in their efforts to maintain and improve Django Naqsh:

* You can donate Ethereum to this account: 0x4753B709fb7ee19B32Dc7e84aa9ca86288bf543F

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
    email [you@example.com]: mazdakb@gmail.com
    description [A short description of the project.]: A reddit clone.
    domain_name [example.com]: myreddit.com
    version [0.1.0]: 0.0.1
    timezone [UTC]: Asia/Tehran
    use_whitenoise [y]: n
    use_celery [n]: y
    use_mailhog [n]: n
    use_sentry [y]: y
    use_pycharm [n]: y
    windows [n]: n
    use_docker [y]: n
    use_heroku [n]: y
    Select postgresql_version:
    1 - 10.3
    2 - 10.2
    3 - 10.1
    4 - 9.6
    5 - 9.5
    6 - 9.4
    7 - 9.3
    Choose from 1, 2, 3, 4 [1]: 1
    Select open_source_license:
    1 - MIT
    2 - BSD
    3 - GPLv3
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]: 1
    use_grappelli: y
    keep_local_envs_in_vcs [y]: y

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

* Have questions? **Before you ask questions anywhere else**, please post your question on `Stack Overflow`_ under the *django-naqsh* tag. We check there periodically for questions.
* If you think you found a bug or want to request a feature, please open an issue_.
* For anything else, you can chat with us on `Gitter`_.

.. _`Stack Overflow`: http://stackoverflow.com/questions/tagged/django-naqsh
.. _`issue`: https://github.com/mazdakb/django-naqsh/issues

Releases
--------

Need a stable release? You can find them at https://github.com/mazdakb/django-naqsh/releases


Code of Conduct
---------------

Everyone interacting in the Cookiecutter project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.


.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/
