from django.conf.urls import url
from . import views

app_name='libapp'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^(?P<book_id>[0-9]+)/review/$', views.review, name='review'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
    url(r'^(?P<book_id>[0-9]+)/rate/$', views.rate, name='rate'),
]

 