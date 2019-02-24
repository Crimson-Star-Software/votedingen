from django.db import models
from django.contrib.auth.models import User


class Candidate(models.Model):
    def __repr__(self):
        return f"<Candidate {self.name}>"

    def __str__(self):
        return self.name
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    title = models.CharField(max_length=255)


class Election(models.Model):
    def __repr__(self):
        return f"<Election '{self.title}'>"

    def __str__(self):
        return self.title
    title = models.CharField(max_length=255)
    isOpen = models.BooleanField(default=False)
    candidates = models.ManyToManyField(Candidate)
    created_at = models.DateTimeField(auto_now_add=True)


class Voter(models.Model):
    def __str__(self):
        return self.user.username

    def __repr__(self):
        return f"<Voter: '{self.user.username}'>"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    running_as = models.ForeignKey(Candidate, on_delete=models.SET_NULL,
                                    null=True)
    voting_in = models.ForeignKey(Election, on_delete=models.SET_NULL,
                                  null=True)
