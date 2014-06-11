# Copyright 2014 Vypo
#
# message   f=urls.py&n=0b1f0c50eb927691
# sha256    da414a57127c664cce6e42354789c706f187188d2107575cc2cf913329b8b8fb
#
# This file is part of BuilderDB.
#
# BuilderDB is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BuilderDB is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with BuilderDB.  If not, see <http://www.gnu.org/licenses/>.
from django.conf.urls import include, url
from .views import (BuilderListView, BuilderDetailView, BuilderUpdateView,
                    BuilderDeleteView, ReviewListView, ReviewDetailView,
                    ReviewUpdateView, ReviewCreateView, PhotoCreateView,
                    PhotoDeleteView, PhotoDetailView)

urlpatterns = [
    url(r'^$', BuilderListView.as_view(), name='builder.list'),
    url(r'^(?P<slug>[\w-]+)/$', BuilderDetailView.as_view(), name='builder.detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', BuilderUpdateView.as_view(), name='builder.edit'),
    url(r'^(?P<slug>[\w-]+)/delete/$', BuilderDeleteView.as_view(), name='builder.delete'),
    url(r'^(?P<builder>[\w-]+)/review/add/$', ReviewCreateView.as_view(), name='review.create'),
    url(r'^(?P<builder>[\w-]+)/reviews/$', ReviewListView.as_view(), name='review.list'),
    url(r'^(?P<builder>[\w-]+)/reviews/(?P<slug>[\w-]+)/$', ReviewDetailView.as_view(), name='review.detail'),
    url(r'^(?P<builder>[\w-]+)/reviews/(?P<slug>[\w-]+)/update/$', ReviewUpdateView.as_view(), name='review.edit'),
    url(r'^(?P<builder>[\w-]+)/reviews/(?P<slug>[\w-]+)/photo/add/$', PhotoCreateView.as_view(), name='photo.create'),
    url(r'^(?P<builder>[\w-]+)/reviews/(?P<slug>[\w-]+)/photos/(?P<pk>[0-9]+)/delete/$', PhotoDeleteView.as_view(), name='photo.delete'),
    url(r'^(?P<builder>[\w-]+)/reviews/(?P<slug>[\w-]+)/photos/(?P<pk>[0-9]+)/$', PhotoDetailView.as_view(), name='photo.detail'),
]
