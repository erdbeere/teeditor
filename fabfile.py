#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import mkdir
from os.path import isdir

from fabric.api import local

from teeditor.application import Teeditor


def _make_app(debug=False):
    return Teeditor('sqlite:///dev.db')


def create_virtualenv(directory=None):
    if directory is None:
        directory = '../teeditor-venv'
    local('python ./make-bootstrap.py > bootstrap.py', capture=False)
    local('python ./bootstrap.py --no-site-packages {0}'.format(directory),
          capture=False)


def runserver():
    from werkzeug import run_simple
    app = _make_app()
    run_simple('localhost', 8080, app, threaded=False, processes=1,
               use_debugger=True, use_reloader=True)
