from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from base import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^instructors/(?P<pg_name>[\w-]+)/$', views.instructor_profile,
        name='instructor_profile'),
    url(r'^certification$', views.certification_page,
        name='certification'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

