from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from .Media import Media


class BoardObject(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField()
    height = models.IntegerField()

    posX = models.IntegerField()
    posY = models.IntegerField()

    gcode = models.BinaryField()

    data = models.ForeignKey(Media, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BoardObject, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.title
