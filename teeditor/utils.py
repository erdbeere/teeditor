# -*- coding: utf-8 -*-
import os

from jinja2 import Environment, FileSystemLoader
from sqlalchemy import MetaData
from sqlalchemy.orm import create_session, scoped_session
from werkzeug import Local, LocalManager, Response

local = Local()
local_manager = LocalManager([local])
jinja_env = Environment(loader=FileSystemLoader(os.path.join('teeditor',
                                                             'templates')))
application = local('application')
metadata = MetaData()
db = scoped_session(lambda: create_session(application.database_engine,
                                           autocommit=False, autoflush=False))
def render_template(template_name, **context):
    template = jinja_env.get_template(template_name)
    return Response(template.render(**context), mimetype='text/html')
