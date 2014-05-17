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
