from django_medusa.renderers import StaticSiteRenderer
from base.models import Instructor
from django.core.urlresolvers import reverse


class HomeRenderer(StaticSiteRenderer):
    def get_paths(self):
        paths = [reverse('home')]
        return paths

class InstructorRenderer(StaticSiteRenderer):

    def get_paths(self):
        paths = ['',]
        items = Instructor.objects.all()
        for item in items:
            paths.append(reverse('instructor_profile', kwargs={"pg_name":item.page_name}))

        return paths + [reverse('certification')]


renderers = [HomeRenderer, InstructorRenderer, ]