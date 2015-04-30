from django.db import models
from django.db.models.signals import pre_save
from util.storage import OverwriteStorage
# Create your models here.


class Instructor(models.Model):
    """Instructor's name, nick name, head photo and one big photo for detail show"""
    name = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50)
    img_head = models.ImageField(upload_to="insturctors", default=None, storage=OverwriteStorage())
    img_profile = models.ImageField(upload_to="insturctors", default=None, storage=OverwriteStorage())
    detail = models.TextField(default=None, null=True, blank=True)
    ski = models.BooleanField(default=None)
    snowboard = models.BooleanField(default=None)

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
                statement = statement
            )

class Carousel(models.Model):
    img = models.ImageField(upload_to="carousel", storage=OverwriteStorage())
    text = models.TextField(default=None, null=True, blank=True)
    slide_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.slide_id)


