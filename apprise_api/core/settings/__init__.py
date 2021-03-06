# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Chris Caron <lead2gold@gmail.com>
# All rights reserved.
#
# This code is licensed under the MIT License.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files(the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions :
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import os

# Base Directory (relative to settings)
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY', '+reua88v8rs4j!bcfdtinb-f0edxazf!$x_q1g7jtgckxd7gi=')

# SECURITY WARNING: don't run with debug turned on in production!
# If you want to run this app in DEBUG mode, run the following:
#
#    ./manage.py runserver --settings=core.settings.debug
#
# Or alternatively run:
#
#    export DJANGO_SETTINGS_MODULE=core.settings.debug
#    ./manage.py runserver
DEBUG = bool(os.environ.get("DEBUG", False))

# allow all hosts by default otherwise read from the
# ALLOWED_HOSTS environment variable
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(' ')

# Application definition
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',

    # Apprise API
    'api',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Static files relative path (CSS, JavaScript, Images)
STATIC_URL = '/s/'

# The location to store Apprise configuration files
APPRISE_CONFIG_DIR = os.environ.get(
    'APPRISE_CONFIG_DIR', os.path.join(BASE_DIR, 'var', 'config'))

# Stateless posts to /notify/ will resort to this set of URLs if none
# were otherwise posted with the URL request.
APPRISE_STATELESS_URLS = os.environ.get('APPRISE_STATELESS_URLS', '')
