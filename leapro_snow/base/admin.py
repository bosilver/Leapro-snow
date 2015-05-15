from django.contrib import admin

# Register your models here.
from base.models import Instructor, Carousel, Certification

admin.site.register(Instructor)
admin.site.register(Carousel)
admin.site.register(Certification)
