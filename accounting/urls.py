# Copyright (c) 2015-2016 Data King Ltd
# See LICENSE file for license details

from django.conf.urls import *

from accounting.views import *

urlpatterns = patterns(
    '',
    url(
        r'^general-ledger/(?P<fy>\d+)/$',
        GeneralLedgerView.as_view(),
        name='general_ledger'
    ),
    url(
        r'^general-journal/(?P<fy>\d+)/$',
        JournalView.as_view(),
        name='general_journal'
    ),
    url(
        r'^journal/(?P<fy>\d+)/(?P<code>[^/]+)/$',
        JournalView.as_view(),
        name='journal'
    )
)
