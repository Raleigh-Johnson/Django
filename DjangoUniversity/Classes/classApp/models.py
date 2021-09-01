from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(blank=True, null=False)
    instructor = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    Person1 = ('Math', '0', 'Smith', '.5')
    Person2 = ('English', '1', 'Jeff', '.5')
    Person3 = ('Math', '0', 'Davids', '1')
    objects = models.Manager()



