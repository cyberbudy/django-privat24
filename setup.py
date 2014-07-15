#!/usr/bin/env python
#coding: utf-8
from setuptools import setup

import sys
import os
reload(sys).setdefaultencoding("UTF-8")

def get_long_desc():
    setup_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(setup_dir, 'README.rst')
    return open(filename).read().decode('utf8')

setup(
    name='django-privat24',
    version='0.1',

    packages=['privat24'],
    include_package_data=True,

#    url='http://bitbucket.org/denger/django-onpay/',
#    download_url = 'http://bitbucket.org/denger/django-onpay/get/tip.zip',
    license = 'MIT License',
    description = u'Приложение для интеграции платежной системы PRIVAT24 в проекты на Django.'.encode('utf8'),
    long_description = get_long_desc(),
    author='Igor Nephedov',
    author_email='igonef@pisem.net',
    install_requires=[
        'django>=1.5'
    ],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', # example license
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)