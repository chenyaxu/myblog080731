from django.conf.urls import url

from blog.feeds import AllPostRssFeed
from .views import index, postListView, post_detail, archives, category, post_tags, search

urlpatterns = [
    url(r'^index/$', index, name='index'),
    # url(r'^index/$', postListView.as_view(), name='index'),
    url(r'^post_detail/(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', archives, name='archives'),
    url(r'^category/(?P<id>\d+)/$', category, name='category'),
    url(r'^post_tags/(\d+)/$', post_tags, name='post_tags'),
    # url(r'^search/$', search, name='search'),
]