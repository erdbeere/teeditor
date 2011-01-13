#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import mkdir
from os.path import isdir

from fabric.api import local

def create_virtualenv(directory=None):
    if directory is None:
        directory = '../teeditor-venv'
    local('python ./make-bootstrap.py > bootstrap.py', capture=False)
    local('python ./bootstrap.py --no-site-packages {0}'.format(directory),
          capture=False)
