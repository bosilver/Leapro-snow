from django.db import models
from django.contrib.flatpages.models import FlatPage
# Create your models here.


class Instructor(models.Model):
    """Instructor's name, nick name, head photo and one big photo for detail show"""
    name = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50)
    img_head = models.ImageField(upload_to="insturctors", default=None)
    ski = models.BooleanField(default=None)
    snowboard = models.BooleanField(default=None)
    img_profile = models.ImageField(upload_to="insturctors", default=None, null=True, blank=True)
    location = models.CharField(max_length=200, default=None, null=True, blank=True)
    cert = models.TextField(default=None, null=True, blank=True)
    ski_field = models.TextField(default=None, null=True, blank=True)
    mostlike_ski_field = models.CharField(max_length=200, default=None, null=True, blank=True)
    want_to_say = models.TextField(default=None, null=True, blank=True)
    vedio = models.TextField(default=None, null=True, blank=True)
    page_name = models.CharField(max_length=50, default=None, null=True)

    def __unicode__(self):
        return self.nick_name

    def show(self):
        statement = ''
        if self.ski:
            statement += 'Ski'
            if self.snowboard:
                statement += ' & '
        if self.snowboard:
            statement += 'Snowboard'

        return dict(
                name = self.name,
                nick_name = self.nick_name,
                img_head = self.img_head,
                statement = statement,
                page_name = self.page_name
            )

    def profile(self):

        base_dict = self.show()
        base_dict.update(dict(
                img_profile = self.img_profile,
                location = self.location,
                cert = self.cert,
                ski_field = self.ski_field,
                mostlike_ski_field = self.mostlike_ski_field,
                want_to_say = self.want_to_say,
                vedio = self.vedio
            ))
        return base_dict


class Carousel(models.Model):
    img = models.ImageField(upload_to="carousel")
    text = models.TextField(default=None, null=True, blank=True)
    slide_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.slide_id)

    def show(self):
        return dict(
                id = self.slide_id,
                url = self.img.url,
                text = self.text
            )


