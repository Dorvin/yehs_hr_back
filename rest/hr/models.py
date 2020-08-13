from django.db import models

class Event(models.Model):
    name = models.CharField()
    category = models.CharField()
    date = models.CharField()       # e.g. 202010 (meaning 2020 year 10 month)

class Member(models.Model):
    code = models.CharField()       # id of yehs website
    name = models.CharField()
    email = models.CharField()
    phone = models.CharField()
    yn = models.CharField()         # yehs number
    fn = models.CharField()         # forum number
    univ = models.CharField()
    major = models.CharField()
    events = models.ManyToManyField(Event, related_name='participants')