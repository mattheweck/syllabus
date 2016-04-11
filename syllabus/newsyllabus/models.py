from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class uploadedSyllabus(models.Model):
    class_name = models.CharField(max_length=200)
    #text = something for pdf uploads
    teacher_name = models.CharField(max_length=200)
    school_name = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
