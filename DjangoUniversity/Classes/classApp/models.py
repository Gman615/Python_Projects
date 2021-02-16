from django.db import models

# Create your models here.


class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    course_num = models.IntegerField()
    instructor_name = models.CharField(max_length=60)
    duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.title