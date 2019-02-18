from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=255)


class Election(models.Model):
    title = models.CharField(max_length=255)
    isOpen = models.BooleanField(default=False)
    candidates = models.ManyToManyField(Candidate)
