from nine import versions as nine_versions

__title__ = 'nine.versions'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2015-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = [
    'versions',
]


def versions(request):
    """Get active theme.

    :param django.http.HttpRequest request:
    :return dict:
    """
    return {'VERSIONS': nine_versions}
