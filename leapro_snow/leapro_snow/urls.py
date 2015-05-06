from django.conf.urls import patterns, include, url
from django.contrib import admin
from leapro_snow import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'leapro_snow.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'base.views.home'),
    url(r'^instructors/(?P<pg_name>[\w-]+)/$', 'base.views.instructor_profile',
        name='instructor_profile'),
)

