Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: none

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.2).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.2 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.1.5
-----
2015-10-05

- Removing `mock` dependency from `install_requires` to `tests_require`.

0.1.4
-----
2015-10-02

- Minor Django 1.4 fixes in the `user` module.

0.1.3
-----
2015-08-25

- Recreated release under 0.1.3 on PyPI due to upload error.

0.1.2
-----
2015-08-25

- Python 2.6 fixes.

0.1.1
-----
2015-02-15

- Tests for ``versions`` sub-module added.

0.1
---
2015-02-14

- Initial release with `versions` and `user` modules.
