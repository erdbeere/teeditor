# -*- coding: utf-8 -*-
from teeditor.utils import render_template

def index(request):
    return render_template('portal/index.html')
