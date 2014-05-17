from django.conf.urls import include, url
from .views import (BuilderListView, BuilderDetailView, BuilderUpdateView,
                    BuilderDeleteView, ReviewListView, ReviewDetailView,
                    ReviewUpdateView)

urlpatterns = [
    url(r'^$', BuilderListView.as_view(), name='builder.list'),
    url(r'^(?P<slug>[\w-]+)/$', BuilderDetailView.as_view(), name='builder.detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', BuilderUpdateView.as_view(), name='builder.edit'),
    url(r'^(?P<slug>[\w-]+)/delete/$', BuilderDeleteView.as_view(), name='builder.delete'),
    url(r'^(?P<builder>[\w-]+)/reviews/$', ReviewListView.as_view(), name='review.list'),
    url(r'^(?P<builder>[\w-]+)/reviews/(?P<slug>[\w-]+)/$', ReviewDetailView.as_view(), name='review.detail'),
    url(r'^(?P<builder>[\w-]+)/reviews/(?P<slug>[\w-]+)/update/$', ReviewUpdateView.as_view(), name='review.edit'),
]
