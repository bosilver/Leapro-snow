from django.shortcuts import render
from base.models import Instructor, Carousel
from django.contrib.flatpages.models import FlatPage
import json
# Create your views here.
import logging
def get_logger(name):
    log = logging.getLogger(name)

    log.setLevel(logging.DEBUG)

    formatter_verbose = logging.Formatter('%(asctime)s %(levelname)8s %(message)s')
    formatter_short = logging.Formatter('[%(levelname)8s] %(message)s')
    fh = logging.FileHandler('/tmp/Leapro-Snow.log')
    fh.setFormatter(formatter_verbose)
    log.addHandler(fh)
    sh = logging.StreamHandler()
    sh.setFormatter(formatter_short)
    log.addHandler(sh)

    return log
log = get_logger('base')

def home(request):

    car = Carousel.objects.order_by('slide_id')
    carousel = list()
    for item in car:
        carousel.append(item.show())

    ins = Instructor.objects.order_by('name')
    instructors = list()
    for instructor in ins:
        instructors.append(instructor.show())
    about_page = FlatPage.objects.get(url='/home/about/')

    return render(request,
                  'home.html',
                  {'instructors': instructors, 'carousel': json.dumps(carousel),
                  'about_page': about_page})

def instructor_profile(request, pg_name):

    instructor = Instructor.objects.get(page_name=pg_name).profile()

    log.info(instructor)
    return render(request,
                  'instructor.html',
                  {'instructor': instructor})


