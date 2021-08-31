from django.contrib import admin
from  . import models

class Person(admin.Person):
    pass


admin.site.register(Person)

# Register your models here.
