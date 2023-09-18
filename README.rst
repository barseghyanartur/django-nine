===========
django-nine
===========
`django-nine` - version checking library for Django.

.. image:: https://img.shields.io/pypi/v/django-nine.svg
   :target: https://pypi.python.org/pypi/django-nine
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/django-nine.svg
    :target: https://pypi.python.org/pypi/django-nine/
    :alt: Supported Python versions

.. image:: https://github.com/barseghyanartur/django-nine/actions/workflows/test.yml/badge.svg
   :target: https://github.com/barseghyanartur/django-nine/actions/workflows/test.yml
   :alt: Build Status

.. image:: https://readthedocs.org/projects/django-nine/badge/?version=latest
    :target: http://django-nine.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/license-GPL--2.0--only%20OR%20LGPL--2.1--or--later-blue.svg
   :target: https://github.com/barseghyanartur/django-nine/#License
   :alt: GPL-2.0-only OR LGPL-2.1-or-later

.. image:: https://coveralls.io/repos/github/barseghyanartur/django-nine/badge.svg?branch=master
    :target: https://coveralls.io/github/barseghyanartur/django-nine?branch=master
    :alt: Coverage

Prerequisites
=============
- Python 3.7, 3.8, 3.9, 3.10 and 3.11
- Django 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 2.0, 2.1, 2.2, 3.0, 3.1, 3.2,
  4.0, 4.1 and 4.2

Documentation
=============
Documentation is available on `Read the Docs
<http://django-nine.readthedocs.io/>`_.

Installation
============
Install latest stable version from PyPI:

.. code-block:: sh

    pip install django-nine

Or latest stable version from GitHub:

.. code-block:: sh

    pip install https://github.com/barseghyanartur/django-nine/archive/stable.zip

Usage
=====
Get Django versions
-------------------
In code
~~~~~~~
For example, if Django version installed in your environment is 1.7.4, then
the following would be true.

.. code-block:: python

    from django_nine import versions

    versions.DJANGO_1_7  # True
    versions.DJANGO_LTE_1_7  # True
    versions.DJANGO_GTE_1_7  # True
    versions.DJANGO_GTE_1_8  # False
    versions.DJANGO_GTE_1_4  # True
    versions.DJANGO_LTE_1_6  # False

In templates
~~~~~~~~~~~~
With use of context processors
##############################
Add ``nine.context_processors.versions`` to your context processors.

.. code-block:: python

    TEMPLATES[0]['OPTIONS']['context_processors'] += \
        ['django_nine.context_processors.versions']

Or if you are using an old version of Django:

.. code-block:: python

    TEMPLATE_CONTEXT_PROCESSORS += ['django_nine.context_processors.versions']

Testing
=======
Simply type:

.. code-block:: sh

    ./runtests.py

Or use tox:

.. code-block:: sh

    tox

Or use tox to check specific env:

.. code-block:: sh

    tox -e py37

Or run Django tests:

.. code-block:: sh

    ./manage.py test nine --settings=settings.testing

License
=======
GPL-2.0-only OR LGPL-2.1-or-later

Support
=======
For any security issues contact me at the e-mail given in the `Author`_ section.
For overall issues, go to `GitHub <https://github.com/barseghyanartur/django-nine/issues>`_.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
