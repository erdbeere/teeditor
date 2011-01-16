# -*- coding: utf-8 -*-
import os

from sqlalchemy import create_engine
from werkzeug import SharedDataMiddleware, ClosingIterator, Request, \
                     Local, LocalManager, Response

from teeditor import views
from teeditor.urls import url_map
from teeditor.utils import local, local_manager, render_template, db

class Teeditor(object):
    """Central application object.

    :param db_uri: The database uri which should be used.
    """

    def __init__(self, db_uri):
        local.application = self
        self.database_engine = create_engine(db_uri, convert_unicode=False)
        self.dispatch = SharedDataMiddleware(self.dispatch, {
            '/static/': os.path.join(os.path.dirname(__file__), 'static')
        })

    def dispatch(self, environ, start_response):
        adapter = url_map.bind_to_environ(environ, server_name='localhost')
        request = Request(environ)
        endpoint, args = adapter.match()
        names = endpoint.split('/')
        view = views
        for name in names:
            if not hasattr(view, endpoint):
                __import__(view.__name__, None, None, [name])
            view = getattr(view, name)
        response = view(request)
        return ClosingIterator(response(environ, start_response), [db.remove, local_manager.cleanup])

    def __call__(self, environ, start_response):
        return self.dispatch(environ, start_response)
