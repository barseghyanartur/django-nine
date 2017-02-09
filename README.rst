===========
django-nine
===========
`django-nine` - compatibility library for Django.

Prerequisites
=============
- Python 2.6, 2.7, 3.4, 3.5 and 3.6.
- Django 1.5, 1.6, 1.7, 1.8, 1.9, 1.10 and 1.11.

Installation
============
Install latest stable version from PyPI:

.. code-block:: sh

    pip install django-nine

Or latest stable version from GitHub:

.. code-block:: sh

    pip install https://github.com/barseghyanartur/django-nine/archive/stable.zip

Or latest stable version from BitBucket:

.. code-block:: sh

    pip install https://bitbucket.org/barseghyanartur/django-nine/get/stable.zip

Usage
=====
For example, if Django version installed in your environment is 1.7.4, then
the following would be true.

.. code-block:: python

    from nine import versions

    versions.DJANGO_1_7  # True
    versions.DJANGO_LTE_1_7  # True
    versions.DJANGO_GTE_1_7  # True
    versions.DJANGO_GTE_1_8  # False
    versions.DJANGO_GTE_1_4  # True
    versions.DJANGO_LTE_1_6  # False

Or you could safely import the user model as follows:

.. code-block:: python

    from nine.user import User

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

    tox -e py35

Or run Django tests:

.. code-block:: sh

    ./manage.py test nine --settings=settings.testing

License
=======
GPL 2.0/LGPL 2.1

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
