from django.conf.urls import url
from . import views

app_name='libapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<book_id>[0-9]+)/$', views.details, name='details'),
]

 