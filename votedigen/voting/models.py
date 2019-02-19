from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    title = models.CharField(max_length=255)

class Election(models.Model):
    title = models.CharField(max_length=255)
    isOpen = models.BooleanField(default=False)
    candidates = models.ManyToManyField(Candidate)
    created_at = models.DateTimeField(auto_now_add=True)