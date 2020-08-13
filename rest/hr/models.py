from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=1000)
    category = models.CharField(max_length=1000)
    date = models.CharField(max_length=1000)       # e.g. 202010 (meaning 2020 year 10 month)

class Member(models.Model):
    code = models.CharField(max_length=1000)       # id of yehs website
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    yn = models.CharField(max_length=1000)         # yehs number
    fn = models.CharField(max_length=1000)         # forum number
    univ = models.CharField(max_length=1000)
    major = models.CharField(max_length=1000)
    events = models.ManyToManyField(Event, related_name='participants')