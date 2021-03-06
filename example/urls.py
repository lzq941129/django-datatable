#!/usr/bin/env python
# coding: utf-8
from django.conf.urls import include, url

import app.views

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', app.views.base, name='base'),
    url(r'^bulk/$',app.views.bulks,name='bulk'),

    url(r'^datasource/ajax/$', app.views.ajax, name='ajax'),
    url(r'^datasource/ajaxsource/$', app.views.ajax_source, name='ajax_source'),
    url(r'^datasource/ajaxsource/api/$', app.views.MyDataView.as_view(), name='ajax_source_api'),

    url(r'^column/sequence/$', app.views.sequence_column, name='sequence_column'),
    url(r'^column/calendar/$', app.views.calendar_column, name='calendar_column'),
    url(r'^column/link/$', app.views.link_column, name='link_column'),
    url(r'^column/checkbox/$', app.views.checkbox_column, name='checkbox_column'),

    url(r'^user/(\d+)/$', app.views.user_profile, name='user_profile'),
    url(r'^table/', include('table.urls')),
    url(r'^admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

