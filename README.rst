===========
django-nine
===========
`django-nine` - compatibility library for Django.

Installation
============
1. Install latest stable version from PyPI:

.. code-block:: none

    $ pip install django-nine

Or latest stable version from GitHub:

.. code-block:: none

    $ pip install -e git+https://github.com/barseghyanartur/django-nine@stable#egg=django-nine

Or latest stable version from BitBucket:

.. code-block:: none

    $ pip install -e hg+https://bitbucket.org/barseghyanartur/django-nine@stable#egg=django-nine

Usage
=====
For example, if Django version installed in your environment is 1.7.4, then
the following would be true.

.. code-block:: python

    from nine import versions

    versions.DJANGO_1_7 # True
    versions.DJANGO_LTE_1_7 # True
    versions.DJANGO_GTE_1_7 # True
    versions.DJANGO_GTE_1_8 # False
    versions.DJANGO_GTE_1_4 # True
    versions.DJANGO_LTE_1_6 # False

Or you could safely import the user model as follows:

.. code-block:: python

    from nine.user import User

License
=======
GPL 2.0/LGPL 2.1

Support
=======
For any issues contact me at the e-mail given in the `Author` section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
