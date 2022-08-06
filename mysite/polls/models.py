from django.db import models

# Create your models here.

import datetime

from django.db import models
from django.utils import timezone

"""
Here, each model is represented by a class that subclasses django.db.models.Model.
https://docs.djangoproject.com/en/4.1/ref/models/instances/#django.db.models.Model

Each field is represented by an instance of the Field class:
https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.Field

"""


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') # if not given human readable name like so, would use machine variable name

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


