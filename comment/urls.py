from django.conf.urls import url
from .views import get_comment

urlpatterns = [
    url(r'^get_comment/(?P<id>\d+)/$', get_comment, name='get_comment'),
]