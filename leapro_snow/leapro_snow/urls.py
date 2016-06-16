from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from base import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^instructors/(?P<pg_name>[\w-]+)/$', views.instructor_profile,
      name='instructor_profile'),
    url(r'^certification/$', views.certification_page,
      name='certification'),
    # url(r'^/$', include('base.urls')),
    # url(r'^$', RedirectView.as_view(url='/Leapro-snow/', permanent=True)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

