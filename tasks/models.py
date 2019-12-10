from django.db import models
from django.db.models import Model
from django.db.models import CharField as Char
from django.db.models import BooleanField as Boolean
from django.db.models import DateField as Date
from datetime import datetime as dt

# Create your models here.
class Task(Model):
    title = Char(max_length = 200)
    complete = Boolean(default=False)
    created = Date(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.created)