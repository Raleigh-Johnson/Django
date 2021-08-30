from django.db import models

class Classes(models.Model):
    title = models.CharField(max_length=60, default="", blank=True)
    number = models.IntegerField(max_length=60, default="", blank=True, null=False)
    instructor = models.CharField(max_length=60, default="", blank=True)
    duration = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)

    objects = models.Manager()
    """
    Person1=(title="", number="0", instructor="Smith", duration=".5")
    Person1.save()
    Person2 = p(title="English", number="1", instructor="Doe", duration="1")
    Person2.save()
    Person3 = p(title="History", number="2", instructor="Winston", duration=".5")
    Person3.save() """
    def __str__(self):
        return self.title
# Create your models here.
