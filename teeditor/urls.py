# -*- coding: utf-8 -*-
from werkzeug.routing import Map, Rule, Submount, Subdomain, EndpointPrefix

url_map = Map([
    Rule('/', endpoint='portal/index'),
    Rule('/static/<file>/', endpoint='static', build_only=True),
])
