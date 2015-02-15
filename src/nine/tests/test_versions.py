__title__ = 'nine.tests.test_versions'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('VersionsTest',)

import unittest
import mock

import django

from nine.tests.base import print_info

class VersionsTest(unittest.TestCase):
    """
    Tests of ``nine.versions`` module.
    """
    def setUp(self):
        pass

    @print_info
    def __test_django_1_6_5(self):
        """
        Tests as if we were using Django==1.6.5.
        """
        with mock.patch('django.get_version') as get_version:
            get_version.return_value = '1.6.5'
            from nine import versions

            self.assertTrue(not versions.DJANGO_1_4)
            self.assertTrue(not versions.DJANGO_LTE_1_4)
            self.assertTrue(not versions.DJANGO_1_5)
            self.assertTrue(not versions.DJANGO_LTE_1_5)
            self.assertTrue(versions.DJANGO_1_6)
            self.assertTrue(versions.DJANGO_LTE_1_7)
            self.assertTrue(versions.DJANGO_LTE_1_8)
            self.assertTrue(versions.DJANGO_GTE_1_4)
            self.assertTrue(versions.DJANGO_GTE_1_5)
            self.assertTrue(versions.DJANGO_GTE_1_6)
            self.assertTrue(not versions.DJANGO_GTE_1_7)

    @print_info
    def test_django_1_8_a1(self):
        """
        Tests as if we were using Django==1.8.a1.
        """
        with mock.patch('django.get_version') as get_version:
            get_version.return_value = '1.8.a1'
            from nine import versions

            self.assertTrue(not versions.DJANGO_1_4)
            self.assertTrue(not versions.DJANGO_LTE_1_4)
            self.assertTrue(not versions.DJANGO_1_5)
            self.assertTrue(not versions.DJANGO_LTE_1_5)
            self.assertTrue(versions.DJANGO_1_8)
            self.assertTrue(versions.DJANGO_LTE_1_9)
            self.assertTrue(versions.DJANGO_LTE_1_8)
            self.assertTrue(versions.DJANGO_GTE_1_4)
            self.assertTrue(versions.DJANGO_GTE_1_5)
            self.assertTrue(versions.DJANGO_GTE_1_6)
            self.assertTrue(versions.DJANGO_GTE_1_7)
            self.assertTrue(versions.DJANGO_GTE_1_8)
            self.assertTrue(not versions.DJANGO_GTE_1_9)

if __name__ == "__main__":
    unittest.main()
