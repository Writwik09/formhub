#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

from django.conf.urls.defaults import *
from . import views

urlpatterns = patterns('',
    # list that ODK Collect uses to download forms
    url(r"^formList$", views.formList),
    # url where ODK Collect submits data
    url(r"^submission$", views.submission),
    url(r"^survey-list/?$", views.export_list),
    url(r"^export_spreadsheet/(?P<id_string>[^/]*)\.xls$", views.xls),
    url(r"^$", views.dashboard),
    url(r"^data/map_data/?$", views.map_data_points),
    url(r"^submission-counts/(\w+)/(\w+)$", views.frequency_table),
    url(r"^survey/(?P<pk>\d+)/$", views.survey),
)