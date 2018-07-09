from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url('^libapp/', include('libapp.urls')),
    url('^admin/', admin.site.urls),
]