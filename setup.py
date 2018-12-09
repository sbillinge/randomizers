#!/usr/bin/env python
# coding=utf-8
"""The randomizer installer."""
from __future__ import print_function
import os
import sys

try:
    from setuptools import setup
    from setuptools.command.develop import develop

    HAVE_SETUPTOOLS = True
except ImportError:
    from distutils.core import setup

    HAVE_SETUPTOOLS = False

from randomizers import __version__ as RA_VERSION


def main():
    try:
        if "--name" not in sys.argv:
            print(logo)
    except UnicodeEncodeError:
        pass
    with open(os.path.join(os.path.dirname(__file__), "README.rst"), "r") as f:
        readme = f.read()
    skw = dict(
        name="randomizers",
        description="various randomizers for helping with teaching and all "
                    "kinds of tasks that involve dividing people and things up "
                    "randomly",
        long_description=readme,
        license="CC0",
        version='0.4.0',
        author="Simon Billinge",
        maintainer="Simon Billinge",
        author_email="simon.billinge@gmail.com",
        url="https://github.com/sbillinge/randomizers",
        platforms="Cross Platform",
        classifiers=["Programming Language :: Python :: 3"],
        packages=["randomizers"],
        package_dir={"randomizers": "randomizers"},
        zip_safe=False,
    )
    if HAVE_SETUPTOOLS:
        skw["setup_requires"] = []
        # skw['install_requires'] = ['Jinja2', 'pymongo']
    setup(**skw)


logo = """
"""

if __name__ == "__main__":
    main()
