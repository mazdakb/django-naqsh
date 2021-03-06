Django Naqsh
============

.. image:: https://readthedocs.org/projects/django-naqsh/badge/?version=latest
    :target: http://django-naqsh.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://www.codetriage.com/mazdakb/django-naqsh/badges/users.svg
    :target: https://www.codetriage.com/mazdakb/django-naqsh
    :alt: Code Helpers Badge

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
    :alt: Code style: black

Powered by Cookiecutter_, Django Naqsh is a bootstrapping tool for creating
production-ready Django web services quickly.

This project is a fork of `cookiecutter-django`_ that is intended to be used as a REST API backend.
Unnecessary modules for a REST API and codes are removed or otherwise enhanced.

* Documentation: https://django-naqsh.readthedocs.io/en/latest/
* See Troubleshooting_ for common errors and obstacles
* If you have problems with Django Naqsh, please open issues_ don't send
  emails to the maintainers.

.. _cookiecutter-django: https://github.com/pydanny/cookiecutter-django
.. _Troubleshooting: https://django-naqsh.readthedocs.io/en/latest/troubleshooting.html
.. _issues: https://github.com/mazdakb/django-naqsh/issues/new

Features
---------

* For Django 3.1
* Works with Python 3.8
* 12-Factor_ based settings via django-environ_
* Secure by default. We believe in SSL.
* Optimized development and production settings
* Comes with custom user model
* Optional basic ASGI setup for Websockets
* Send emails via Anymail_ (using Mailgun_ by default, but switchable)
* Media storage using Amazon S3 or Google Cloud Storage
* Docker support using docker-compose_ for development and production (using Traefik_ with LetsEncrypt_ support)
* Procfile_ for deploying to Heroku
* Instructions for deploying to PythonAnywhere_
* Run tests with unittest or pytest
* Customizable PostgreSQL version
* Default integration with pre-commit_ for identifying simple issues before submission to code review

Optional Integrations
---------------------

*These features can be enabled during initial project setup.*

* Serve static files from Amazon S3, Google Cloud Storage or Whitenoise_
* Configuration for Celery_ and Flower_ (the latter in Docker setup only)
* Integration with MailHog_ for local email testing
* Integration with Sentry_ for error logging

.. _django-environ: https://github.com/joke2k/django-environ
.. _12-Factor: http://12factor.net/
.. _Procfile: https://devcenter.heroku.com/articles/procfile
.. _Mailgun: http://www.mailgun.com/
.. _Whitenoise: https://whitenoise.readthedocs.io/
.. _Celery: http://www.celeryproject.org/
.. _Flower: https://github.com/mher/flower
.. _Anymail: https://github.com/anymail/django-anymail
.. _MailHog: https://github.com/mailhog/MailHog
.. _Sentry: https://sentry.io/welcome/
.. _docker-compose: https://github.com/docker/compose
.. _PythonAnywhere: https://www.pythonanywhere.com/
.. _Traefik: https://traefik.io/
.. _LetsEncrypt: https://letsencrypt.org/
.. _pre-commit: https://github.com/pre-commit/pre-commit

Constraints
-----------

* Only maintained 3rd party libraries are used.
* Uses PostgreSQL everywhere
* Environment variables for configuration (This won't work with Apache/mod_wsgi).

Support this Project!
----------------------

This project is run by volunteers.  If you are considering a donation, I encourage you to support the creators of *cookiecutter-django* in their efforts to maintain it:

* Daniel Roy Greenfeld (`GitHub <https://github.com/pydanny>`_, `Patreon <https://www.patreon.com/danielroygreenfeld>`_)

* Nikita Shupeyko (`GitHub <https://github.com/webyneter>`_)

Usage
------

Let's pretend you want to create a Django project called "redditclone". Rather than using ``startproject``
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter_ to do all the work.

First, get Cookiecutter. Trust me, it's awesome::

    $ pip install "cookiecutter>=1.7.0"

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
    1 - 13.1
    2 - 12.5
    3 - 11.10
    4 - 10.15
    5 - 9.6
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

"Your Stuff"
-------------

Scattered throughout the Python files of this project are places marked with "your stuff". This is where third-party libraries are to be integrated with your project.

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

.. _cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _grid: https://www.djangopackages.com/grids/g/cookiecutters/

Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~

We accept pull requests if they're small, atomic, and make our own project development
experience better.

Articles
---------

* `Using cookiecutter-django with Google Cloud Storage`_ - Mar. 12, 2019
* `cookiecutter-django with Nginx, Route 53 and ELB`_ - Feb. 12, 2018
* `cookiecutter-django and Amazon RDS`_ - Feb. 7, 2018
* `Using Cookiecutter to Jumpstart a Django Project on Windows with PyCharm`_ - May 19, 2017
* `Exploring with Cookiecutter`_ - Dec. 3, 2016
* `Introduction to Cookiecutter-Django`_ - Feb. 19, 2016
* `Django and GitLab - Running Continuous Integration and tests with your FREE account`_ - May. 11, 2016
* `Development and Deployment of Cookiecutter-Django on Fedora`_ - Jan. 18, 2016
* `Development and Deployment of Cookiecutter-Django via Docker`_ - Dec. 29, 2015
* `How to create a Django Application using Cookiecutter and Django 1.8`_ - Sept. 12, 2015

Have a blog or online publication? Write about your cookiecutter-django tips and tricks, then send us a pull request with the link.

.. _`Using cookiecutter-django with Google Cloud Storage`: https://ahhda.github.io/cloud/gce/django/2019/03/12/using-django-cookiecutter-cloud-storage.html
.. _`cookiecutter-django with Nginx, Route 53 and ELB`: https://msaizar.com/blog/cookiecutter-django-nginx-route-53-and-elb/
.. _`cookiecutter-django and Amazon RDS`: https://msaizar.com/blog/cookiecutter-django-and-amazon-rds/
.. _`Exploring with Cookiecutter`: http://www.snowboardingcoder.com/django/2016/12/03/exploring-with-cookiecutter/
.. _`Using Cookiecutter to Jumpstart a Django Project on Windows with PyCharm`: https://joshuahunter.com/posts/using-cookiecutter-to-jumpstart-a-django-project-on-windows-with-pycharm/

.. _`Development and Deployment of Cookiecutter-Django via Docker`: https://realpython.com/blog/python/development-and-deployment-of-cookiecutter-django-via-docker/
.. _`Development and Deployment of Cookiecutter-Django on Fedora`: https://realpython.com/blog/python/development-and-deployment-of-cookiecutter-django-on-fedora/
.. _`How to create a Django Application using Cookiecutter and Django 1.8`: https://www.swapps.io/blog/how-to-create-a-django-application-using-cookiecutter-and-django-1-8/
.. _`Introduction to Cookiecutter-Django`: http://krzysztofzuraw.com/blog/2016/django-cookiecutter.html
.. _`Django and GitLab - Running Continuous Integration and tests with your FREE account`: http://dezoito.github.io/2016/05/11/django-gitlab-continuous-integration-phantomjs.html

Code of Conduct
---------------

Everyone interacting in the Cookiecutter project's codebases, issue trackers, chat
rooms and mailing lists are expected to follow the `PyPA Code of Conduct`_.


.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/
