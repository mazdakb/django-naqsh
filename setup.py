#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Our version ALWAYS matches the version of Django we support
# If Django has a new release, we branch, tag, then update this setting after the tag.
version = "2.2.0"

if sys.argv[-1] == "tag":
    os.system('git tag -a %s -m "version %s"' % (version, version))
    os.system("git push --tags")
    sys.exit()

with open("README.rst") as readme_file:
    long_description = readme_file.read()

setup(
    name="django-naqsh",
    version=version,
    description="Naqsh is a bootstrapping tool for quickly creating production-ready Django web services.",
    long_description=long_description,
    author="Mazdak Badakhshan",
    author_email="geraneum@gmail.com",
    url="https://github.com/mazdakb/django-naqsh",
    packages=[],
    license="BSD",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
        "Natural Language :: English",
        "Intended Audience :: Developers",
    ],
    keywords=(
        "cookiecutter, Python, projects, project templates, "
        "django, skeleton, scaffolding, web service, REST,"
    ),
)
