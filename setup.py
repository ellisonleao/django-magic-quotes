# -*- encoding: utf-8 -*-

import os
from setuptools import setup, find_packages

from quotes import VERSION

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='django-taggit',
    version=".".join(map(str, VERSION)),
    description='django-magic-quotes is a Django application for adding quotes to your site.',
    long_description=readme,
    author=u'Ellison Leão, Rael Max',
    author_email='ellisonleao@gmail.com',
    url='http://github.com/ellisonleao/django-magic-quotes/tree/master',
    packages=find_packages(),
    zip_safe=False,
    package_data = {
        'quotes': [
            'locale/*/LC_MESSAGES/*',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    test_suite='quotes.tests.runtests.runtests'
)

