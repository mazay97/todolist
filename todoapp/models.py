# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models


# Create your models here.
class ToDo(models.Model):
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')


class User(models.Model):
    name = models.CharField(max_length=200)


class UserToDo(models.Model):
    class Meta:
        unique_together = (('todo', 'user'),)

    todo = models.ForeignKey(ToDo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
