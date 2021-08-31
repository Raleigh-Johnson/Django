from django.db import models


class Person(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.CharField(max_length=60, default="", blank=True, null=False)
    instructor = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    objects = models.Manager()

    Person1 =('Math', '0', 'Smith', '.5')
    Person1.save()
    Person2 = ('English', '1', 'Jeff', '.5')
    Person2.save()
    Person3 = ('Math', '0', 'Davids', '1')
    Person3.save()

