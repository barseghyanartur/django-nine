"""
Compatibility module. Contains information about the current Django version in
use, including (LTE and GTE statements).
"""

__title__ = 'nine.versions'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'LOOSE_DJANGO_VERSION', 'LOOSE_DJANGO_MINOR_VERSION',

    'DJANGO_1_4', 'DJANGO_1_5', 'DJANGO_1_6', 'DJANGO_1_7', 'DJANGO_1_8',
    'DJANGO_1_9', 'DJANGO_2_0',

    'DJANGO_GTE_1_4', 'DJANGO_GTE_1_5', 'DJANGO_GTE_1_6', 'DJANGO_GTE_1_7',
    'DJANGO_GTE_1_8', 'DJANGO_GTE_1_9', 'DJANGO_GTE_2_0',

    'DJANGO_LTE_1_4', 'DJANGO_LTE_1_5', 'DJANGO_LTE_1_6', 'DJANGO_LTE_1_7',
    'DJANGO_LTE_1_8', 'DJANGO_LTE_1_9', 'DJANGO_LTE_2_0',
)

from distutils.version import LooseVersion

import django

LOOSE_DJANGO_VERSION = LooseVersion(django.get_version())
LOOSE_DJANGO_MINOR_VERSION = LooseVersion('.'.join([str(i) for i in LOOSE_DJANGO_VERSION.version[0:2]]))
LOOSE_VERSION_1_4 = LooseVersion('1.4')
LOOSE_VERSION_1_5 = LooseVersion('1.5')
LOOSE_VERSION_1_6 = LooseVersion('1.6')
LOOSE_VERSION_1_7 = LooseVersion('1.7')
LOOSE_VERSION_1_8 = LooseVersion('1.8')
LOOSE_VERSION_1_9 = LooseVersion('1.9')
LOOSE_VERSION_2_0 = LooseVersion('2.0')
LOOSE_VERSION_2_1 = LooseVersion('2.0')

# Exact versions
DJANGO_1_4 = LOOSE_VERSION_1_4 <= LOOSE_DJANGO_VERSION < LOOSE_VERSION_1_5
DJANGO_1_5 = LOOSE_VERSION_1_5 <= LOOSE_DJANGO_VERSION < LOOSE_VERSION_1_6
DJANGO_1_6 = LOOSE_VERSION_1_6 <= LOOSE_DJANGO_VERSION < LOOSE_VERSION_1_7
DJANGO_1_7 = LOOSE_VERSION_1_7 <= LOOSE_DJANGO_VERSION < LOOSE_VERSION_1_8
DJANGO_1_8 = LOOSE_VERSION_1_8 <= LOOSE_DJANGO_VERSION < LOOSE_VERSION_1_9
DJANGO_1_9 = LOOSE_VERSION_1_9 <= LOOSE_DJANGO_VERSION < LOOSE_VERSION_2_0
DJANGO_2_0 = LOOSE_VERSION_2_0 <= LOOSE_DJANGO_VERSION < LOOSE_VERSION_2_1

# LTE list
DJANGO_LTE_1_4 = LOOSE_DJANGO_MINOR_VERSION <= LOOSE_VERSION_1_4
DJANGO_LTE_1_5 = LOOSE_DJANGO_MINOR_VERSION <= LOOSE_VERSION_1_5
DJANGO_LTE_1_6 = LOOSE_DJANGO_MINOR_VERSION <= LOOSE_VERSION_1_6
DJANGO_LTE_1_7 = LOOSE_DJANGO_MINOR_VERSION <= LOOSE_VERSION_1_7
DJANGO_LTE_1_8 = LOOSE_DJANGO_MINOR_VERSION <= LOOSE_VERSION_1_8
DJANGO_LTE_1_9 = LOOSE_DJANGO_MINOR_VERSION <= LOOSE_VERSION_1_9
DJANGO_LTE_2_0 = LOOSE_DJANGO_MINOR_VERSION <= LOOSE_VERSION_2_0

# GTE list
DJANGO_GTE_1_4 = LOOSE_DJANGO_MINOR_VERSION >= LOOSE_VERSION_1_4
DJANGO_GTE_1_5 = LOOSE_DJANGO_MINOR_VERSION >= LOOSE_VERSION_1_5
DJANGO_GTE_1_6 = LOOSE_DJANGO_MINOR_VERSION >= LOOSE_VERSION_1_6
DJANGO_GTE_1_7 = LOOSE_DJANGO_MINOR_VERSION >= LOOSE_VERSION_1_7
DJANGO_GTE_1_8 = LOOSE_DJANGO_MINOR_VERSION >= LOOSE_VERSION_1_8
DJANGO_GTE_1_9 = LOOSE_DJANGO_MINOR_VERSION >= LOOSE_VERSION_1_9
DJANGO_GTE_2_0 = LOOSE_DJANGO_MINOR_VERSION >= LOOSE_VERSION_2_0
